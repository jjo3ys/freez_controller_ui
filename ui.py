import time
import pandas as pd
import tkinter

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

degree_color ={ 7: '00FF00', 7.5:'15FF00', 8:'30FF00', 8.5:'45FF00', 9:'60FF00', 9.5:'75FF00', 10:'90FF00', 10.5:'AAFF00', 11:'BBFF00', 11.5:'CCFF00', 12:'DDFF00', 12.5:'EEFF00', 13:'FFFF00', 13.5:'FFEE00', 14:'FFDD00', 14.5:'FFCC00', 15:'FFBB00', 15.5:'FFAA00', 16:'FF9000', 16.5:'FF6000', 17:'FF3000', 17.5:'FF0000'}

def main():
    global canvas, root, graph_canvas
    global date_list_box, scroll
    global absortion1, absortion2, absortion3, absortion4
    global turbor1, turbor2, turbor3, turbor4
    global return_pipe, supply_pipe

    w = 1800
    h = 800

    root = Tk()
    root.title("Energy ui")
    root.resizable(False, False)
    root.iconbitmap('inu.ico')
    root.geometry('1900x950')

    canvas = Canvas(root, width=w, height=h, bg="white", highlightbackground='black')
    canvas.place(x=50, y=75)

    graph_canvas = Canvas(canvas, width=360, height=240, bg="white", highlightbackground='black')
    graph_canvas.place(x=1400, y=40)

    graph_canvas.create_line(10, 5, 10, 235)
    graph_canvas.create_text(23, 10, text='RT', font=('', 10))
    graph_canvas.create_line(10, 120, 355, 120)
    graph_canvas.create_text(345, 130, text='날짜', font=('', 10))

    graph_canvas.create_text(180, 60, text='과공급', fill='gray', font=('', 15))
    graph_canvas.create_text(180, 180, text='저공급', fill='gray', font=('', 15))

    supply_pipe = [190, 420, 
                270, 420, 
                270, 700,

                (510, 700), (510, 605), (490, 605), (490, 585), (510, 585), (510, 410), (490, 410), (490, 390), (510, 390), (510, 215), (490, 215), (490, 195), (530, 195), (530, 700),
                (710, 700), (710, 605), (690, 605), (690, 585), (710, 585), (710, 410), (690, 410), (690, 390), (710, 390), (710, 215), (690, 215), (690, 195), (730, 195), (730, 700),
                (910, 700), (910, 605), (890, 605), (890, 585), (910, 585), (910, 410), (890, 410), (890, 390), (910, 390), (910, 215), (890, 215), (890, 195), (930, 195), (930, 700),
                (1110, 700), (1110, 605), (1090, 605), (1090, 585), (1110, 585), (1110, 410), (1090, 410), (1090, 390), (1110, 390), (1110, 215), (1090, 215), (1090, 195), (1130, 195), (1130, 700),
                (1310, 700), (1310, 605), (1290, 605), (1290, 585), (1310, 585), (1310, 410), (1290, 410), (1290, 390), (1310, 390), (1310, 215), (1290, 215), (1290, 195), (1330, 195), (1330, 700),

                1330, 740,
                230, 740,
                230, 460,
                190, 460]

    return_pipe = [190, 380, 
                270, 380, 
                270, 100,

                (350, 100), (350, 605), (390, 605), (390, 585), (370, 585), (370, 410), (390, 410), (390, 390), (370, 390), (370, 215), (390, 215), (390, 195), (370, 195), (370, 100),
                (550, 100), (550, 605), (590, 605), (590, 585), (570, 585), (570, 410), (590, 410), (590, 390), (570, 390), (570, 215), (590, 215), (590, 195), (570, 195), (570, 100),
                (750, 100), (750, 605), (790, 605), (790, 585), (770, 585), (770, 410), (790, 410), (790, 390), (770, 390), (770, 215), (790, 215), (790, 195), (770, 195), (770, 100),
                (950, 100), (950, 605), (990, 605), (990, 585), (970, 585), (970, 410), (990, 410), (990, 390), (970, 390), (970, 215), (990, 215), (990, 195), (970, 195), (970, 100),
                (1150, 100), (1150, 605), (1190, 605), (1190, 585), (1170, 585), (1170, 410), (1190, 410), (1190, 390), (1170, 390), (1170, 215), (1190, 215), (1190, 195), (1170, 195), (1170, 100),

                1170, 60,
                230, 60,
                230, 340,
                190, 340]

    #건물
    # canvas.create_rectangle(540, 250, 740, h-250, fill='gray')h=800
    canvas.create_rectangle(390, 130, 490, 280, fill='#E0E0E0')
    canvas.create_rectangle(390, 325, 490, 475, fill='#E0E0E0')
    canvas.create_rectangle(390, 520, 490, 670, fill='#E0E0E0')

    canvas.create_rectangle(590, 130, 690, 280, fill='#E0E0E0')
    canvas.create_rectangle(590, 325, 690, 475, fill='#E0E0E0')
    canvas.create_rectangle(590, 520, 690, 670, fill='#E0E0E0')

    canvas.create_rectangle(790, 130, 890, 280, fill='#E0E0E0')
    canvas.create_rectangle(790, 325, 890, 475, fill='#E0E0E0')
    canvas.create_rectangle(790, 520, 890, 670, fill='#E0E0E0')

    canvas.create_rectangle(990, 130, 1090, 280, fill='#E0E0E0')
    canvas.create_rectangle(990, 325, 1090, 475, fill='#E0E0E0')
    canvas.create_rectangle(990, 520, 1090, 670, fill='#E0E0E0')

    canvas.create_rectangle(1190, 130, 1290, 280, fill='#E0E0E0')
    canvas.create_rectangle(1190, 325, 1290, 475, fill='#E0E0E0')
    canvas.create_rectangle(1190, 520, 1290, 670, fill='#E0E0E0')
    dong = ['대학본부', '정보전산원', '자연대', '도서관', '공동실험실습관', '공대', '정보대', '인문대', '복지회관', '예체대', '학생복지회관', '컨벤션', '사회대법대', '동북아경영', '교수회관']
    for x in range(3):
        for i in range(5):
            canvas.create_text(440+i*200, 205+x*195, text=dong[i+x*5], font=('', 10), anchor='center')
            for j in range(1, 5):
                canvas.create_line(390+i*200, 130+x*195+j*30, 490+i*200, 130+x*195+j*30)

    #파이프
    supply_pipe = canvas.create_polygon(supply_pipe, fill='white', outline='blue', width=5)
    return_pipe = canvas.create_polygon(return_pipe, fill='white', outline='orange', width=5)

    canvas.create_text(700, 80, text='환수 파이프', font=("", 20), anchor='center')
    canvas.create_text(700, 720, text='공급 파이프', font=("", 20), anchor='center')

    # #펌프
    # canvas.create_polygon([220, 495, 280, 525, 280, 495, 220, 525], fill='blue', outline='black')
    # canvas.create_text(350, 510, text='1차 펌프', font=("", 20), anchor='center')

    # canvas.create_polygon([610, h-200, 670, h-170, 670, h-200, 610, h-170], fill='blue', outline='black')
    # canvas.create_polygon([910, h-200, 970, h-170, 970, h-200, 910, h-170], fill='blue', outline='black')
    # canvas.create_polygon([1310, h-200, 1370, h-170, 1370, h-200, 1310, h-170], fill='blue', outline='black')
    # canvas.create_text(790, h-185, text='2차 펌프', font=("", 15), anchor='center')
    
    #텍스트
    # energy_img = Image.open("energy_img.png").resize((150,150))
    # energy_img = ImageTk.PhotoImage(energy_img)
    # canvas.create_image(110, 120, image=energy_img, anchor='center')
    ref = Image.open('refrigerator2.png')
    ref600 = ref.resize((80, 50))
    ref600 = ImageTk.PhotoImage(ref600)
    ref475 = ref.resize((72, 45))
    ref475 = ImageTk.PhotoImage(ref475)
    ref180 = ref.resize((64, 40))
    ref180 = ImageTk.PhotoImage(ref180)

    canvas.create_image(50, 280, image=ref600)
    canvas.create_text(50, 310, text='흡수식 1', font=('', 10), anchor='center')
    absortion1 = canvas.create_text(50, 325, text='OFF', font=('', 10))

    canvas.create_image(50, 360, image=ref600)
    canvas.create_text(50, 390, text='흡수식 2', font=('', 10), anchor='center')
    absortion2 = canvas.create_text(50, 405, text='OFF', font=('', 10))

    canvas.create_image(50, 440, image=ref600)
    canvas.create_text(50, 470, text='흡수식 3', font=('', 10), anchor='center')
    absortion3 = canvas.create_text(50, 485, text='OFF', font=('', 10))

    canvas.create_image(50, 520, image=ref600)
    canvas.create_text(50, 550, text='흡수식 4', font=('', 10), anchor='center')
    absortion4 = canvas.create_text(50, 565, text='OFF', font=('', 10))

    canvas.create_image(150, 280, image=ref475)
    canvas.create_text(150, 310, text='터보식 1', font=('', 10), anchor='center')
    turbor1 = canvas.create_text(150, 325, text='OFF', font=('', 10))

    canvas.create_image(150, 360, image=ref475)
    canvas.create_text(150, 390, text='터보식 2', font=('', 10), anchor='center')
    turbor2 = canvas.create_text(150, 405, text='OFF', font=('', 10))

    canvas.create_image(150, 440, image=ref180)
    canvas.create_text(150, 470, text='터보식 3', font=('', 10), anchor='center')
    turbor3 = canvas.create_text(150, 485, text='OFF', font=('', 10))

    canvas.create_image(150, 520, image=ref180)
    canvas.create_text(150, 550, text='터보식 4', font=('', 10), anchor='center')
    turbor4 = canvas.create_text(150, 565, text='OFF', font=('', 10))

    canvas.create_rectangle((7, 255), (190, 575), width=5)
    canvas.create_text(98, 235, text='기계실', font=('', 15))

    image = Image.open("green_to_red.png").resize((20, 95))
    image = ImageTk.PhotoImage(image)

    canvas.create_text(110, 70, text='수온 색상 변화', font=("", 10) , anchor='center')
    canvas.create_image(110, 130, image=image, anchor='center')
    canvas.create_text(100, 90, text='17.0도', font=("", 7), anchor='e')
    canvas.create_text(100, 170, text='7.0도', font=("", 7), anchor='e')

    canvas.create_text(1530, 350, text='외기온도 :', font=('', 10))
    canvas.create_text(1530, 380, text='생산부하 :', font=('', 10))
    canvas.create_text(1530, 410, text='건물부하 :', font=('', 10))
    canvas.create_text(1525, 440, text='과공급부하 :', font=('', 10))
    canvas.create_text(1525, 470, text='저공급부하 :', font=('', 10))
    canvas.create_text(1515, 500, text='기계실환수온도 :', font=('', 10))
    canvas.create_text(1515, 530, text='기계실공급온도 :', font=('', 10))

    date_frame = Frame(root)
    date_frame.place(x=750, y=30, anchor='center', height=60, width=300)
    
    text_ = Label(date_frame, text='날짜/시간', width=20, height=1)
    text_.pack(side='top')
    
    date_list_box = Listbox(date_frame, height=1, width=20)
    date_list_box.pack(side='top')

    scroll = Scrollbar(date_frame, orient='horizontal')
    scroll.pack(side='top', fill='both')

    open_button = Button(root, width=7, height=1, text='파일 열기', command = open_file)
    open_button.place(x=970, y=45)

    read_button = Button(root, width=7, height=1, text='재생', command = lambda: play_file())
    read_button.place(x=910, y=20)

    stop_button = Button(root, width=7, height=1, text='중지', command= stop_func)
    stop_button.place(x=970, y=20)

    choice = Button(root, width=7, height=1, text='날짜 선택', command = lambda: get_date_list())
    choice.place(x=910, y=45)
    
    canvas.mainloop()

