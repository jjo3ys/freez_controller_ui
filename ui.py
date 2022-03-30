import time
import math

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = filedialog.askopenfilename(
        title='파일 선택',
        initialdir='/',
        filetypes=filetypes)

    # with open(filename, 'r', encoding='utf-8') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         #canvas.

w = 1500
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
root.geometry('1600x1000')

open_button = Button(root, text='파일 열기', command=select_file)
open_button.place(x=10, y=10)
canvas = Canvas(root, width=w, height=h, bg="white", highlightbackground='black')
canvas.place(x=50, y=100)
img = Image.open('refrigerator.png')
img = img.resize((300,150))
img = ImageTk.PhotoImage(img)
canvas.create_image(180, h/2, image=img)
canvas.create_line(222, 444, 50, 644)#x 222 y 444 공급 박스 중심점
# circle = canvas.create_oval(lupx, lupy, lupx+50, lupy+50)#생성하려는원 외접 사각형의 좌상단, 우하단 좌표
# rectangle = canvas.create_rectangle(rdpx-50, rdpy-50, rdpx, rdpy, fill='gray')

arc1 = canvas.create_arc(rupx, rupy, rupx-50, rupy+50, start = 160, extent=120, style=ARC) # extent 호의 각도, style=ARC 일 때 호만, 없을 때 피자형태
# arc2 = canvas.create_arc(ldpx+50, ldpy-50, ldpx, ldpy, extent=270)
# point = [w/2-25, h/2+10, w/2+25, h/2+10, w/2, h/2-40]
# canvas.create_polygon(point, outline='black', fill='white', width=3)
# canvas.create_line(lupx, lupy, rdpx, rdpy, fill='red')#코드 순서대로 도형 순서
# #canvas.create_image(rdpx, rdpy, anchor=NW, image=PhotoImage(file="")) anchor=NW: 이미지의 좌상단점을 기준점으로 사용
# for x in range(60):
#     canvas.move(arc1, 5, 0)# (n, x, y) n object를 x좌표를 x만큼, y좌표를 y만큼 이동
#     root.update()
#     time.sleep(0.2)
canvas.mainloop()