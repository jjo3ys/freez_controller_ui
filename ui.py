import time
from tkinter import font
import pandas as pd
import tkinter

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

degree_color ={ 7: '00FF00', 7.5:'15FF00', 8:'30FF00', 8.5:'45FF00', 9:'60FF00', 9.5:'75FF00', 10:'90FF00', 10.5:'AAFF00', 11:'BBFF00', 11.5:'CCFF00', 12:'DDFF00', 12.5:'EEFF00', 13:'FFFF00', 13.5:'FFEE00', 14:'FFDD00', 14.5:'FFCC00', 15:'FFBB00', 15.5:'FFAA00', 16:'FF9000', 16.5:'FF6000', 17:'FF3000', 17.5:'FF0000'}

p_x = 210
p_y = 420
window_x = 2250
window_y = 950

def main():
    global canvas, root, supply_graph_canvas, degree_graph_canvas, produced_graph_canvas, building_graph_canvas, norm, bold
    global date_list_box, scroll, play_var
    global absortion1, absortion2, absortion3, absortion4, absortion1_b, absortion2_b, absortion3_b, absortion4_b
    global turbor1, turbor2, turbor3, turbor4, turbor1_b, turbor2_b, turbor3_b, turbor4_b
    global return_pipe, supply_pipe
    global w, h

    root = Tk()
    root.title("Energy ui")
    root.resizable(True, False)
    root.iconbitmap('inu.ico')
    root.geometry('{}x{}'.format(window_x, window_y))
    # root.config(bg='#4E4E4E')
    label = Label(root, text='designed by Yeon-Seong Jo', font=('', 8))
    label.place(x=2050, y=55)
    label = Label(root, text='Industrial Inteligence Lab', font=('', 15, 'bold'), foreground='#000000')#00B3FF
    label.place(x=1965, y=25)
    
    w = 2150
    h = 800
    
    canvas = Canvas(root, width=w, height=h, bg="white", highlightbackground='black')
    canvas.place(x=50, y=75)
    #저, 과공급 그래프
    canvas.create_text(w-205, h-720, text='저·과 공급 그래프', font=('', 15, 'bold'))
    canvas.create_text(w-385, h-430, text='과공급 냉방부하(RT) : ', font=('', 10), anchor='w')
    canvas.create_text(w-385, h-410, text='저공급 냉방부하(RT) : ', font=('', 10), anchor='w')

    supply_graph_canvas = Canvas(canvas, width=360, height=240, bg="white", highlightbackground='black')
    supply_graph_canvas.place(x=w-385, y=h-700)

    supply_graph_canvas.create_line(10, 5, 10, 235)
    supply_graph_canvas.create_text(23, 10, text='RT', font=('', 10))
    supply_graph_canvas.create_line(10, 120, 355, 120)
    supply_graph_canvas.create_text(335, 110, text='시간(h)', font=('', 10))
    
    for i in range(24):
        supply_graph_canvas.create_line(10+i*13.3, 120, 10+i*13.3, 115)
        if i%3 == 2:
            d = i+1
            supply_graph_canvas.create_text(10+d*13.3, 130, text="{}".format(d), font=('', 10))
    
    supply_graph_canvas.create_text(180, 60, text='과공급', fill='gray', font=('', 15))
    supply_graph_canvas.create_text(180, 180, text='저공급', fill='gray', font=('', 15))

    #외기온도 그래프
    canvas.create_text(w-595, h-720, text='외기온도 그래프', font=('', 15, 'bold'))
    canvas.create_text(w-770, h-430, text='외기온도 : ', font=('', 10), anchor='w')

    degree_graph_canvas = Canvas(canvas, width=360, height=240, bg='white', highlightbackground='black')
    degree_graph_canvas.place(x=w-770, y=h-700)

    degree_graph_canvas.create_line(5, 220, 355, 220)
    degree_graph_canvas.create_text(335, 210, text='시간(h)', font=('', 10))
    for i in range(25):
        degree_graph_canvas.create_line(20+i*13.3, 220, 20+i*13.3, 215)
        if i%3 == 2:
            d = i+1
            degree_graph_canvas.create_text(20+d*13.3, 230, text="{}".format(d), font=('', 10))

    degree_graph_canvas.create_line(20, 235, 20, 5)
    degree_graph_canvas.create_text(45, 25, text='섭씨\n온도(℃)', font=('', 10))
    for i in range(1, 8):
        degree_graph_canvas.create_line(20, 220-(i*25), 25, 220-(i*25))
        degree_graph_canvas.create_text(10, 220-(i*25), text='{}'.format(i*5), font=('',10))


    #생산부하 그래프
    canvas.create_text(w-595, h-370, text='생산부하 그래프', font=('', 15, 'bold'))
    canvas.create_text(w-770, h-80, text='총 생산 냉방부하(RT) : ', font=('', 10), anchor='w')

    produced_graph_canvas = Canvas(canvas, width=360, height=240, bg='white', highlightbackground='black')
    produced_graph_canvas.place(x=w-770, y=h-350)

    produced_graph_canvas.create_line(5, 220, 355, 220)
    produced_graph_canvas.create_text(335, 210, text='시간(h)', font=('', 10))
    for i in range(25):
        produced_graph_canvas.create_line(20+i*13.3, 220, 20+i*13.3, 215)
        if i%3 == 2:
            d = i+1
            produced_graph_canvas.create_text(20+d*13.3, 230, text="{}".format(d), font=('', 10))

    produced_graph_canvas.create_line(20, 235, 20, 5)
    produced_graph_canvas.create_text(35, 10, text='RT', font=('', 10))
        
    #건물부하 그래프
    canvas.create_text(w-205, h-370, text='건물부하 그래프', font=('', 15, 'bold'))
    canvas.create_text(w-385, h-80, text='총 건물 냉방부하(RT) : ', font=('', 10), anchor='w')

    building_graph_canvas = Canvas(canvas, width=360, height=240, bg='white', highlightbackground='black')
    building_graph_canvas.place(x=w-385, y=h-350)

    building_graph_canvas.create_line(5, 220, 355, 220)
    building_graph_canvas.create_text(335, 210, text='시간(h)', font=('', 10))
    for i in range(25):
        building_graph_canvas.create_line(20+i*13.3, 220, 20+i*13.3, 215)
        if i%3 == 2:
            d = i+1
            building_graph_canvas.create_text(20+d*13.3, 230, text="{}".format(d), font=('', 10))

    building_graph_canvas.create_line(20, 235, 20, 5)
    building_graph_canvas.create_text(35, 10, text='RT', font=('', 10))
        
    #파이프
    supply_pipe = [p_x, p_y, 
                p_x+80, p_y, 
                p_x+80, p_y+280,

                (p_x+320, p_y+280), (p_x+320, p_y+185), (p_x+300, p_y+185), (p_x+300, p_y+165), (p_x+320, p_y+165), (p_x+320, p_y-10), (p_x+300, p_y-10), (p_x+300, p_y-30), (p_x+320, p_y-30), (p_x+320, p_y-205), (p_x+300, p_y-205), (p_x+300, p_y-225), (p_x+340, p_y-225), (p_x+340, p_y+280),
                (p_x+520, p_y+280), (p_x+520, p_y+185), (p_x+500, p_y+185), (p_x+500, p_y+165), (p_x+520, p_y+165), (p_x+520, p_y-10), (p_x+500, p_y-10), (p_x+500, p_y-30), (p_x+520, p_y-30), (p_x+520, p_y-205), (p_x+500, p_y-205), (p_x+500, p_y-225), (p_x+540, p_y-225), (p_x+540, p_y+280),
                (p_x+720, p_y+280), (p_x+720, p_y+185), (p_x+700, p_y+185), (p_x+700, p_y+165), (p_x+720, p_y+165), (p_x+720, p_y-10), (p_x+700, p_y-10), (p_x+700, p_y-30), (p_x+720, p_y-30), (p_x+720, p_y-205), (p_x+700, p_y-205), (p_x+700, p_y-225), (p_x+740, p_y-225), (p_x+740, p_y+280),
                (p_x+920, p_y+280), (p_x+920, p_y+185), (p_x+900, p_y+185), (p_x+900, p_y+165), (p_x+920, p_y+165), (p_x+920, p_y-10), (p_x+900, p_y-10), (p_x+900, p_y-30), (p_x+920, p_y-30), (p_x+920, p_y-205), (p_x+900, p_y-205), (p_x+900, p_y-225), (p_x+940, p_y-225), (p_x+940, p_y+280),
                (p_x+1120, p_y+280), (p_x+1120, p_y+185), (p_x+1100, p_y+185), (p_x+1100, p_y+165), (p_x+1120, p_y+165), (p_x+1120, p_y-10), (p_x+1100, p_y-10), (p_x+1100, p_y-30), (p_x+1120, p_y-30), (p_x+1120, p_y-205), (p_x+1100, p_y-205), (p_x+1100, p_y-225), (p_x+1140, p_y-225), (p_x+1140, p_y+280),

                p_x+1140, p_y+320,
                p_x+40, p_y+320,
                p_x+40, p_y+40,
                p_x, p_y+40]

    return_pipe = [p_x, p_y-40, 
                p_x+80, p_y-40, 
                p_x+80, p_y-320,

                (p_x+160, p_y-320), (p_x+160, p_y+185), (p_x+200, p_y+185), (p_x+200, p_y+165), (p_x+180, p_y+165), (p_x+180, p_y-10), (p_x+200, p_y-10), (p_x+200, p_y-30), (p_x+180, p_y-30), (p_x+180, p_y-205), (p_x+200, p_y-205), (p_x+200, p_y-225), (p_x+180, p_y-225), (p_x+180, p_y-320),
                (p_x+360, p_y-320), (p_x+360, p_y+185), (p_x+400, p_y+185), (p_x+400, p_y+165), (p_x+380, p_y+165), (p_x+380, p_y-10), (p_x+400, p_y-10), (p_x+400, p_y-30), (p_x+380, p_y-30), (p_x+380, p_y-205), (p_x+400, p_y-205), (p_x+400, p_y-225), (p_x+380, p_y-225), (p_x+380, p_y-320),
                (p_x+560, p_y-320), (p_x+560, p_y+185), (p_x+600, p_y+185), (p_x+600, p_y+165), (p_x+580, p_y+165), (p_x+580, p_y-10), (p_x+600, p_y-10), (p_x+600, p_y-30), (p_x+580, p_y-30), (p_x+580, p_y-205), (p_x+600, p_y-205), (p_x+600, p_y-225), (p_x+580, p_y-225), (p_x+580, p_y-320),
                (p_x+760, p_y-320), (p_x+760, p_y+185), (p_x+800, p_y+185), (p_x+800, p_y+165), (p_x+780, p_y+165), (p_x+780, p_y-10), (p_x+800, p_y-10), (p_x+800, p_y-30), (p_x+780, p_y-30), (p_x+780, p_y-205), (p_x+800, p_y-205), (p_x+800, p_y-225), (p_x+780, p_y-225), (p_x+780, p_y-320),
                (p_x+960, p_y-320), (p_x+960, p_y+185), (p_x+1000, p_y+185), (p_x+1000, p_y+165), (p_x+980, p_y+165), (p_x+980, p_y-10), (p_x+1000, p_y-10), (p_x+1000, p_y-30), (p_x+980, p_y-30), (p_x+980, p_y-205), (p_x+1000, p_y-205), (p_x+1000, p_y-225), (p_x+980, p_y-225), (p_x+980, p_y-320),

                p_x+980, p_y-360,
                p_x+40, p_y-360,
                p_x+40, p_y-80,
                p_x, p_y-80]

    #건물
    # canvas.create_rectangle(540, 250, 740, h-250, fill='gray')h=800
    canvas.create_rectangle(p_x+200, p_y-290, p_x+300, p_y-140, fill='#E0E0E0')
    canvas.create_rectangle(p_x+200, p_y-95, p_x+300, p_y+55, fill='#E0E0E0')
    canvas.create_rectangle(p_x+200, p_y+100, p_x+300, p_y+250, fill='#E0E0E0')

    canvas.create_rectangle(p_x+400, p_y-290, p_x+500, p_y-140, fill='#E0E0E0')
    canvas.create_rectangle(p_x+400, p_y-95, p_x+500, p_y+55, fill='#E0E0E0')
    canvas.create_rectangle(p_x+400, p_y+100, p_x+500, p_y+250, fill='#E0E0E0')

    canvas.create_rectangle(p_x+600, p_y-290, p_x+700, p_y-140, fill='#E0E0E0')
    canvas.create_rectangle(p_x+600, p_y-95, p_x+700, p_y+55, fill='#E0E0E0')
    canvas.create_rectangle(p_x+600, p_y+100, p_x+700, p_y+250, fill='#E0E0E0')

    canvas.create_rectangle(p_x+800, p_y-290, p_x+900, p_y-140, fill='#E0E0E0')
    canvas.create_rectangle(p_x+800, p_y-95, p_x+900, p_y+55, fill='#E0E0E0')
    canvas.create_rectangle(p_x+800, p_y+100, p_x+900, p_y+250, fill='#E0E0E0')

    canvas.create_rectangle(p_x+1000, p_y-290, p_x+1100, p_y-140, fill='#E0E0E0')
    canvas.create_rectangle(p_x+1000, p_y-95, p_x+1100, p_y+55, fill='#E0E0E0')
    canvas.create_rectangle(p_x+1000, p_y+100, p_x+1100, p_y+250, fill='#E0E0E0')


    dong = ['대학본부', '정보전산원', '자연대', '도서관', '공동실험실습관', '공대', '정보대', '인문대', '복지회관', '예체대', '학생복지회관', '컨벤션', '사회대법대', '동북아경영', '교수회관']
    for x in range(3):
        for i in range(5):
            canvas.create_text(p_x+250+i*200, p_y-215+x*195, text=dong[i+x*5], font=('', 10), anchor='center')
            for j in range(1, 5):
                canvas.create_line(p_x+200+i*200, p_y-290+x*195+j*30, p_x+300+i*200, p_y-290+x*195+j*30)

    #파이프
    supply_pipe = canvas.create_polygon(supply_pipe, fill='white', outline='blue', width=5)
    return_pipe = canvas.create_polygon(return_pipe, fill='white', outline='orange', width=5)

    canvas.create_text(p_x+510, p_y-340, text='환수 배관', font=("", 20), anchor='center')
    canvas.create_text(p_x+510, p_y+300, text='공급 배관', font=("", 20), anchor='center')

    
    #냉동기 이미지
    ref = Image.open('refrigerator2.png')
    ref600 = ref.resize((80, 50))
    ref600 = ImageTk.PhotoImage(ref600)
    ref475 = ref.resize((72, 45))
    ref475 = ImageTk.PhotoImage(ref475)
    ref180 = ref.resize((64, 40))
    ref180 = ImageTk.PhotoImage(ref180)
    #흡수식
    canvas.create_image(p_x-140, p_y-140, image=ref600)
    canvas.create_text(p_x-140, p_y-110, text='흡수식 1', font=('', 10), anchor='center')
    absortion1_b = canvas.create_rectangle((p_x-160, p_y-103), (p_x-120, p_y-88), fill='red', outline='black')
    absortion1 = canvas.create_text(p_x-140, p_y-95, text='OFF', font=('', 10, 'bold'), fill='white')

    canvas.create_image(p_x-140, p_y-60, image=ref600)
    canvas.create_text(p_x-140, p_y-30, text='흡수식 2', font=('', 10), anchor='center')
    absortion2_b = canvas.create_rectangle((p_x-160, p_y-23), (p_x-120, p_y-8), fill='red', outline='black')
    absortion2 = canvas.create_text(p_x-140, p_y-15, text='OFF', font=('', 10, 'bold'), fill='white')

    canvas.create_image(p_x-140, p_y+20, image=ref600)
    canvas.create_text(p_x-140, p_y+50, text='흡수식 3', font=('', 10), anchor='center')
    absortion3_b = canvas.create_rectangle((p_x-160, p_y+55), (p_x-120, p_y+72), fill='red', outline='black')
    absortion3 = canvas.create_text(p_x-140, p_y+65, text='OFF', font=('', 10, 'bold'), fill='white')

    canvas.create_image(p_x-140, p_y+100, image=ref600)
    canvas.create_text(p_x-140, p_y+130, text='흡수식 4', font=('', 10), anchor='center')
    absortion4_b = canvas.create_rectangle((p_x-160, p_y+137), (p_x-120, p_y+152), fill='red', outline='black')
    absortion4 = canvas.create_text(p_x-140, p_y+145, text='OFF', font=('', 10, 'bold'), fill='white')

    #터보식
    canvas.create_image(p_x-40, p_y-140, image=ref475)
    canvas.create_text(p_x-40, p_y-110, text='터보식 1', font=('', 10), anchor='center')
    turbor1_b = canvas.create_rectangle((p_x-60, p_y-103), (p_x-20, p_y-88), fill='red', outline='black')
    turbor1 = canvas.create_text(p_x-40, p_y-95, text='OFF', font=('', 10, 'bold'), fill='white')
    
    canvas.create_image(p_x-40, p_y-60, image=ref475)
    canvas.create_text(p_x-40, p_y-30, text='터보식 2', font=('', 10), anchor='center')
    turbor2_b = canvas.create_rectangle((p_x-60, p_y-23), (p_x-20, p_y-8), fill='red', outline='black')
    turbor2 = canvas.create_text(p_x-40, 405, text='OFF', font=('', 10, 'bold'), fill='white')

    canvas.create_image(p_x-40, p_y+20, image=ref180)
    canvas.create_text(p_x-40, p_y+50, text='터보식 3', font=('', 10), anchor='center')
    turbor3_b = canvas.create_rectangle((p_x-60, p_y+55), (p_x-20, p_y+72), fill='red', outline='black')
    turbor3 = canvas.create_text(p_x-40, 485, text='OFF', font=('', 10, 'bold'), fill='white')

    canvas.create_image(p_x-40, p_y+100, image=ref180)
    canvas.create_text(p_x-40, p_y+130, text='터보식 4', font=('', 10), anchor='center')
    turbor4_b = canvas.create_rectangle((p_x-60, p_y+137), (p_x-20, p_y+152), fill='red', outline='black')
    turbor4 = canvas.create_text(p_x-40, p_y+145, text='OFF', font=('', 10, 'bold'), fill='white')

    canvas.create_rectangle((p_x-183, p_y-170), (p_x, p_y+160), width=5)
    canvas.create_text(p_x-92, p_y-195, text='기계실', font=('', 15))

    image = Image.open("green_to_red.png").resize((20, 95))
    image = ImageTk.PhotoImage(image)

    canvas.create_text(110, 70, text='수온 색상 변화', font=("", 15) , anchor='center')
    canvas.create_image(110, 130, image=image, anchor='center')
    canvas.create_text(100, 90, text='17.0도', font=("", 10), anchor='e')
    canvas.create_text(100, 170, text='7.0도', font=("", 10), anchor='e')

    play_var = IntVar()
    x1 = Radiobutton(root, text='1배속', value=1, variable=play_var)
    x1.place(x=1450, y=20)
    x1.select()
    x3 = Radiobutton(root, text='3배속', value=3, variable=play_var)
    x3.place(x=1520, y=20)
    x5 = Radiobutton(root, text='5배속', value=5, variable=play_var)
    x5.place(x=1450, y=45)
    x10 = Radiobutton(root, text='10배속', value=10, variable=play_var)
    x10.place(x=1520, y=45)

    date_frame = Frame(root)
    date_frame.place(x=1160, y=30, anchor='center', height=60, width=300)
    
    text_ = Label(date_frame, text='날짜/시간', width=20, height=1)
    text_.pack(side='top')
    
    date_list_box = Listbox(date_frame, height=1, width=20)
    date_list_box.pack(side='top')

    scroll = Scrollbar(date_frame, orient='horizontal')
    scroll.pack(side='top', fill='both')

    open_button = Button(root, width=7, height=1, text='파일 열기', command = open_file)
    open_button.place(x=1380, y=45)

    read_button = Button(root, width=7, height=1, text='재생', command = lambda: play_file())
    read_button.place(x=1320, y=20)

    stop_button = Button(root, width=7, height=1, text='중지', command= stop_func)
    stop_button.place(x=1380, y=20)

    choice = Button(root, width=7, height=1, text='날짜 선택', command = lambda: get_date_list())
    choice.place(x=1320, y=45)

    bold = font.Font(size=10, weight="bold")
    norm = font.Font(size=10, weight='normal')
    
    canvas.mainloop()