def stop_func():
    global stop
    stop = False

def set_color(line):
    global degree, supply_degree, return_degree, rt, wf, produce_rt, building_rt, over_rt, under_rt, p_return, p_supply

    total_rt = line[0]
    refs = list(map(int, eval(line[1])))
    entrophy = str(line[2])
    r_degree = round(float(line[3]), 2)
    p_return_degree = round(float(line[3]), 2)
    date = str(line[4])
    color = 'orange'

    # alpha = ['A', 'B', 'C', 'D', 'E', 'F']
    # integer = [i for i in range(10)]

    if r_degree-round(r_degree) > 0:
        round_d = round(r_degree)
    else:
        round_d = round(r_degree)

    if round_d >= 17.5:
        color = '#'+degree_color[16]
    else:
        color = '#'+degree_color[round_d]
    # if r_degree >=7 and r_degree <=11:
    #     color = "#00FF00"
    
    # elif r_degree >11 and r_degree <=15:
    #     color = "#FFFF00"
    
    # elif r_degree > 15:
    #     color = "#FF0000"
    produced = 0

    if refs[0] == 1:
        canvas.itemconfig(turbor1, text='ON', fill='#19EB35')
        produced += 475
    elif refs[0] == 0:
        canvas.itemconfig(turbor1, text='OFF', fill='black')

    if refs[1] == 1:
        canvas.itemconfig(turbor2, text='ON', fill='#19EB35')
        produced += 475
    elif refs[1] == 0:
        canvas.itemconfig(turbor2, text='OFF', fill='black')

    if refs[2] == 1:
        canvas.itemconfig(turbor3, text='ON', fill='#19EB35')
        produced += 180
    elif refs[2] == 0:
        canvas.itemconfig(turbor3, text='OFF', fill='black')

    if refs[3] == 1:
        canvas.itemconfig(turbor4, text='ON', fill='#19EB35')
        produced += 180
    elif refs[3] == 0:
        canvas.itemconfig(turbor4, text='OFF', fill='black')

    if refs[4] == 1:
        canvas.itemconfig(absortion1, text='ON', fill='#19EB35')
        produced += 600
    elif refs[4] == 0:
        canvas.itemconfig(absortion1, text='OFF', fill='black')

    if refs[5] == 1:
        canvas.itemconfig(absortion2, text='ON', fill='#19EB35')
        produced += 600
    elif refs[5] == 0:
        canvas.itemconfig(absortion2, text='OFF', fill='black')

    if refs[6] == 1:
        canvas.itemconfig(absortion3, text='ON', fill='#19EB35')
        produced += 600
    elif refs[6] == 0:
        canvas.itemconfig(absortion3, text='OFF', fill='black')

    if refs[7] == 1:
        canvas.itemconfig(absortion4, text='ON', fill='#19EB35')
        produced += 600
    elif refs[7] == 0:
        canvas.itemconfig(absortion4, text='OFF', fill='black')

    if produced>=total_rt:
        over = round(produced-total_rt,2)
        under = 0.0
    else:
        over = 0.0
        under = round(total_rt-produced,2)
    
    # date_time = canvas.create_text(90, 30, text=date, font=('', 10), anchor='w')
    degree = canvas.create_text(1600, 350, text=str(entrophy)+'도', font=('', 10))
    produce_rt = canvas.create_text(1600, 380, text=str(produced)+'RT', font=('', 10))
    building_rt = canvas.create_text(1600, 410, text=str(total_rt)+'RT', font=('', 10))
    over_rt = canvas.create_text(1600, 440, text=str(over)+'RT', font=('', 10))
    under_rt = canvas.create_text(1600, 470, text=str(under)+'RT', font=('', 10))
    p_return = canvas.create_text(1600, 500, text=str(p_return_degree)+'도', font=('', 10))
    p_supply = canvas.create_text(1600, 530, text='7.0도', font=('', 10))

    supply_degree = []
    return_degree = []
    rt = []
    wf = []
    for i in range(3):
        for j in range(5):
            sd = canvas.create_text(440+j*200, 145+i*195, text='7.0도', font=('', 10), anchor='center')
            rd = canvas.create_text(440+j*200, 175+i*195, text=str(r_degree)+'도', font=('', 10), anchor='center')
            r = canvas.create_text(440+j*200, 235+i*195, text=str(total_rt)+'RT', font=('', 10), anchor='center')
            w = canvas.create_text(440+j*200, 265+i*195, text='유량 (예정)', font=('', 10), anchor='center')
            supply_degree.append(sd)
            return_degree.append(rd)
            rt.append(r)
            wf.append(w)
    # supply_degree = canvas.create_text(90, 70, text='7.0도', font=('', 10), anchor='w')
    # return_degree = canvas.create_text(90, 90, text=str(return_degree)+'도', font=('', 10), anchor='w')
    # rt = canvas.create_text(105, 110, text=total_rt+'RT', font=('', 10), anchor='w')

    canvas.itemconfig(supply_pipe, fill='#00ff00')
    canvas.itemconfig(return_pipe, fill=color)
    
    root.update()  

