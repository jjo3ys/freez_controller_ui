import time
import pandas as pd

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

def main():
    global canvas, root
    global date_list_box, scroll
    global absortion1, absortion2, absortion3, absortion4
    global turbor1, turbor2, turbor3, turbor4
    global return_pipe, supply_pipe

    w = 1500
    h = 800

    root = Tk()
    root.title("Energy ui")
    root.resizable(False, False)
    root.iconbitmap('inu.ico')
    root.geometry('1600x950')

    canvas = Canvas(root, width=w, height=h, bg="white", highlightbackground='black')
    canvas.place(x=50, y=75)

    supply_pipe = [190, h/2+20, 
                270, h/2+20, 
                270, h-100,
                620, h-100,
                620, h-250,
                660, h-250,
                660, h-100,
                920, h-100,
                920, h-250,
                960, h-250,
                960, h-100,
                1320, h-100,
                1320, h-250,
                1360, h-250,
                1360, h-60,

                230, h-60,
                230, h/2+60,
                190, h/2+60]

    return_pipe = [190, h/2-20, 
                270, h/2-20, 
                270, 100,
                620, 100,
                620, 250,
                660, 250,
                660, 100,
                920, 100,
                920, 250,
                960, 250,
                960, 100,
                1320, 100,
                1320, 250,
                1360, 250,
                1360, 60,
                230, 60,
                230, h/2-60,
                190, h/2-60]

    #냉동기
    canvas.create_rectangle(30, 340, 190, 460, fill='#0099ff')
    canvas.create_text(115, 400, text="냉동기", font=('', 20))

    #터보식 냉동기
    canvas.create_text(110, 260, text='터보식', font=('', 10))
    turbor1 = canvas.create_rectangle(35, 290, 65, 320, fill='#AEAEAE')#475
    canvas.create_text(50, 305, text='1', font=('', 10))
    turbor2 = canvas.create_rectangle(75, 290, 105, 320, fill='#AEAEAE')#475
    canvas.create_text(90, 305, text='2', font=('', 10))
    turbor3 = canvas.create_rectangle(115, 290, 145, 320, fill='#AEAEAE')#180
    canvas.create_text(130, 305, text='3', font=('', 10))
    turbor4 = canvas.create_rectangle(155, 290, 185, 320, fill='#AEAEAE')#180
    canvas.create_text(170, 305, text='4', font=('', 10))

    canvas.create_rectangle(45, 320, 55, 340, fill='#AEAEAE')
    canvas.create_rectangle(85, 320, 95, 340, fill='#AEAEAE')
    canvas.create_rectangle(125, 320, 135, 340, fill='#AEAEAE')
    canvas.create_rectangle(165, 320, 175, 340, fill='#AEAEAE')

    #흡수식 냉동기
    canvas.create_text(110, 540, text='흡수식', font=('', 10))
    absortion1 = canvas.create_rectangle(35, 510, 65, 480, fill='gray')#600
    canvas.create_text(50, 495, text='1', font=('', 10))
    absortion2 = canvas.create_rectangle(75, 510, 105, 480, fill='gray')#600
    canvas.create_text(90, 495, text='2', font=('', 10))
    absortion3 = canvas.create_rectangle(115, 510, 145, 480, fill='gray')#600
    canvas.create_text(130, 495, text='3', font=('', 10))
    absortion4 = canvas.create_rectangle(155, 510, 185, 480, fill='gray')#600
    canvas.create_text(170, 495, text='4', font=('', 10))

    canvas.create_rectangle(45, 480, 55, 460, fill='gray')
    canvas.create_rectangle(85, 480, 95, 460, fill='gray')
    canvas.create_rectangle(125, 480, 135, 460, fill='gray')
    canvas.create_rectangle(165, 480, 175, 460, fill='gray')

    #건물
    canvas.create_rectangle(540, 250, 740, h-250, fill='gray')
    canvas.create_text(640, h/2, text='건물1', font=('', 20), anchor='center')

    canvas.create_rectangle(840, 250, 1040, h-250, fill='gray')
    canvas.create_text(940, h/2, text='건물2', font=('', 20), anchor='center')

    canvas.create_text(1140, h/2, text='. . .', font=('', 40), anchor='center')

    canvas.create_rectangle(1240, 250, 1440, h-250, fill='gray')
    canvas.create_text(1340, h/2, text='건물N', font=('', 20), anchor='center')

    #파이프
    supply_pipe = canvas.create_polygon(supply_pipe, fill='white', outline='black')
    return_pipe = canvas.create_polygon(return_pipe, fill='white', outline='black')

    canvas.create_text(790, 80, text='환수 파이프', font=("", 20), anchor='center')
    canvas.create_text(790, 720, text='공급 파이프', font=("", 20), anchor='center')

    #펌프
    canvas.create_polygon([220, 495, 280, 525, 280, 495, 220, 525], fill='blue', outline='black')
    canvas.create_text(350, 510, text='1차 펌프', font=("", 20), anchor='center')

    canvas.create_polygon([610, h-200, 670, h-170, 670, h-200, 610, h-170], fill='blue', outline='black')
    canvas.create_polygon([910, h-200, 970, h-170, 970, h-200, 910, h-170], fill='blue', outline='black')
    canvas.create_polygon([1310, h-200, 1370, h-170, 1370, h-200, 1310, h-170], fill='blue', outline='black')
    canvas.create_text(790, h-185, text='2차 펌프', font=("", 15), anchor='center')

    canvas.create_text(85, 30, text='날짜/시간 :', font=('', 10), anchor='e')
    canvas.create_text(85, 50, text='외기 온도 :', font=('', 10), anchor='e')
    canvas.create_text(85, 70, text='공급 온도 :', font=('', 10), anchor='e')
    canvas.create_text(85, 90, text='환수 온도 :', font=('', 10), anchor='e')
    canvas.create_text(5, 110, text='건물 냉방 부하 :', font=('', 10), anchor='w')

    image = Image.open("green_to_red.png").resize((20, 95))
    image = ImageTk.PhotoImage(image)

    canvas.create_text(1420, 20, anchor='w', text='환수 온도 색상 변화', font=("", 7))
    canvas.create_image(1470, 30, anchor='nw',image=image)
    canvas.create_text(1440, 35, anchor='w', text='17.0도', font=("", 7))
    canvas.create_text(1440, 118, anchor='w', text='12.0도', font=("", 7))

    date_frame = Frame(root)
    date_frame.place(x=750, y=30, anchor='center', height=60, width=300)
    
    text_ = Label(date_frame, text='날짜/시간', width=20, height=1)
    text_.pack(side='top')
    
    date_list_box = Listbox(date_frame, height=1, width=20)
    date_list_box.pack(side='top')

    scroll = Scrollbar(date_frame, orient='horizontal')
    scroll.pack(side='top', fill='both')

    open_button = Button(root, width=7, height=1, text='파일 열기', command = open_file)
    open_button.place(x=50, y=15)

    read_button = Button(root, width=7, height=1, text='재생', command = lambda: read_file())
    read_button.place(x=910, y=20)

    choice = Button(root, width=7, height=1, text='날짜 선택', command = lambda: get_date_list())
    choice.place(x=910, y=45)
    
    canvas.mainloop()

