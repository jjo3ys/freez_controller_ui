import time
import math
import os

from tkinter import font
from tkinter.ttk import Progressbar
import pandas as pd
import tkinter

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

from Simulator import Main

wf = [3986.28, 1209.48, 848.66, 1259.43, 1531.40,
      863.21, 1151.27, 102.52, 435.12, 935.72,
      2013.41, 1212.51, 211.61, 481.76, 593.70]


degree_color = {7:'000fff', 7.5:'004fff', 8:'008fff', 8.5:'00bfff', 9:'00dfff', 9.5:'00ffff', 10:'00ffdf', 10.5:'00ffbf', 11:'00ff8f', 11.5:'00ff4f', 12:'00ff0f', 12.5:'4fff00', 13:'8fff00', 13.5:'bfff00', 14:'dfff00', 14.5:'ffff00', 15:'ffbf00', 15.5:'ffdf00', 16:'ffbf00', 16.5:'ff8f00', 17:'ff4f00', 17.5:'ff0000', 18:'df0000', 19:'8f0000', 20:'4f0000'}

p_x = 210
p_y = 420
window_x = 1480
window_y = 925

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

class ResizingCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        self.config(width=self.width, height=self.height)
        self.scale("all", 0, 0, wscale, hscale)

def main():
    global canvas, root, supply_graph_canvas, degree_graph_canvas, produced_graph_canvas, building_graph_canvas, electric_graph_canvas, acc_graph_canvas, norm, bold
    global date_list_box, scroll, play_var, load_button, simul_button, read_button, choice, stop_button
    global absortion1, absortion2, absortion3, absortion4, absortion1_b, absortion2_b, absortion3_b, absortion4_b
    global ref_list
    global return_pipe, supply_pipe
    global w, h
    global return_list, supply_list, building_rt_list, p_supply, p_return

    root = Tk()

    window_x = root.winfo_screenwidth()
    window_y = root.winfo_screenheight()-200

    root.title("Energy ui")
    root.resizable(True, True)
    root.iconbitmap('inu.ico')
    root.geometry('{}x{}+{}+{}'.format(int(window_x/3*2), int(window_y), 50, 50))
    # root.config(bg='#4E4E4E')
        
    w = 1375
    h = 800
    
    bold = font.Font(size=10, weight="bold")
    norm = font.Font(size=10, weight='normal')
    
    Label(root).pack()

    frame1 = Frame(root)
    frame1.pack(fill='x')

    frame4 = Frame(frame1)
    frame4.pack(side='right')

    Label(frame4, text='Industrial Inteligence Lab', font=('', 15, 'bold'), foreground='#000000').pack(side='top', anchor='ne', padx=25)#00B3FF
    Label(frame4, text='designed by Yeon-Seong Jo', font=('', 8)).pack(side='top', anchor='ne', padx=25)

    Label(frame1, width=5).pack(side='right')

    frame3 = Frame(frame1)
    frame3.pack(side='right')
    frame3_1 = Frame(frame3)
    frame3_1.pack(fill='x')
    frame3_2 = Frame(frame3)
    frame3_2.pack(fill='x')
    
    play_var = IntVar()
    x1 = Radiobutton(frame3_1, text='Speed X1', value=1, variable=play_var)
    x1.pack(side='left', anchor='w')
    
    x1.select()
    x3 = Radiobutton(frame3_1, text='Speed X3', value=3, variable=play_var)
    x3.pack(side='left', anchor='w')
    
    x5 = Radiobutton(frame3_2, text='Speed X5', value=5, variable=play_var)
    x5.pack(side='left', anchor='w')
    
    x10 = Radiobutton(frame3_2, text='Speed X10', value=10, variable=play_var)
    x10.pack(side='left', anchor='w')
    
    Label(frame1, width=5).pack(side='right')

    frame2 = Frame(frame1)
    frame2.pack(side='right')
    frame2_1 = Frame(frame2)
    frame2_1.pack()
    frame2_2 = Frame(frame2)
    frame2_2.pack()
    frame2_3 = Frame(frame2)
    frame2_3.pack()
    
    read_button = Button(frame2_1, width=7, height=1, text='Play', command = play_file)
    read_button.pack(side='left')

    stop_button = Button(frame2_2, width=7, height=1, text='Stop', command= stop_func)
    stop_button.pack(side='left')

    choice = Button(frame2_3, width=7, height=1, text='Date', command = get_date_list)
    choice.pack(side='left')

    Label(frame1, width=5).pack(side='right')

    date_frame = Frame(frame1)
    date_frame.pack(side='right')
    text_ = Label(date_frame, text='Date / Time', width=20, height=1)
    text_.pack(side='top')
    
    date_list_box = Listbox(date_frame, height=1, width=20)
    date_list_box.pack(side='top')

    scroll = Scrollbar(date_frame, orient='horizontal')
    scroll.pack(side='top', fill='both')

    Label(frame1, width=5).pack(side='right', fill='x')

    #model load
    model_frame = Frame(frame1)
    model_frame.pack(side='right')
    simul_button = Button(model_frame, width=10, height=1, text='SIMULATION', command = simulation)
    simul_button.pack()

    Label(model_frame, height=1).pack()

    load_button = Button(model_frame, width=7, height=1, text='LOAD', command = load_file)
    load_button.pack()
    
    if not len(os.listdir()):
        simul_button['state'] = DISABLED

    canvas = ResizingCanvas(root, width=w, height=h, bg="white", highlightbackground='black')
    canvas.pack(side='bottom', anchor='center',fill=BOTH, expand=YES, padx='25', pady='25')

    graph_window = Toplevel(root)
    graph_window.title("Graphs")
    graph_window.iconbitmap('inu.ico')
    graph_window.resizable(False, False)
    graph_window.geometry('820x860+{}+{}'.format(int(window_x/3*2+70), 50))

    graph_canvas = Canvas(graph_window, width=780, height=820, bg='white', highlightbackground='black')
    graph_canvas.place(x=410, y=430, anchor='center')
    #저, 과공급 그래프
    graph_canvas.create_text(200, 15, text='저·과 공급 그래프', font=('', 12, 'bold'))

    supply_graph_canvas = Canvas(graph_canvas, width=360, height=240, bg="white", highlightbackground='black')
    supply_graph_canvas.place(x=20, y=30)

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

    #누적 과저공급 그래프
    graph_canvas.create_text(580, 15, text='누적 과저공급 그래프', font=('', 12, 'bold'))

    acc_graph_canvas = Canvas(graph_canvas, width=360, height=240, bg='white', highlightbackground='black')
    acc_graph_canvas.place(x=400, y=30)

    acc_graph_canvas.create_line(5, 220, 355, 220)
    acc_graph_canvas.create_text(335, 210, text='시간(h)', font=('', 10))
    for i in range(25):
        acc_graph_canvas.create_line(20+i*13.3, 220, 20+i*13.3, 215)
        if i%3 == 2:
            d = i+1
            acc_graph_canvas.create_text(20+d*13.3, 230, text="{}".format(d), font=('', 10))

    acc_graph_canvas.create_line(20, 235, 20, 5)
    acc_graph_canvas.create_text(35, 10, text='RT', font=('', 10))

    #생산부하 그래프
    graph_canvas.create_text(200, 285, text='생산부하 그래프', font=('', 12, 'bold'))

    produced_graph_canvas = Canvas(graph_canvas, width=360, height=240, bg='white', highlightbackground='black')
    produced_graph_canvas.place(x=20, y=300)

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
    graph_canvas.create_text(580, 285, text='건물부하 그래프', font=('', 12, 'bold'))

    building_graph_canvas = Canvas(graph_canvas, width=360, height=240, bg='white', highlightbackground='black')
    building_graph_canvas.place(x=400, y=300)
    
    building_graph_canvas.create_line(5, 220, 355, 220)
    building_graph_canvas.create_text(335, 210, text='시간(h)', font=('', 10))
    for i in range(25):
        building_graph_canvas.create_line(20+i*13.3, 220, 20+i*13.3, 215)
        if i%3 == 2:
            d = i+1
            building_graph_canvas.create_text(20+d*13.3, 230, text="{}".format(d), font=('', 10))

    building_graph_canvas.create_line(20, 235, 20, 5)
    building_graph_canvas.create_text(35, 10, text='RT', font=('', 10))

    #전력 사용량 그래프
    graph_canvas.create_text(200, 555, text='누적 전력 사용량 그래프', font=('', 12, 'bold'))

    electric_graph_canvas = Canvas(graph_canvas, width=360, height=240, bg='white', highlightbackground='black')
    electric_graph_canvas.place(x=20, y=570)

    electric_graph_canvas.create_line(5, 220, 355, 220)
    electric_graph_canvas.create_text(335, 210, text='시간(h)', font=('', 10))
    for i in range(25):
        electric_graph_canvas.create_line(20+i*13.3, 220, 20+i*13.3, 215)
        if i%3 == 2:
            d = i+1
            electric_graph_canvas.create_text(20+d*13.3, 230, text="{}".format(d), font=('', 10))
    
    electric_graph_canvas.create_line(20, 235, 20, 5)
    electric_graph_canvas.create_text(40, 10, text='KW/h', font=('', 10))#1KW=860Kcal, 1 RT = 3,024 Kcal/h 1 RT = 3.51628 KW/h

    #외기온도 그래프
    graph_canvas.create_text(580, 555, text='외기온도 그래프', font=('', 12, 'bold'))

    degree_graph_canvas = Canvas(graph_canvas, width=360, height=240, bg='white', highlightbackground='black')
    degree_graph_canvas.place(x=400, y=570)

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
        
    #파이프
    supply_pipe = canvas.create_polygon(supply_pipe, fill='white', outline='blue', width=5)
    return_pipe = canvas.create_polygon(return_pipe, fill='white', outline='orange', width=5)
    p_return = canvas.create_text(p_x+520, p_y-340, text='Return Degree : ℃', font=('', 12, 'bold'), anchor='w')
    p_supply = canvas.create_text(p_x+520, p_y+300, text='Supply Degree : ℃', font=('', 12, 'bold'), anchor='w')

    #건물
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

    #건물 예시
    canvas.create_text(p_x-100, p_y+185, text='건물 데이터 각주', font=('', 10, 'bold'))
    canvas.create_rectangle(p_x-150, p_y+350, p_x-50, p_y+200, fill='#E0E0E0')
    canvas.create_text(p_x-100, p_y+320+15, text='유량', font=('', 10, 'bold'), anchor='center')
    canvas.create_line(p_x-150, p_y+320, p_x-50, p_y+320)
    canvas.create_text(p_x-100, p_y+290+15, text='건물 부하', font=('', 10, 'bold'), anchor='center')
    canvas.create_line(p_x-150, p_y+290, p_x-50, p_y+290)
    canvas.create_text(p_x-100, p_y+260+15, text='건물 이름', font=('', 10, 'bold'), anchor='center')
    canvas.create_line(p_x-150, p_y+260, p_x-50, p_y+260)
    canvas.create_text(p_x-100, p_y+230+15, text='환수 온도', font=('', 10, 'bold'), anchor='center')
    canvas.create_line(p_x-150, p_y+230, p_x-50, p_y+230)
    canvas.create_text(p_x-100, p_y+200+15, text='공급 온도', font=('', 10, 'bold'), anchor='center')

    dong = ['공과대학', '공동실험실습관', '교수회관', '대학본부', '도서관', '동북아경제통상', '복지회관', '사회법과대학', '예체능대학', '인문대학', '자연대학', '정보기술대학', '정보전산원', '컨벤션센터', '학생복지회관']

    supply_list = []
    return_list = []
    building_rt_list = []

    for x in range(3):
        for i in range(5):
            s = canvas.create_text(p_x+250+i*200, p_y-275+x*195, text='', font=('', 10), anchor='center')
            r = canvas.create_text(p_x+250+i*200, p_y-245+x*195, text='', font=('', 10), anchor='center')
            b = canvas.create_text(p_x+250+i*200, p_y-185+x*195, text='', font=('', 10), anchor='center')           
            canvas.create_text(p_x+250+i*200, p_y-215+x*195, text=dong[i+x*5], font=('', 10), anchor='center')
            canvas.create_text(p_x+250+i*200, p_y-155+x*195, text=str(wf[i+x*5])+' L/m', font=('', 10), anchor='center')

            supply_list.append(s)
            return_list.append(r)
            building_rt_list.append(b)

            for j in range(1, 5):
                canvas.create_line(p_x+200+i*200, p_y-290+x*195+j*30, p_x+300+i*200, p_y-290+x*195+j*30)

    #냉동기 이미지
    ref = Image.open('refrigerator2.png')
    ref600 = ref.resize((80, 50))
    ref600 = ImageTk.PhotoImage(ref600)
    ref475 = ref.resize((72, 45))
    ref475 = ImageTk.PhotoImage(ref475)
    ref180 = ref.resize((64, 40))
    ref180 = ImageTk.PhotoImage(ref180)

    ref_list = []
    #Turbor
    canvas.create_image(p_x-40, p_y-140, image=ref475)
    canvas.create_text(p_x-40, p_y-110, text='Turbor 1', font=('', 10), anchor='center')
    turbor1_b = canvas.create_rectangle((p_x-60, p_y-103), (p_x-20, p_y-88), fill='red', outline='black')
    turbor1 = canvas.create_text(p_x-40, p_y-95, text='OFF', font=('', 10, 'bold'), fill='white')
    ref_list.append([turbor1, turbor1_b])

    canvas.create_image(p_x-40, p_y-60, image=ref475)
    canvas.create_text(p_x-40, p_y-30, text='Turbor 2', font=('', 10), anchor='center')
    turbor2_b = canvas.create_rectangle((p_x-60, p_y-23), (p_x-20, p_y-8), fill='red', outline='black')
    turbor2 = canvas.create_text(p_x-40, 405, text='OFF', font=('', 10, 'bold'), fill='white')
    ref_list.append([turbor2, turbor2_b])

    canvas.create_image(p_x-40, p_y+20, image=ref180)
    canvas.create_text(p_x-40, p_y+50, text='Turbor 3', font=('', 10), anchor='center')
    turbor3_b = canvas.create_rectangle((p_x-60, p_y+55), (p_x-20, p_y+72), fill='red', outline='black')
    turbor3 = canvas.create_text(p_x-40, 485, text='OFF', font=('', 10, 'bold'), fill='white')
    ref_list.append([turbor3, turbor3_b])

    canvas.create_image(p_x-40, p_y+100, image=ref180)
    canvas.create_text(p_x-40, p_y+130, text='Turbor 4', font=('', 10), anchor='center')
    turbor4_b = canvas.create_rectangle((p_x-60, p_y+137), (p_x-20, p_y+152), fill='red', outline='black')
    turbor4 = canvas.create_text(p_x-40, p_y+145, text='OFF', font=('', 10, 'bold'), fill='white')
    ref_list.append([turbor4, turbor4_b])

    #Abosrtion
    canvas.create_image(p_x-140, p_y-140, image=ref600)
    canvas.create_text(p_x-140, p_y-110, text='Abosrtion 1', font=('', 10), anchor='center')
    absortion1_b = canvas.create_rectangle((p_x-160, p_y-103), (p_x-120, p_y-88), fill='red', outline='black')
    absortion1 = canvas.create_text(p_x-140, p_y-95, text='OFF', font=('', 10, 'bold'), fill='white')
    ref_list.append([absortion1, absortion1_b])

    canvas.create_image(p_x-140, p_y-60, image=ref600)
    canvas.create_text(p_x-140, p_y-30, text='Abosrtion 2', font=('', 10), anchor='center')
    absortion2_b = canvas.create_rectangle((p_x-160, p_y-23), (p_x-120, p_y-8), fill='red', outline='black')
    absortion2 = canvas.create_text(p_x-140, p_y-15, text='OFF', font=('', 10, 'bold'), fill='white')
    ref_list.append([absortion2, absortion2_b])

    canvas.create_image(p_x-140, p_y+20, image=ref600)
    canvas.create_text(p_x-140, p_y+50, text='Abosrtion 3', font=('', 10), anchor='center')
    absortion3_b = canvas.create_rectangle((p_x-160, p_y+55), (p_x-120, p_y+72), fill='red', outline='black')
    absortion3 = canvas.create_text(p_x-140, p_y+65, text='OFF', font=('', 10, 'bold'), fill='white')
    ref_list.append([absortion3, absortion3_b])

    canvas.create_image(p_x-140, p_y+100, image=ref600)
    canvas.create_text(p_x-140, p_y+130, text='Abosrtion 4', font=('', 10), anchor='center')
    absortion4_b = canvas.create_rectangle((p_x-160, p_y+137), (p_x-120, p_y+152), fill='red', outline='black')
    absortion4 = canvas.create_text(p_x-140, p_y+145, text='OFF', font=('', 10, 'bold'), fill='white')
    ref_list.append([absortion4, absortion4_b])

    canvas.create_rectangle((p_x-183, p_y-170), (p_x, p_y+160), width=5)
    canvas.create_text(p_x-92, p_y-195, text='Cooling System', font=('', 15, 'bold'))

    image = Image.open("green_to_red.png").resize((20, 95))
    image = ImageTk.PhotoImage(image)

    canvas.create_text(110, 55, text='Temperature\nColor change', font=("", 15) , anchor='center')
    canvas.create_image(110, 130, image=image, anchor='center')
    canvas.create_text(100, 90, text='17.0 ℃', font=("", 10), anchor='e')
    canvas.create_text(100, 170, text='7.0 ℃', font=("", 10), anchor='e')
    
    canvas.mainloop()