def open_file():
    global df
    global filename
    global date
    global index
    global under_list, over_list

    filetypes = (
        ('csv files', '*.csv'),
        ('excel files', '*.xlsx'),
        ('All files', '*.*')
    )
    try:
        file = filedialog.askopenfilename(
            title='파일 선택',
            initialdir='/',
            filetypes=filetypes)

        filename = file
        if 'csv' in filename:
            df = pd.read_csv(filename)
        elif 'xlsx' in filename:
            df = pd.read_excel(filename)
        date = df['date'].tolist()

        under_list = [0 for i in range(len(date))]
        over_list = [0 for i in range(len(date))]

        try:
            date_list_box.delete(0, END)
        except:
            pass

        for d in date:
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
                canvas.delete(degree, produce_rt, building_rt, over_rt, under_rt, p_return, p_supply)
                for s,r,t,w in zip(supply_degree, return_degree, rt, wf):
                    canvas.delete(s,r,t,w)
            except:
                pass
            set_color(df_list[max(date_list_box.nearest(0), index)])
            index+=1
            if index == date_list_box.size():
                break
            time.sleep(0.5)
    
    except tkinter.TclError:
        pass

    except:
        messagebox.showwarning("파일 불러오기 오류", "파일을 먼저 선택해 주세요.")              
            
def select_date(date_index):
    global select

    date_list_box.see(date_index)
    select = df.loc[date_index].tolist()
    try:
        canvas.delete(degree, produce_rt, building_rt, over_rt, under_rt, p_return, p_supply)
        for s,r,t,w in zip(supply_degree, return_degree, rt, wf):
            canvas.delete(s,r,t,w)
    except:
        pass     

    set_color(select)
    
def get_date_list():   
    try:
        height = min(18*len(date)+70, 600)

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
        for d in date:
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
        canvas.delete(degree, produce_rt, building_rt, over_rt, under_rt, p_return, p_supply)
        for s,r,t,w in zip(supply_degree, return_degree, rt, wf):
            canvas.delete(s,r,t,w)
    except:
        pass      
    set_color(select)

if __name__ == '__main__':
    main()