def set_color(line):
    global date_time, degree, supply_degree, return_degree, rt

    total_rt = str(line[0])
    refs = list(map(int, eval(line[1])))
    entrophy = str(line[2])
    return_degree = float(line[3])
    date = str(line[4])
    color = 'orange'
    if return_degree >=7 and return_degree <=12:
        color = "#00FF11"
    
    elif return_degree >12 and return_degree <=15:
        color = "yellow"
    
    elif return_degree > 15:
        color = "red"

    if refs.count(475) == 1:
        canvas.itemconfig(turbor1, fill='#19EB35')
        canvas.itemconfig(turbor2, fill='#AEAEAE')
    elif refs.count(475) == 2:
        canvas.itemconfig(turbor1, fill='#19EB35')
        canvas.itemconfig(turbor2, fill='#19EB35')   
    elif refs.count(475) == 0:
        canvas.itemconfig(turbor1, fill='#AEAEAE')
        canvas.itemconfig(turbor2, fill='#AEAEAE')     

    if refs.count(180) == 1:
        canvas.itemconfig(turbor3, fill='#19EB35')
        canvas.itemconfig(turbor4, fill='#AEAEAE')
    elif refs.count(180) == 2:
        canvas.itemconfig(turbor3, fill='#19EB35')
        canvas.itemconfig(turbor4, fill='#19EB35')   
    elif refs.count(180) == 0:
        canvas.itemconfig(turbor3, fill='#AEAEAE')
        canvas.itemconfig(turbor4, fill='#AEAEAE') 

    if refs.count(600) == 0:
        canvas.itemconfig(absortion1, fill='gray')
        canvas.itemconfig(absortion2, fill='gray') 
        canvas.itemconfig(absortion3, fill='gray')
        canvas.itemconfig(absortion4, fill='gray') 
    
    elif refs.count(600) == 1:
        canvas.itemconfig(absortion1, fill='#19EB35')
        canvas.itemconfig(absortion2, fill='gray') 
        canvas.itemconfig(absortion3, fill='gray')
        canvas.itemconfig(absortion4, fill='gray') 
    
    elif refs.count(600) == 2:
        canvas.itemconfig(absortion1, fill='#19EB35')
        canvas.itemconfig(absortion2, fill='#19EB35') 
        canvas.itemconfig(absortion3, fill='gray')
        canvas.itemconfig(absortion4, fill='gray') 
    
    elif refs.count(600) == 3:
        canvas.itemconfig(absortion1, fill='#19EB35')
        canvas.itemconfig(absortion2, fill='#19EB35') 
        canvas.itemconfig(absortion3, fill='#19EB35')
        canvas.itemconfig(absortion4, fill='gray') 
    
    elif refs.count(600) == 4:
        canvas.itemconfig(absortion1, fill='#19EB35')
        canvas.itemconfig(absortion2, fill='#19EB35') 
        canvas.itemconfig(absortion3, fill='#19EB35')
        canvas.itemconfig(absortion4, fill='#19EB35') 
    
    date_time = canvas.create_text(90, 30, text=date, font=('', 10), anchor='w')
    degree = canvas.create_text(90, 50, text=str(entrophy)+'도', font=('', 10), anchor='w')
    supply_degree = canvas.create_text(90, 70, text='5.0도', font=('', 10), anchor='w')
    return_degree = canvas.create_text(90, 90, text=str(return_degree)+'도', font=('', 10), anchor='w')
    rt = canvas.create_text(105, 110, text=total_rt+'RT', font=('', 10), anchor='w')

    canvas.itemconfig(supply_pipe, fill='#0099ff')
    canvas.itemconfig(return_pipe, fill=color)
    
    root.update()  

