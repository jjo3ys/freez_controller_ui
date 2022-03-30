import time
import math

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

w = 1000
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
root.geometry('1100x1000')


canvas = Canvas(root, width=w, height=h, bg="white", highlightbackground='black')
canvas.place(x=50, y=100)

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
               230, h-60,#740
               230, h/2+60,#460
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

canvas.create_rectangle(lupx+20, h/2-60, lupx+170, h/2+60, fill='#0099ff')
canvas.create_text(lupx+95, h/2, text="냉동기", font=('', 20))

canvas.create_rectangle(640, 200, 880, h-200, fill='gray')
canvas.create_text(760, h/2, text='건물', font=('', 20))

canvas.create_polygon(supply_pipe, fill='white', outline='black')
canvas.create_polygon(return_pipe, fill='white', outline='black')

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = filedialog.askopenfilename(
        title='파일 선택',
        initialdir='/',
        filetypes=filetypes)

    with open(filename, 'r', encoding='utf-8') as f:
        try:
            lines = f.readlines()
            for line in lines:
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
                return_1 = canvas.create_polygon(return_coord, fill='orange')
                for i in range(33):
                    sub_return_coord = [740, 380, 780, 380, 780, 380-i*10, 740, 380-i*10]
                    canvas.coords(return_1, sub_return_coord)
                    root.update()
                    time.sleep(0.01)

                return_2 = canvas.create_polygon([740, 100, 740, 60], fill='orange')
                for i in range(52):
                    sub_return_coord = [740, 60, 740, 100, 740-i*10, 100, 740-i*10, 60]
                    canvas.coords(return_2, sub_return_coord)
                    root.update()
                    time.sleep(0.01)

                return_3 = canvas.create_polygon([230, 100, 270, 100], fill='orange')
                for i in range(29):
                    sub_return_coord = [230, 100, 270, 100, 270, 100+i*10, 230, 100+i*10]
                    canvas.coords(return_3, sub_return_coord)
                    root.update()
                    time.sleep(0.01)
                
                return_4 = canvas.create_polygon([230, 340, 230, 380], fill='orange')
                for i in range(9):
                    sub_return_coord = [230, 340, 230, 380, 230-i*10, 380, 230-i*10, 340]
                    canvas.coords(return_4, sub_return_coord)
                    root.update()
                    time.sleep(0.01)
                    
                time.sleep(0.5)
                canvas.delete(supply_1, supply_2, supply_3, supply_4, return_1, return_2, return_3, return_4)
                
        except:
            messagebox.showwarning("파일 불러오기 오류", "파일을 불러올 수 없습니다.")

open_button = Button(root, text='파일 열기', command = select_file)
open_button.place(x=10, y=10)

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