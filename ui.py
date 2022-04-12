from fileinput import filename
import time
import csv
import pandas as pd

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
from matplotlib.pyplot import text

filename = ''

w = 900
h = 800

lupx = lupy = 20
rupx = w-20
rupy=20
ldpx = 20
ldpy = h-20
rdpx = w-20
rdpy = h-20

root = Tk()
root.title("Energy ui")
root.resizable(False, False)
root.iconbitmap('inu.ico')
root.geometry('1000x950')

canvas = Canvas(root, width=w, height=h, bg="white", highlightbackground='black')
canvas.place(x=50, y=75)

# img = Image.open('refrigerator.png')
# img = img.resize((300,150))
# img = ImageTk.PhotoImage(img)
# canvas.create_image(180, h/2, image=img)
#canvas.create_line(222, 444, 50, 644)#x 222 y 444 공급 박스 중심점
# circle = canvas.create_oval(lupx, lupy, lupx+50, lupy+50)#생성하려는원 외접 사각형의 좌상단, 우하단 좌표
# rectangle = canvas.create_rectangle(rdpx-50, rdpy-50, rdpx, rdpy, fill='gray')
supply_pipe = [190, h/2+20, 
               270, h/2+20, 
               270, h-100,
               740, h-100,
               740, h-200,
               780, h-200,
               780, h-60,
               230, h-60,
               230, h/2+60,
               190, h/2+60]

return_pipe = [190, h/2-20, 
               270, h/2-20, 
               270, 100,
               740, 100,
               740, 200,
               780, 200,
               780, 60,
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
canvas.create_rectangle(640, 200, 880, h-200, fill='gray')
canvas.create_text(760, h/2, text='건물', font=('', 20))

#파이프
supply_pipe = canvas.create_polygon(supply_pipe, fill='white', outline='black')
return_pipe = canvas.create_polygon(return_pipe, fill='white', outline='black')

canvas.create_text(500, 30, text='환수 파이프', font=("", 20))
canvas.create_text(500, 670, text='공급 파이프', font=("", 20))

canvas.create_text(85, 30, text='날짜/시간 :', font=('', 10), anchor='e')
canvas.create_text(85, 50, text='외기 온도 :', font=('', 10), anchor='e')
canvas.create_text(85, 70, text='공급 온도 :', font=('', 10), anchor='e')
canvas.create_text(85, 90, text='환수 온도 :', font=('', 10), anchor='e')
canvas.create_text(5, 110, text='건물 냉방 부하 :', font=('', 10), anchor='w')

image = Image.open("green_to_red.png").resize((20, 95))
image = ImageTk.PhotoImage(image)
canvas.create_text(820, 20, anchor='w', text='환수 온도 색상 변화', font=("", 7))
canvas.create_image(870, 30, anchor='nw',image=image)
canvas.create_text(840, 35, anchor='w', text='17.0도', font=("", 7))
canvas.create_text(840, 118, anchor='w', text='12.0도', font=("", 7))

def set_color(line):
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
    degree = canvas.create_text(90, 50, text=entrophy, font=('', 10), anchor='w')
    supply_degree = canvas.create_text(90, 70, text='5.0도', font=('', 10), anchor='w')
    return_degree = canvas.create_text(90, 90, text=str(return_degree)+'도', font=('', 10), anchor='w')
    rt = canvas.create_text(105, 110, text=total_rt+'rt', font=('', 10), anchor='w')

    canvas.itemconfig(supply_pipe, fill='#0099ff')
    canvas.itemconfig(return_pipe, fill=color)
    
    root.update()  

    return date_time, degree, supply_degree, return_degree, rt

def read_file(filename):
    if filename == '':
        messagebox.showwarning("파일 불러오기 오류", "파일을 먼저 선택해 주세요.")
    else:
        with open(filename, 'r', encoding='utf-8') as f:
            rdr = csv.reader(f)
            rdr = list(rdr)
            for line in rdr[1:]:    
                try:
                    canvas.delete(date_time, degree, supply_degree, return_degree, rt)
                except:
                    pass      
                date_time, degree, supply_degree, return_degree, rt = set_color(line)
                time.sleep(1)
                
            
def select_file():
    global filename
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

    except:
        messagebox.showwarning("파일 불러오기 오류", "파일을 불러올 수 없습니다.")

def select_date(df, date_index):
    select = df.loc[date_index].tolist()
    date_time, degree, supply_degree, return_degree, rt = set_color(select)
    try:
        canvas.delete(date_time, degree, supply_degree, return_degree, rt)
    except:
        pass
    
def date_list(filename):
    if 'csv' in filename:
        df = pd.read_csv(filename)

    elif 'xlsx' in filename:
        df = pd.read_excel(filename)
    
    else:
        messagebox.showwarning("파일 불러오기 오류", "파일을 먼저 선택해 주세요.")
    
    date_list = df['date'].tolist()

    height = 18*len(date_list)+70
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
    list_.bind('<Double-1>', lambda event: select_date(df, list_.curselection()))
    scb = Scrollbar(new_window, orient='vertical')
    scb.config(command=list_.yview)
    scb.pack(side='right', fill='y')  

    select_date_button = Button(new_window, width=7, height=1, text='가져오기', command=lambda: select_date(df, list_.curselection()))
    select_date_button.place(x=245, y=30, anchor='ne')
    list_.config(yscrollcommand=scb.set)
    for date in date_list:
        list_.insert('end', date)

open_button = Button(root, width=7, height=1, text='파일 열기', command = select_file)
open_button.place(x=50, y=15)

read_button = Button(root, width=7, height=1, text='재생', command = lambda: read_file(filename))
read_button.place(x=50, y=45)

choice = Button(root, width=7, height=1, text='날짜 선택', command = lambda: date_list(filename))
choice.place(x=953, y=45, anchor='ne')
canvas.mainloop()