def stop_func():
    global stop
    stop = False

def set_color(line):
    global degree, supply_degree, return_degree, rt, wf, produce_rt, building_rt, over_rt, under_rt, p_return, p_supply, graph_date
    global over_graph, produce_graph, building_graph, degree_graph

    total_rt = line[0]
    refs = list(map(int, eval(line[1])))
    entrophy = str(line[2])
    r_degree = round(float(line[3]), 2)
    s_degree = round(float(line[4]), 2)
    date = str(line[5]).split(' ')[0]
    time = str(line[5]).split(' ')[1].split(':')
    r_color = 'orange'
    s_color = 'orange'

    over_plots = []
    degree_plots = []
    produce_plots = []
    builidng_plots = []

    t = int(time[0])*4 + (int(time[1])//15) + 1

    if t == 1 or len(day_of_over[date]) != 96:
        over_plots.append([10, 120])
        degree_plots.append([20, 220])
        produce_plots.append([20, 220])
        builidng_plots.append([20, 220])

    for i in range(len(day_of_over[date])):
        
        over_plots.append([3.325*i+10, int(120+(day_of_over[date][i]/7))])
        produce_plots.append([3.325*i+20, 220-day_of_produce[date][i]/produce_max*200])
        builidng_plots.append([3.325*i+20, 220-day_of_building[date][i]/building_max*200])
        degree_plots.append([3.325*i+20, 220-day_of_degree[date][i]/35*175])    

    try:
        over_graph = supply_graph_canvas.create_line(over_plots[:min(t, 96)], fill='blue', width=2)
        produce_graph = produced_graph_canvas.create_line(produce_plots[:min(t, 96)], fill='blue', width=2)
        building_graph = building_graph_canvas.create_line(builidng_plots[:min(t, 96)], fill='blue', width=2)
        degree_graph = degree_graph_canvas.create_line(degree_plots[:min(t, 96)], fill='blue', width=2)
    except:
        over_graph = supply_graph_canvas.create_polygon(over_plots[:min(t, 96)], fill='blue', width=2)
        produce_graph = produced_graph_canvas.create_polygon(produce_plots[:min(t, 96)], fill='blue', width=2)
        building_graph = building_graph_canvas.create_polygon(builidng_plots[:min(t, 96)], fill='blue', width=2)
        degree_graph = degree_graph_canvas.create_polygon(degree_plots[:min(t, 96)], fill='blue', width=2)

    if r_degree-round(r_degree) > 0:
        round_rd = max(round(r_degree)-0.5, 7)
    else:
        round_rd = round(r_degree)
    
    if s_degree-round(s_degree) > 0:
        round_sd = max(round(s_degree)-0.5, 7)
    else:
        round_sd = round(s_degree)

    if round_rd >= 17.5:
        r_color = '#'+degree_color[17.5]
    else:
        r_color = '#'+degree_color[round_rd]
    
    if round_sd >= 17.5:
        s_color = '#'+degree_color[17.5]
    else:
        s_color = '#'+degree_color[round_sd]

    produced = 0

    if refs[0] == 1:
        canvas.itemconfig(turbor1, text='ON')
        canvas.itemconfig(turbor1_b, fill='#009900')
        produced += 475
    elif refs[0] == 0:
        canvas.itemconfig(turbor1, text='OFF')
        canvas.itemconfig(turbor1_b, fill='red')

    if refs[1] == 1:
        canvas.itemconfig(turbor2, text='ON')
        canvas.itemconfig(turbor2_b, fill='#009900')
        produced += 475
    elif refs[1] == 0:
        canvas.itemconfig(turbor2, text='OFF')
        canvas.itemconfig(turbor2_b, fill='red')

    if refs[2] == 1:
        canvas.itemconfig(turbor3, text='ON')
        canvas.itemconfig(turbor3_b, fill='#009900')
        produced += 180
    elif refs[2] == 0:
        canvas.itemconfig(turbor3, text='OFF')
        canvas.itemconfig(turbor3_b, fill='red')

    if refs[3] == 1:
        canvas.itemconfig(turbor4, text='ON')
        canvas.itemconfig(turbor4_b, fill='#009900')
        produced += 180
    elif refs[3] == 0:
        canvas.itemconfig(turbor4, text='OFF')
        canvas.itemconfig(turbor4_b, fill='red')

    if refs[4] == 1:
        canvas.itemconfig(absortion1, text='ON')
        canvas.itemconfig(absortion1_b, fill='#009900')
        produced += 600
    elif refs[4] == 0:
        canvas.itemconfig(absortion1, text='OFF')
        canvas.itemconfig(absortion1_b, fill='red')

    if refs[5] == 1:
        canvas.itemconfig(absortion2, text='ON')
        canvas.itemconfig(absortion2_b, fill='#009900')
        produced += 600
    elif refs[5] == 0:
        canvas.itemconfig(absortion2, text='OFF')
        canvas.itemconfig(absortion2_b, fill='red')

    if refs[6] == 1:
        canvas.itemconfig(absortion3, text='ON')
        canvas.itemconfig(absortion3_b, fill='#009900')
        produced += 600
    elif refs[6] == 0:
        canvas.itemconfig(absortion3, text='OFF')
        canvas.itemconfig(absortion3_b, fill='red')

    if refs[7] == 1:
        canvas.itemconfig(absortion4, text='ON')
        canvas.itemconfig(absortion4_b, fill='#009900')
        produced += 600
    elif refs[7] == 0:
        canvas.itemconfig(absortion4, text='OFF')
        canvas.itemconfig(absortion4_b, fill='red')

    if produced>=total_rt:
        over = round(produced-total_rt,2)
        under = 0.0
    else:
        over = 0.0
        under = round(total_rt-produced,2)
    
    graph_date = canvas.create_text(w-400, h-750, text='날짜 : '+date, font=('', 12, 'bold'))
    degree = canvas.create_text(w-700, h-430, text=str(entrophy)+'도', font=('', 10), anchor='w')
    produce_rt = canvas.create_text(w-620, h-80, text=str(produced)+'RT', font=('', 10), anchor='w')
    
    building_rt = canvas.create_text(w-235, h-80, text=str(total_rt)+'RT', font=('', 10), anchor='w')
    over_rt = canvas.create_text(w-245, h-430, text=str(over)+'RT', font=('', 10), anchor='w')
    under_rt = canvas.create_text(w-245, h-410, text=str(under)+'RT', font=('', 10), anchor='w')

    p_return = canvas.create_text(w-380, h-50, text='환수 온도 : '+str(r_degree)+'도', font=('', 10, 'bold'))
    p_supply = canvas.create_text(w-380, h-30, text='공급 온도 : '+str(s_degree)+'도', font=('', 10, 'bold'))

    supply_degree = []
    return_degree = []
    rt = []
    wf = []
    for i in range(3):
        for j in range(5):
            sd = canvas.create_text(p_x+250+j*200, p_y-275+i*195, text=str(s_degree)+'도', font=('', 10), anchor='center')
            rd = canvas.create_text(p_x+250+j*200, p_y-245+i*195, text=str(r_degree)+'도', font=('', 10), anchor='center')
            r = canvas.create_text(p_x+250+j*200, p_y-185+i*195, text=str(total_rt)+'RT', font=('', 10), anchor='center')
            watter = canvas.create_text(p_x+250+j*200, p_y-155+i*195, text='유량 (예정)', font=('', 10), anchor='center')
            supply_degree.append(sd)
            return_degree.append(rd)
            rt.append(r)
            wf.append(watter)

    canvas.itemconfig(supply_pipe, fill=s_color)
    canvas.itemconfig(return_pipe, fill=r_color)
    
    root.update()  

def open_file():
    global df
    global filename
    global datetime
    global index
    global day_of_over, day_of_degree, day_of_building, day_of_produce
    global produce_max, building_max, produce_list, building_list

    filetypes = (
        ('csv files', '*.csv'),
        ('excel files', '*.xlsx'),
        ('all files', '*.*')
    )
    try:
        filename = filedialog.askopenfilename(
            title='파일 선택',
            initialdir='/',
            filetypes=filetypes)

        if 'csv' in filename:
            df = pd.read_csv(filename)
        elif 'xlsx' in filename:
            df = pd.read_excel(filename)
        
        datetime = df['date'].tolist()
        total_rt = df['total_rt'].tolist()
        cover_rt = df['operation'].tolist()
        degree_list = df['air_temp'].tolist()

        for i in range(len(cover_rt)):
            r = 0
            cover_ = list(map(int, eval(cover_rt[i])))
            if cover_[0] == 1:
                r += 475
            if cover_[1] == 1:
                r += 475
            if cover_[2] == 1:
                r += 180
            if cover_[3] == 1:
                r += 180
            if 1 in cover_[4:]:
                r+= 600*cover_[4:].count(1)
            cover_rt[i] = r
        
        day_of_over = {}
        day_of_degree = {}
        day_of_produce = {}
        day_of_building = {}
        
        for i in range(len(datetime)):
            d = datetime[i].split(' ')[0]
            if d not in day_of_over:
                day_of_over[d] = [round(total_rt[i]-cover_rt[i], 2)]
            else:
                day_of_over[d].append(round(total_rt[i]-cover_rt[i], 2))

            if d not in day_of_produce:
                day_of_produce[d] = [cover_rt[i]]
            else:
                day_of_produce[d].append(cover_rt[i])

            if d not in day_of_building:
                day_of_building[d] = [round(total_rt[i], 2)]
            else:
                day_of_building[d].append(round(total_rt[i], 2))

            if d not in day_of_degree:
                day_of_degree[d] = [degree_list[i]]
            else:
                day_of_degree[d].append(degree_list[i])

        produce_max = max(cover_rt)
        building_max = round(max(total_rt), 2)

        for i in range(len(datetime)):
            d = datetime[i].split(' ')

        try:
            for p, b in zip(produce_list, building_list):
                produced_graph_canvas.delete(p)
                building_graph_canvas.delete(b)
        except: pass

        produce_list = []
        building_list = []

        for i in range(1, 11):
            p = produced_graph_canvas.create_text(20, 220-i*20, text=str((max(cover_rt)/10)*i), font=('',7))
            b = building_graph_canvas.create_text(20, 220-i*20, text=str(round((max(total_rt)/10)*i, 2)), font=('',7))
            produce_list.append(p)
            building_list.append(b)

        try:
            date_list_box.delete(0, END)
        except:
            pass

        for d in datetime:
            date_list_box.insert('end', d)

        date_list_box.config(yscrollcommand=scroll.set)
        scroll.config(command=custom_command)
        index = 0

    except:
        messagebox.showwarning("파일 불러오기 오류", "파일을 불러올 수 없습니다.")

def play_file():  
    global df 
    global date_list_box
    global stop
    global index
    try:          
        df_list = df.to_numpy().tolist()
        stop=True
        while stop:
            date_list_box.see(max(date_list_box.nearest(0), index))
            try:
                supply_graph_canvas.delete(over_graph)
                produced_graph_canvas.delete(produce_graph)
                building_graph_canvas.delete(building_graph)
                degree_graph_canvas.delete(degree_graph)
            except:pass
            try:
                canvas.delete(degree, produce_rt, building_rt, over_rt, under_rt, p_return, p_supply, graph_date)
                for s,r,t,w in zip(supply_degree, return_degree, rt, wf):
                    canvas.delete(s,r,t,w)
            except:pass
            set_color(df_list[max(date_list_box.nearest(0), index)])
            index+=1
            if index == date_list_box.size():
                break
            time.sleep(0.3/play_var.get())
    
    except tkinter.TclError:
        pass

    except:
        messagebox.showwarning("파일 불러오기 오류", "파일을 먼저 선택해 주세요.")              
            
def select_date(date_index):
    global select, index

    index = date_index[0]
    date_list_box.see(index)
    select = df.loc[index].tolist()
    try:
        supply_graph_canvas.delete(over_graph)
        produced_graph_canvas.delete(produce_graph)
        building_graph_canvas.delete(building_graph)
        degree_graph_canvas.delete(degree_graph)
    except:pass
    try:
        canvas.delete(degree, produce_rt, building_rt, over_rt, under_rt, p_return, p_supply, graph_date)
        for s,r,t,w in zip(supply_degree, return_degree, rt, wf):
            canvas.delete(s,r,t,w)
    except:
        pass     

    set_color(select)
    
def get_date_list():   
    try:
        height = min(18*len(datetime)+70, 600)

        new_window = Toplevel(root)
        new_window.title("Select date")
        new_window.iconbitmap('inu.ico')
        new_window.resizable(False, False)
        new_window.geometry('270x{}'.format(str(height)))
        text = Label(new_window, text='날짜')
        text.place(x=34, y=10)

        frame = Frame(new_window)
        frame.place(x=10, y=30, width=200, height=height-70)

        list_ = Listbox(frame, height=200, width=20)
        list_.pack(side='top')
        list_.bind('<Double-1>', lambda event: select_date(list_.curselection()))

        scb = Scrollbar(new_window, orient='vertical')
        scb.config(command=list_.yview)
        scb.pack(side='right', fill='y')  

        select_date_button = Button(new_window, width=7, height=1, text='가져오기', command=lambda: select_date(list_.curselection()))
        select_date_button.place(x=245, y=30, anchor='ne')
        list_.config(yscrollcommand=scb.set)
        for d in datetime:
            list_.insert('end', d)

    except NameError:
        messagebox.showwarning("파일 불러오기 오류", "파일을 먼저 선택해 주세요.")

def custom_command(*args):
    global select
    global index

    date_list_box.yview(*args)
    index = date_list_box.nearest(0)
    select = df.loc[index].tolist()
    try:
        supply_graph_canvas.delete(over_graph)
        produced_graph_canvas.delete(produce_graph)
        building_graph_canvas.delete(building_graph)
        degree_graph_canvas.delete(degree_graph)
    except:pass
    try:
        canvas.delete(degree, produce_rt, building_rt, over_rt, under_rt, p_return, p_supply, graph_date)
        for s,r,t,w in zip(supply_degree, return_degree, rt, wf):
            canvas.delete(s,r,t,w)
    except:
        pass      
    set_color(select)

if __name__ == '__main__':
    main()