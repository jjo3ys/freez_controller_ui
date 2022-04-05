import time
import csv

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
from matplotlib.pyplot import text

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

canvas.create_rectangle(30, 340, 190, 460, fill='#0099ff')
canvas.create_text(115, 400, text="냉동기", font=('', 20))

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

canvas.create_rectangle(640, 200, 880, h-200, fill='gray')
canvas.create_text(760, h/2, text='건물', font=('', 20))

canvas.create_polygon(supply_pipe, fill='white', outline='black')
canvas.create_polygon(return_pipe, fill='white', outline='black')

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

def select_file():
    filetypes = (
        ('csv files', '*.csv'),
        ('excel files', '*.xlsx'),
        ('All files', '*.*')
    )

    filename = filedialog.askopenfilename(
        title='파일 선택',
        initialdir='/',
        filetypes=filetypes)

    with open(filename, 'r', encoding='utf-8') as f:
        # try:
        rdr = csv.reader(f)
        rdr = list(rdr)
        # lines = f.readlines()
        for line in rdr:
            print(line[1])
            
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

            root.update()

            
            date_time = canvas.create_text(90, 30, text=date, font=('', 10), anchor='w')
            degree = canvas.create_text(90, 50, text=entrophy, font=('', 10), anchor='w')
            supply_degree = canvas.create_text(90, 70, text='7.0도', font=('', 10), anchor='w')
            return_degree = canvas.create_text(90, 90, text=str(return_degree)+'도', font=('', 10), anchor='w')
            rt = canvas.create_text(105, 110, text=total_rt+'rt', font=('', 10), anchor='w')

            supply_coord = [190, 420, 190, 460]
            return_coord = [190, 380, 190, 340]
            supply_1 = canvas.create_polygon(supply_coord, fill='#0099ff')
            for i in range(9):
                sub_supply_coord = [190, 420, 190, 460, 190+i*10, 460, 190+i*10, 420]
                canvas.coords(supply_1, sub_supply_coord)
                root.update()
                time.sleep(0.01)

            supply_2 = canvas.create_polygon([230, 460, 270, 460], fill='#0099ff')
            for i in range(29):
                sub_supply_coord = [230, 460, 270, 460, 270, 460+i*10, 230, 460+i*10]
                canvas.coords(supply_2, sub_supply_coord)
                root.update()
                time.sleep(0.01)
            
            supply_3 = canvas.create_polygon([270, 420, 270, 460], fill='#0099ff')
            for i in range(52):
                sub_supply_coord = [270, 700, 270, 740, 270+i*10, 740, 270+i*10, 700]
                canvas.coords(supply_3, sub_supply_coord)
                root.update()
                time.sleep(0.01)

            supply_4 = canvas.create_polygon([740, 700 ,780, 700], fill='#0099ff')
            for i in range(29):
                sub_supply_coord = [740, 700, 780, 700, 780, 700-i*10, 740, 700-i*10]
                canvas.coords(supply_4, sub_supply_coord)
                root.update()
                time.sleep(0.01)

            time.sleep(0.5)
            return_1 = canvas.create_polygon(return_coord, fill=color)
            for i in range(33):
                sub_return_coord = [740, 380, 780, 380, 780, 380-i*10, 740, 380-i*10]
                canvas.coords(return_1, sub_return_coord)
                root.update()
                time.sleep(0.01)

            return_2 = canvas.create_polygon([740, 100, 740, 60], fill=color)
            for i in range(52):
                sub_return_coord = [740, 60, 740, 100, 740-i*10, 100, 740-i*10, 60]
                canvas.coords(return_2, sub_return_coord)
                root.update()
                time.sleep(0.01)

            return_3 = canvas.create_polygon([230, 100, 270, 100], fill=color)
            for i in range(29):
                sub_return_coord = [230, 100, 270, 100, 270, 100+i*10, 230, 100+i*10]
                canvas.coords(return_3, sub_return_coord)
                root.update()
                time.sleep(0.01)
            
            return_4 = canvas.create_polygon([230, 340, 230, 380], fill=color)
            for i in range(9):
                sub_return_coord = [230, 340, 230, 380, 230-i*10, 380, 230-i*10, 340]
                canvas.coords(return_4, sub_return_coord)
                root.update()
                time.sleep(0.01)
                
            time.sleep(0.5)
            canvas.delete(supply_1, supply_2, supply_3, supply_4, return_1, return_2, return_3, return_4, date_time, degree, supply_degree, return_degree, rt)
            
        # except:
        #     messagebox.showwarning("파일 불러오기 오류", "파일을 불러올 수 없습니다.")

open_button = Button(root, text='파일 열기', command = select_file)
open_button.place(x=50, y=25)

# arc1 = canvas.create_arc(lupx, lupy, lupx-50, lupy+50, start = 160, extent=120, style=ARC) # extent 호의 각도, style=ARC 일 때 호만, 없을 때 피자형태
# point = [w/2-25, h/2+10, w/2+25, h/2+10, w/2, h/2-40]
# canvas.create_polygon(point, outline='black', fill='white', width=3)
# canvas.create_line(lupx, lupy, rdpx, rdpy, fill='red')#코드 순서대로 도형 순서
# #canvas.create_image(rdpx, rdpy, anchor=NW, image=PhotoImage(file="")) anchor=NW: 이미지의 좌상단점을 기준점으로 사용
# for x in range(120):
#     canvas.move(arc1, 5, 0)# (n, x, y) n object를 x좌표를 x만큼, y좌표를 y만큼 이동
#     root.update()
#     time.sleep(1/60)
canvas.mainloop()