def stop_func():
    global stop
    stop = False

def set_data(line):
    global p_return, p_supply
    global building_graph, degree_graph, electric_graph, acc_graph

    pick = model_select.get()
    model = model_list[pick]

    refs = list(map(int, eval(line[3])))
    r_degree = round(float(line[4]), 2)
    s_degree = round(float(line[5]), 2)
    date = str(line[0]).split(' ')[0]
    time = str(line[0]).split(' ')[1].split(':')

    buildings_rt = line[9].split(', ')
    buildings_supply = list(map(float, line[10].split(', ')))
    buildings_return = list(map(float, line[11].split(', ')))

    r_color = 'orange'
    s_color = 'orange'

    t = int(time[0])*4 + (int(time[1])//15)

    degree_plots = [20, 220-day_of_degree[model][date][0]/35*175]
    builidng_plots = [20, 220]

    for i in range(t+1):
        try:
            builidng_plots += [3.325*i+20, 220-day_of_building[model][date][i]/building_max*200]
            degree_plots += [3.325*i+20, 220-day_of_degree[model][date][i]/35*175]
            
        except:
            pass


    building_graph_canvas.coords(building_graph, builidng_plots)
    degree_graph_canvas.coords(degree_graph, degree_plots)
    

    for m in model_list:
        over_plots = [10, 120]    
        acc_plots = [20, 220]   
        produce_plots = [20, 220]
        electric_plots = [20, 220]
        for i in range(t+1):
            try:
                over_plots += [3.325*i+10, 120+day_of_over[m][date][i]/supply_max*100]
                acc_plots += [3.325*i+10, 220-sum(day_of_acc[m][date][:i])/acc_max*200]
                produce_plots += [3.325*i+20, 220-day_of_produce[m][date][i]/produce_max*200]
                electric_plots += [3.325*i+20, 220-sum(day_of_produce[m][date][:i])*3.51628/electric_max*200]
            except:
                pass
        
        acc_graph_canvas.coords(df_dict[m]['acc_graph'], acc_plots)
        supply_graph_canvas.coords(df_dict[m]['over_graph'], over_plots)
        produced_graph_canvas.coords(df_dict[m]['produce_graph'], produce_plots)
        electric_graph_canvas.coords(df_dict[m]['electric_graph'], electric_plots)
    
    # try:
    #     abs_over = abs(day_of_over[model][date][t])
    #     if abs_over == 0:
    #         x = 110
    #         y = 0
    #     elif abs_over > 0 and abs_over <=100:
    #         x = abs(math.cos(18)*110)
    #         y = -abs(math.sin(18)*110)
        
    #     elif abs_over > 100 and abs_over <=200:
    #         x = abs(math.cos(54)*110)
    #         y = -abs(math.sin(54)*110)
        
    #     elif abs_over > 200 and abs_over <=300:
    #         x = 0
    #         y = -110
        
    #     elif abs_over > 300 and abs_over <= 400:
    #         x = -abs(math.cos(126)*110)
    #         y = -abs(math.sin(126)*110)
        
    #     elif abs_over > 400 and abs_over <= 500:
    #         x = -abs(math.cos(162)*110)
    #         y = -abs(math.sin(162)*110)
        
    #     else:
    #         x=-110
    #         y=0
    #     coordinate = [180, 210, 180+x, 210+y]

    #     acc_graph_canvas.coords(arrow, coordinate)
    # except:
    #     pass

    if r_degree>=18:
        round_rd = round(r_degree)
    elif r_degree-round(r_degree) > 0:
        round_rd = max(round(r_degree)+0.5, 7)
    else:
        round_rd = round(r_degree)
    
    if s_degree>=18:
        round_sd = round(s_degree)
    elif s_degree-round(s_degree) > 0:
        round_sd = max(round(s_degree)+0.5, 7)
    else:
        round_sd = round(s_degree)

    if round_rd >= 20:
        r_color = '#'+degree_color[20]
    else:
        r_color = '#'+degree_color[round_rd]
    
    if round_sd >= 20:
        s_color = '#'+degree_color[20]
    else:
        s_color = '#'+degree_color[round_sd]

    for i in range(6):
        if refs[i] == 1:
            canvas.itemconfig(ref_list[i][0], text='ON')
            canvas.itemconfig(ref_list[i][1], fill='#009900')
        else:
            canvas.itemconfig(ref_list[i][0], text='OFF')
            canvas.itemconfig(ref_list[i][1], fill='red')
   
    canvas.itemconfig(p_return, text='환수 온도 : '+str(r_degree)+'도')
    canvas.itemconfig(p_supply, text='공급 온도 : '+str(s_degree)+'도')

    for i in range(3):
        for j in range(5):
            s = supply_list[i*5+j]
            r = return_list[i*5+j]
            b = building_rt_list[i*5+j]

            canvas.itemconfig(s, text=str(round(buildings_supply[i*5+j],2))+' 도')
            canvas.itemconfig(r, text=str(round(buildings_return[i*5+j],2))+' 도')
            canvas.itemconfig(b, text=buildings_rt[i*5+j]+' RT')

    canvas.itemconfig(supply_pipe, fill=s_color)
    canvas.itemconfig(return_pipe, fill=r_color)
    
    root.update()  

def pick_model():
    pick = model_select.get()
    model = model_list[pick]
    df = df_dict[model]['data']
    select = df.loc[index].tolist()
    set_data(select)

def disable_event():
    pass

def simulation():
    model = Main()
    progress_wd = Toplevel(root)
    progress_wd.title("Simulating...")
    progress_wd.iconbitmap('inu.ico')
    progress_wd.resizable(False, False)
    progress_wd.geometry('300x100+{}+{}'.format(int(root.winfo_width()/2), int(root.winfo_height()/2)))
    progress_wd.protocol("WM_DELETE_WINDOW", disable_event)


    p_var = DoubleVar()
    pg_bar = Progressbar(progress_wd, maximum=100, length=250, variable=p_var)
    pg_bar.place(x=150, y=50, anchor='center')

    load_button['state'] = DISABLED
    simul_button['state'] = DISABLED
    read_button['state'] = DISABLED
    stop_button['state'] = DISABLED
    choice['state'] = DISABLED

    simul = 'Simulating'
    txt = StringVar()
    txt.set(simul)

    pg_txt = Label(progress_wd, textvariable=txt, anchor='center')
    pg_txt.place(x=150, y=25, anchor='center')
    id = 0
    for process in model.run():
        # print(process)
        p_var.set(process+1)
        pg_bar.update()
        txt.set(simul+'.'*int((id//100)%3+1))
        id += 1

    progress_wd.destroy()
    load_button['state'] = ACTIVE
    simul_button['state'] = ACTIVE
    read_button['state'] = ACTIVE
    stop_button['state'] = ACTIVE
    choice['state'] = ACTIVE
    load_file()

def load_file():
    global df, df_dict
    global model_select, model_list, radio_bt_list
    global datetime
    global index
    global day_of_over, day_of_acc, day_of_degree, day_of_building, day_of_produce
    global building_max, supply_max, produce_max, electric_max, acc_max
    global building_graph, electric_graph, degree_graph, over_graph, acc_graph
    global produce_list, building_list, electric_list, over_supply_list, acc_list

    try:
        try:
            for p, b, e in zip(produce_list, building_list, electric_list):
                produced_graph_canvas.delete(p)
                building_graph_canvas.delete(b)
                electric_graph_canvas.delete(e)        
        except: pass

        try:          
            for o, a in zip(over_supply_list, acc_list):
                supply_graph_canvas.delete(o)
                acc_graph_canvas.delete(a)
        except: pass

        try:
            for radioBt in radio_bt_list:
                canvas.delete(radioBt)
        except:
            pass

        try:
            supply_graph_canvas.delete(over_graph)
            degree_graph_canvas.delete(degree_graph)
            produced_graph_canvas.delete(produce_graph)
            building_graph_canvas.delete(building_graph)
            electric_graph_canvas.delete(electric_graph)
            acc_graph_canvas.delete(acc_graph)
        except:pass

        model_list = Main.model_list
        model_select = IntVar()
        df_dict = {}
        radio_bt_list = []
        day_of_over = {}#
        day_of_acc = {}
        day_of_degree = {}#
        day_of_produce = {}#
        day_of_building = {}#
        colors = ['blue', 'red']
        building_max, supply_max, produce_max, electric_max, acc_max = 0, 0, 0, 0, 0

        for id, model in enumerate(model_list):
            df_dict[model] = {}
            day_of_over[model] = {}
            day_of_acc[model] = {}
            day_of_degree[model] = {}
            day_of_produce[model] = {}
            day_of_building[model] = {}

            df = pd.read_csv("./simul_result/{}_result.csv".format(model))
            df_dict[model]['data']=df
            model_button = Radiobutton(canvas, text=model, value=id, variable=model_select, command=pick_model)
            model_button.place(x=2, y=id*25+2)
            model_button.configure(background='white')
            radio_bt_list.append(model_button)

            datetime = df['date'].tolist()
            total_rt = df['total_rt'].tolist()
            cover_rt = df['operation'].tolist()
            degree_list = df['air_temp'].tolist()
            first_date = datetime[0].split(" ")[0]
            for i in range(len(cover_rt)):
                cover_ = list(map(int, eval(cover_rt[i])))
                r = cover_[0:2].count(1)*475 + cover_[2:4].count(1)*180 + cover_[4:].count(1)*600

                cover_rt[i] = r
            for i in range(len(datetime)):
                d = datetime[i].split(' ')[0]
                if d not in day_of_over[model]:
                    day_of_over[model][d] = [round(total_rt[i]-cover_rt[i], 2)]
                else:
                    day_of_over[model][d].append(round(total_rt[i]-cover_rt[i], 2))
                
                if d not in day_of_acc[model]:
                    day_of_acc[model][d] = [abs(round(total_rt[i]-cover_rt[i], 2))]
                else:
                    day_of_acc[model][d].append(abs(round(total_rt[i]-cover_rt[i], 2)))

                if d not in day_of_produce[model]:
                    day_of_produce[model][d] = [cover_rt[i]]
                else:
                    day_of_produce[model][d].append(cover_rt[i])

                if d not in day_of_building[model]:
                    day_of_building[model][d] = [round(total_rt[i], 2)]
                else:
                    day_of_building[model][d].append(round(total_rt[i], 2))

                if d not in day_of_degree[model]:
                    day_of_degree[model][d] = [degree_list[i]]
                else:
                    day_of_degree[model][d].append(degree_list[i])
            
            min_list = []
            max_list = []
            abs_list = []
            electric_max_list = []
            for d in day_of_over[model]:
                min_list.append(min(day_of_over[model][d]))
                max_list.append(max(day_of_over[model][d]))
                abs_list.append(sum(day_of_acc[model][d]))
                electric_max_list.append(sum(day_of_produce[model][d]))
            
            electric_max = max(round(max(electric_max_list)*3.51628), electric_max)#
            acc_max = max(round(max(abs_list), 2), acc_max)
            produce_max = max(max(cover_rt), produce_max)#
            building_max = max(round(max(total_rt), 2), building_max)#
            supply_max = max(max(abs(min(min_list)), max(max_list)), supply_max)#

            del min_list, max_list, electric_max_list, abs_list

            over_plots = [10, 120]
            over_plots += over_plots
            acc_plots = [20, 220]
            acc_plots += acc_plots
            produce_plots = [20, 220]
            produce_plots += produce_plots
            electric_plots = [20, 220]
            electric_plots += electric_plots
        
            
            over_graph = supply_graph_canvas.create_line(over_plots, fill=colors[id], width=3-id)
            acc_graph = acc_graph_canvas.create_line(acc_plots, fill=colors[id], width=3-id)
            produce_graph = produced_graph_canvas.create_line(produce_plots, fill=colors[id], width=3-id)
            electric_graph = electric_graph_canvas.create_line(electric_plots, fill=colors[id], width=3-id)

            acc_graph_canvas.create_rectangle(280, 15*id+5, 290, 15*(id+1), fill=colors[id])
            supply_graph_canvas.create_rectangle(280, 15*id+5, 290, 15*(id+1), fill=colors[id])
            produced_graph_canvas.create_rectangle(280, 15*id+5, 290, 15*(id+1), fill=colors[id])
            electric_graph_canvas.create_rectangle(280, 15*id+5, 290, 15*(id+1), fill=colors[id])

            acc_graph_canvas.create_text(300, 15*id+5, text=model, font=('', 7), anchor='nw')
            supply_graph_canvas.create_text(300, 15*id+5, text=model, font=('', 7), anchor='nw')
            produced_graph_canvas.create_text(300, 15*id+5, text=model, font=('', 7), anchor='nw')
            electric_graph_canvas.create_text(300, 15*id+5, text=model, font=('', 7), anchor='nw')


            df_dict[model]['over_graph'] = over_graph
            df_dict[model]['acc_graph'] = acc_graph
            df_dict[model]['produce_graph'] = produce_graph
            df_dict[model]['electric_graph'] = electric_graph

        acc_list = []
        produce_list = []
        building_list = []
        electric_list = []
        over_supply_list = []

        for i in range(1, 11):
            a = acc_graph_canvas.create_text(20, 220-i*20, text=str(round((acc_max/10)*i, 2)), font=('', 7))
            p = produced_graph_canvas.create_text(20, 220-i*20, text=str((produce_max/10)*i), font=('',7))
            e = electric_graph_canvas.create_text(20, 220-i*20, text=str(round(electric_max/10)*i), font=('',7))#1KW=860Kcal, 1 RT = 3,024 Kcal/h 1 RT = 3.51628 KW/h
            b = building_graph_canvas.create_text(20, 220-i*20, text=str(round((max(total_rt)/10)*i, 2)), font=('',7))
            acc_list.append(a)
            produce_list.append(p)
            electric_list.append(e)
            building_list.append(b)
        
        for i in range(11):
            o = supply_graph_canvas.create_text(20, 220-i*20, text=str(round(-supply_max + supply_max/5*i, 2)), font=('', 7))
            over_supply_list.append(o)

        degree_plots = [20, 220-day_of_degree[model][first_date][0]/35*175]
        degree_plots += degree_plots
        builidng_plots = [20, 220]
        builidng_plots += builidng_plots
        

        building_graph = building_graph_canvas.create_line(builidng_plots, fill='gray', width=2)
        degree_graph = degree_graph_canvas.create_line(degree_plots, fill='gray', width=2)
        

        index = 0
        pick = model_select.get()
        model = model_list[pick]
        df = df_dict[model]['data']

        df_list = df.to_numpy().tolist()

        try:
            date_list_box.delete(0, END)
        except:
            pass

        for d in datetime:
            date_list_box.insert('end', d)

        date_list_box.config(yscrollcommand=scroll.set)
        scroll.config(command=custom_command)
        set_data(df_list[max(date_list_box.nearest(0), index)])
            
    except:
        messagebox.showwarning('Load 오류', '파일을 불러올 수 없습니다.\nsimulation 버튼을 클릭해 주세요.')
        load_button['state'] = DISABLED
   
def play_file():  
    global df_dict 
    global date_list_box
    global stop
    global index
    try:     
        pick = model_select.get()
        model = model_list[pick]
        df = df_dict[model]['data']     
        df_list = df.to_numpy().tolist()
        stop=True
        while stop:
            date_list_box.see(max(date_list_box.nearest(0), index))
            set_data(df_list[max(date_list_box.nearest(0), index)])
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
    pick = model_select.get()
    model = model_list[pick]
    df = df_dict[model]['data']
    select = df.loc[index].tolist()
    set_data(select)
    
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
    pick = model_select.get()
    model = model_list[pick]
    df = df_dict[model]['data']
    select = df.loc[index].tolist()     
    set_data(select)

if __name__ == '__main__':
    main()