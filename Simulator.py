import pandas as pd
import Energy_Sim_v2

class Main:
    model_list = ['THRESHOLD', 'RECORD']
    model_len = len(model_list)
    
    def run(self):
        for model_id, OPER_MODEL in enumerate(self.model_list):
            ESim = Energy_Sim_v2.EnergySim()
            ESim.get_input()
            T_supply = ESim.T_supply#고정
            return_model = ESim.T_return_model#고정
            time_idx = ESim.time_idx#고정
            time_len = len(time_idx)
            real_temp = ESim.get_real_temp()#고정
            air_temp = ESim.weather_data#고정
            oper_dict = ESim.get_operation_dict()#고정

            sim_inputs = []
            oper_list = []
            produce_load = 0

            #과거정보 저장
            past_return = 14
            past_demand = 0
            past_oper = [0, 0, 0, 0, 0, 0]



            for id, time in enumerate(time_idx):
                total_demand = ESim.load_data.loc[time, "LOAD"]#필

                demands = ESim.sep_demand(total_demand)
                Tin_list = ESim.get_building_Tin(T_supply)
                Tout_list = ESim.get_building_Tout(demands, Tin_list)
                input_list = ESim.get_return_model_input(Tin_list, Tout_list, past_return)

                T_return = round(return_model.predict(input_list)[0], 2)

                #Operation mode
                if OPER_MODEL == 'RECORD':
                    oper_list = ESim.get_oper_record(time)
                    produce_load = oper_list[:2].count(float(1))*475 + oper_list[2:4].count(float(1))*180 + oper_list[4:].count(float(1))*600

                else:
                    produce_load = ESim.threshold_model(past_demand, total_demand, time, produce_load)


                #Produce_load 2 Operation
                oper_list = ESim.operation_selection(produce_load, past_oper)#필


                #Plantroom
                T_supply = ESim.plantroom(produce_load, T_return)


                #Temperature increase
                T_return = ESim.temp_increase(time, T_return)
                T_supply = ESim.temp_increase(time, T_supply)

                #Real data load
                Real_T_SUPPLY = real_temp.loc[time, "T_SUPPLY"]#필
                Real_T_RETURN = real_temp.loc[time, "T_RETURN"]#필
                Real_air_temp = air_temp.loc[time, "외기온도"]#필

                #Past data save
                past_return = T_return
                past_demand = total_demand
                past_oper = oper_list

                str_building_rt = str(demands).replace('[', '').replace(']', '')
                str_building_supply = str(Tin_list).replace('[', '').replace(']', '')
                str_building_return = str(Tout_list).replace('[', '').replace(']', '')

                sim_inputs.append([total_demand, produce_load, oper_list, T_return, T_supply, Real_T_RETURN, Real_T_SUPPLY, time, Real_air_temp, str_building_rt, str_building_supply, str_building_return])
                yield ((time_len*model_id+id)/(time_len*self.model_len))*100
            sim_input_df = pd.DataFrame(sim_inputs)
            sim_input_df.columns = ["total_rt", "produce_load", "operation", "T_return(Simul)", "T_supply(Simul)", "T_return(Real)", "T_supply(Real)", "date", "air_temp", "buildings_rt", "buildings_supply", "buildings_return"]
            sim_input_df.set_index("date", inplace=True)

            sim_input_df.to_csv("./simul_result/{}_result.csv".format(OPER_MODEL))