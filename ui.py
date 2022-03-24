from tkinter import *

w = 1500
h = 800

lupx = lupy = 20
rupx = w-20
rupy=20
ldpx = 20
ldpy = h-20
rdpx = w-20
rdpy = h-20

window = Tk()
window = Canvas(window, width=w, height=h)
window.pack()
window.create_oval(lupx, lupy, lupx+50, lupy+50)#생성하려는원 외접 사각형의 좌상단, 우하단 좌표
window.create_rectangle(rdpx-50, rdpy-50, rdpx, rdpy, fill='gray')

window.create_arc(rupx, rupy, rupx-50, rupy+50, extent=180, style=ARC) # extent 호의 각도, style=ARC 일 때 호만, 없을 때 피자형태
window.create_arc(ldpx+50, ldpy-50, ldpx, ldpy, extent=270)
point = [w/2-25, h/2+10, w/2+25, h/2+10, w/2, h/2-40]
window.create_polygon(point, outline='black', fill='white', width=3)
window.create_line(lupx, lupy, rdpx, rdpy, fill='red')#코드 순서대로 도형 순서
#window.create_image(rdpx, rdpy, anchor=NW, image=PhotoImage(file="")) anchor=NW: 이미지의 좌상단점을 기준점으로 사용

window.mainloop()