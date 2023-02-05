import random
from glob import glob
import numpy as np
import pandas as pd
import datetime
import glob
from itertools import combinations
import joblib
import pickle
from itertools import product


pd.set_option('display.max_rows', None)

class EnergySim:


    def __init__(self):

        #Param
        self.weather_file       = "./analysis_data/weather_info.csv"
        self.load_file          = "./analysis_data/new_load_table.csv"
        self.real_temp_file     = './data/real_temp.csv'
        self.oper_record_file   = './analysis_data/15_min_chiller.csv'


        #HyperParam
        self.start_date  = '2021-06-01 00:15'
        self.end_date    = '2021-07-01 00:00'
        self.time_idx    = pd.date_range(start=self.start_date, end=self.end_date, freq='15min')
        self.total_flux  = 16000
        self.buildings   = ['공과대학', '공동실험실습관', '교수회관',
                            '대학본부', '도서관', '동북아경제통상',
                            '복지회관', '사회법과대학', '예체능대학',
                            '인문대학', '자연대학', '정보기술대학',
                            '정보전산원', '컨벤션센터', '학생복지회관']

        self.fluxs      = [3986.28, 1209.48, 848.66, 1259.43, 1531.40,
                           863.21, 1151.27, 102.52, 435.12, 935.72,
                           2013.41, 1212.51, 211.61, 481.76, 593.70]


        self.T_supply    = 11
        self.flux_dict   = self.flux_dict()


        #Plantroom
        self.plantroom_info = [475, 475, 180, 180, 600, 600]
        self.comb_dict = self.get_combination()
        self.operation_dict = self.get_operation_dict()

        #Model
        self.T_return_model = self.T_return_model_load()

        #Data
        self.weather_data = self.weather_loader()
        self.load_data = self.load_loader(self.load_file)
        self.input_data = self.get_input()
        self.real_temp_data = self.get_real_temp()


    def weather_loader(self):
        """
         외기정보 로딩 --> 외기온도, 외기습도
         """
        weather_file = pd.read_csv(self.weather_file)
        table = weather_file[["외기온도", "외기습도"]]
        table.ffill(axis=0, inplace=True)
        table.set_index(self.time_idx, inplace=True)

        return table


    def load_loader(self, load_file):
        """
         냉방부하 로드
         """
        load_file = pd.read_csv(load_file)
        table = pd.DataFrame(load_file['LOAD'])
        table.ffill(axis=0, inplace=True)
        table.set_index(self.time_idx, inplace=True)
        table[table < 0] = -table

        return table


    def get_input(self):
        """
        시뮬레이션 input loading
        날씨, 실제부하
        """
        data_list = []
        data_list.append(self.weather_data)
        data_list.append(self.load_data)
        input_table = pd.concat(data_list, axis=1)

        return input_table


    def get_real_temp(self):
        """
        실제 공급/환수 온도 loading
        """
        table = pd.read_csv(self.real_temp_file, index_col="DATE")
        table.index = pd.to_datetime(table.index)

        return table


    def flux_dict(self):
        """
        Key     : 건물명
        Value   : 유량
        """
        flux_dict = dict()
        for idx, b in enumerate(self.buildings):
            flux_dict[b] = self.fluxs[idx] / sum(self.fluxs)

        return flux_dict


    def sep_demand(self, total_demand):
        """
        유량 비율에 따른 건물 부하 나눔
        """
        demand_list = []

        flux_dict = self.flux_dict

        for b in flux_dict.keys():
            demand_list.append(round(total_demand * flux_dict[b]))

        return demand_list


    def get_building_Tin(self, T_supply):
        """
        건물 별 T_in (random요소 포함)
        """
        T_in_list = []
        for b in range(15):
            T_in_list.append(round(T_supply + random.uniform(0.0, 2.0), 2))

        return T_in_list



    def get_building_Tout(self, demand_list, T_in_list):
        """
        건물 별 T_out 계산
        """
        T_out_list = []
        for idx, demand in enumerate(demand_list):
            flux = self.fluxs[idx]
            T_in = T_in_list[idx]

            kcal_demand = demand * 3024
            lph_flux = flux * 60

            # print(f"demand : {demand}, kcal : {kcal_demand}, flux : {flux}, lph : {lph_flux}")
            T_out = T_in + (kcal_demand / lph_flux)
            T_out_list.append(round(T_out, 2))


        for i in range(len(T_out_list)):
            if demand_list[i] == 0:
                T_out_list[i] += round(random.uniform(0.5, 1.0), 2)


        return T_out_list


    def get_return_model_input(self, T_in_list, T_out_list, past_return):
        """
        환수온도 예측모델 input 생성
        """
        input_list = []
        for i in range(len(T_in_list)):
            input_list.append(T_in_list[i])
            input_list.append(T_out_list[i])

        input_list.append(past_return)
        input = np.array(input_list)
        input = input.reshape(1, len(input))


        return input


    def T_return_model_load(self):
        """
        환수온도 예측모델
        """
        model = joblib.load('./model/return_T_model.pkl')

        return model


    # ----- Plantroom
    def get_combination(self):
        """
        냉동기가 생성할 수 있는 부하의 합과, 조합으로 이루어진 딕셔너리 생성
        dict[부하의 합] = 해당 부하를 만족하기 위해 켜야되는 냉동기
        """
        e_sum_list = []
        comb_dict = dict()
        for i in range(len(self.plantroom_info)):
            com_list = list(combinations(self.plantroom_info, i + 1))

            for c in com_list:
                line = list(c)
                e_sum = sum(line)
                if line.count(600) < 2:
                    line.append(e_sum)
                else:
                    continue

                if e_sum not in e_sum_list:
                    e_sum_list.append(e_sum)
                    comb_dict[line[-1]] = line[:-1]

        return comb_dict



    def get_oper_record(self, time):
        """
        실제 냉동기 운영 기록 loading
        """
        table = pd.read_csv(self.oper_record_file, encoding='utf-8', index_col=0)
        table.set_index(self.time_idx, inplace=True)
        oper_list = table.loc[time].values.tolist()

        return oper_list


    def get_produce_load(self, oper_list):
        """
        냉동기 운영 mode --> 운영 RT로 환산
        """
        produce_load = 0
        for o in range(len(oper_list)):
            produce_load += oper_list[o] * self.plantroom_info[o]

        return produce_load


    def plantroom(self, produce_load, T_return):
        """
        <기계실>
        생산된 부하, 환수온도를 고려하여 공급온도를 계산
        if) 부하생산 X --> 공급온도 = 환수온도 + 0.05
        """
        kcal_produce_load = produce_load * 3024
        lph_total_flux = self.total_flux * 60

        if produce_load == 0:
            self.T_supply = T_return + 0.05

        else:
            self.T_supply = round(-(kcal_produce_load / lph_total_flux) + T_return, 2)

        return self.T_supply


    #Setting
    def temp_increase(self, time, T):
        """
        외기온도에 따른 온도변화 진행
        """

        T += 0.1

        return round(T, 2)


    #RT 2 OPER
    def get_operation_dict(self):
        """
        생성된 RT값 --> 냉동기 운영 mode로 변환
        """
        operation_dict = dict()
        for operation in product([0, 1], repeat=6):
            capa = 0
            for c in range(len(self.plantroom_info)):
                if operation[c] == 1:
                    capa = capa + self.plantroom_info[c] * operation[c]
                    operation_dict[operation] = capa

        operation_dict[(0, 0, 0, 0, 0, 0)] = 0

        return operation_dict


    def operation_selection(self, produce_load, past_oper):
        available_oper = []
        # RT와 일치하는 운영을 모두 가져옴
        for key, value in self.operation_dict.items():
            if value == produce_load:
                available_oper.append(list(key))

        # 이전 운영의 켜져있는 냉동기와 겹치는 냉동기 체크
        count_list = []
        for oper in available_oper:
            c = 0
            for idx in range(len(past_oper)):
                if oper[idx] == 1 and past_oper[idx] == 1:
                    c = c + 1
            count_list.append(c)

        # 동일한 운영이 있을 경우, 그대로 가져옴
        # 그 외의 경우, 가장 겹치는 냉동기가 많은 운영을 가져옴
        max_val = max(count_list)
        if count_list.count(max_val) == 1:
            select_idx = count_list.index(max_val)
            action_operation = available_oper[select_idx]
        else:
            select_idx_list = list(filter(lambda x: count_list[x] == max_val, range(len(count_list))))
            choice = random.choice(select_idx_list)
            action_operation = available_oper[choice]

        return action_operation



    #OPER MODEL
    def threshold_model(self, past_demand, total_demand, time, produce_load):
        """
        임계점 기반 냉동기 운영모델
        """
        # 파라미터
        friday = 4
        load_increase_list = [[180, 655, 395.03],
                              [475, 655, 407.12],
                              [475, 950, 860.57],
                              [655, 1130, 788.57],
                              [950, 1130, 788.57],
                              [1130, 1310, 1055.69]]

        load_decrease_list = [[655, 180, 395.03],
                              [655, 475, 635.02],
                              [950, 475, 635.02],
                              [1130, 655, 801.5],
                              [1130, 950, 949.26],
                              [1310, 1130, 1181.66]]

        if time.dayofweek <= friday:  ##평일
            if time.hour >= 9 and time.hour < 21:  ## 운영 의사결정 시간
                if time.hour == 9 and time.minute == 0:  ## 운영 9:00분 655RT start
                    produce_load = 655

                else:
                    sub_increase_list = []
                    sub_decrease_list = []
                    for i in load_increase_list:  ## 실측부하가 증가할때
                        from_load, to_load, threshold_load, = i[0], i[1], i[2]
                        if produce_load == from_load:
                            if past_demand >= threshold_load:  ## 임계점보다 상승
                                sub_increase_list.append(to_load)
                                sub_increase_list.append(produce_load)
                        elif not sub_increase_list:
                            sub_increase_list.append(produce_load)
                    produce_load = max(sub_increase_list)


                    for j in load_decrease_list:  ##실측부하가 감소할때
                        from_load_, to_load_, threshold_load_, = j[0], j[1], j[2]
                        if produce_load == from_load_:
                            if past_demand <= threshold_load_:
                                sub_decrease_list.append(to_load_)
                                sub_decrease_list.append(produce_load)
                        elif not sub_decrease_list:
                            sub_decrease_list.append(produce_load)


                    if produce_load in sub_decrease_list:
                        produce_load = min(sub_decrease_list)
                    else:
                        produce_load = random.choice(sub_decrease_list)

                    if total_demand == 0:  ##실측부하가 없으면 운영도 x
                        produce_load = 0

            else:  ##운영 의사결정시간 x
                produce_load = 0


        else:  # 주말
            if time.hour >= 9 and time.hour < 21:  ## 운영시간
                produce_load = 600  ## 주말은 터보냉동기만 운영
                if total_demand == 0:  ##실측부하가없으면 운영도 x
                    produce_load = 0

            else:  ## 운영시간x
                produce_load = 0


        return produce_load