def open_file():
    global df
    global filename
    global date

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

        try:
            date_list_box.delete(0, END)
        except:
            pass

        for d in date:
            date_list_box.insert('end', d)

        date_list_box.config(yscrollcommand=scroll.set)
        scroll.config(command=custom_command)

    except:
        messagebox.showwarning("파일 불러오기 오류", "파일을 불러올 수 없습니다.")

def read_file():  
    global df 
    global date_list_box
    try:          
        df_list = df.to_numpy().tolist()
        for i in range(date_list_box.nearest(0), len(df_list)):  
            date_list_box.see(i)

            try:
                canvas.delete(date_time, degree, supply_degree, return_degree, rt)
            except:
                pass      

            set_color(df_list[i])
            time.sleep(1)

    except:
        messagebox.showwarning("파일 불러오기 오류", "파일을 먼저 선택해 주세요.")              
            
def select_date(date_index):
    global select

    date_list_box.see(date_index)
    select = df.loc[date_index].tolist()
    try:
        canvas.delete(date_time, degree, supply_degree, return_degree, rt)
    except:
        pass     

    set_color(select)
    
def get_date_list():   
    try:
        height = 18*len(date)+70
        if height > 600:
            height = 600

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

    date_list_box.yview(*args)
    select = df.loc[date_list_box.nearest(0)].tolist()

    try:
        canvas.delete(date_time, degree, supply_degree, return_degree, rt)
    except:
        pass      
    set_color(select)

if __name__ == '__main__':
    main()