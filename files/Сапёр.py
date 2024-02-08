from tkinter import *
from PIL import Image,ImageTk
import random
import time
def square(row, col,w,color):
    array = []
    for i in range(row):
        array.append([])
        for j in range(col):
            array[i].append(canvas.create_rectangle(w + j * w,w + i * w, w + (j + 1) * w, w + (i + 1) * w, fill = color))
            win.update()
            
    return array

def bomb(row,col):
    bomb_ar = (random.sample(range(1,row*col),row*col//6))
    print(bomb_ar)
    return bomb_ar

def znach(row,col):
    ar_znach = []
    for j in range(1,row+1):
        ar_znach.append([])
        for i in range(1,col+1):
            cnt = 0
            i = col*(j-1)+i
            
            if bomb_ar.count(i)!=0:
                ar_znach[j-1].append('x')
            else:
                if bomb_ar.count(i+1)!=0 and i%col!=0:
                    cnt+=1
                if bomb_ar.count(i-1)!=0 and i%col!=1:
                    cnt+=1
                if bomb_ar.count(i-col-1)!=0 and i%col!=1 and j!=1:
                    cnt+=1
                if bomb_ar.count(i-col+1)!=0 and i%col!=0 and j!=1:
                    cnt+=1
                if bomb_ar.count(i-col)!=0 and j!=1:
                    cnt+=1
                if bomb_ar.count(i+col)!=0 and j!=row:
                    cnt+=1
                if bomb_ar.count(i+col+1)!=0 and i%col!= 0 and j!=row:
                    cnt+=1
                if bomb_ar.count(i+col-1)!=0 and i%col!=1 and j!=row:
                    cnt+=1
                ar_znach[j-1].append(cnt)
    return ar_znach

def price(w,id_array,ar_znach,row,col,cur_id,cur_id_zn,img_array,ar_0,y,x):
    global ar_otkr
    global del_array
    if ar_otkr.count(cur_id)==0:
        ar_otkr.append(cur_id)
    if cur_id_zn==0 and ar_0.count(cur_id)==0:
        ar_0.append(cur_id)
        del_array.append(canvas.create_image(((cur_id-1)%(col)+1)*w+w//2+1,(cur_id-1)//(row)*w+w//2+1+w,image = img_array[0]))
        if cur_id>col:
            
            price(w,id_array,ar_znach,row,col,id_array[y-1][x],ar_znach[y-1][x],img_array,ar_0,y-1,x)
            
        if cur_id%col!=1:
            
            price(w,id_array,ar_znach,row,col,id_array[y][x-1],ar_znach[y][x-1],img_array,ar_0,y,x-1)
            
        if cur_id<=(col*(row-1)):
            
            price(w,id_array,ar_znach,row,col,id_array[y+1][x],ar_znach[y+1][x],img_array,ar_0,y+1,x)
            
        if cur_id%col!=0:
            
            price(w,id_array,ar_znach,row,col,id_array[y][x+1],ar_znach[y][x+1],img_array,ar_0,y,x+1)

        
        if cur_id>col and cur_id%col!=1:
            
            price(w,id_array,ar_znach,row,col,id_array[y-1][x-1],ar_znach[y-1][x-1],img_array,ar_0,y-1,x-1)

        if cur_id%col!=1 and cur_id<=(col*(row-1)):

            price(w,id_array,ar_znach,row,col,id_array[y+1][x-1],ar_znach[y+1][x-1],img_array,ar_0,y+1,x-1)

        if cur_id<=(col*(row-1)) and cur_id%col!=0:
            
            price(w,id_array,ar_znach,row,col,id_array[y+1][x+1],ar_znach[y+1][x+1],img_array,ar_0,y+1,x+1)
            
        if cur_id%col!=0 and cur_id>col:

            price(w,id_array,ar_znach,row,col,id_array[y-1][x+1],ar_znach[y-1][x+1],img_array,ar_0,y-1,x+1)
        
    elif cur_id_zn == 1:
        del_array.append(canvas.create_image(((cur_id-1)%(col)+1)*w+w//2+1,(cur_id-1)//(row)*w+w//2+1+w,image = img_array[1]))
        
        
    elif cur_id_zn == 2:
        del_array.append(canvas.create_image(((cur_id-1)%(col)+1)*w+w//2+1,(cur_id-1)//(row)*w+w//2+1+w,image = img_array[2]))
        
        
    elif cur_id_zn == 3:
        del_array.append(canvas.create_image(((cur_id-1)%(col)+1)*w+w//2+1,(cur_id-1)//(row)*w+w//2+1+w,image = img_array[3]))
        
        
    elif cur_id_zn == 4:
        del_array.append(canvas.create_image(((cur_id-1)%(col)+1)*w+w//2+1,(cur_id-1)//(row)*w+w//2+1+w,image = img_array[4]))
        
       
    elif cur_id_zn == 5:
        del_array.append(canvas.create_image(((cur_id-1)%(col)+1)*w+w//2+1,(cur_id-1)//(row)*w+w//2+1+w,image = img_array[5]))
        
        
    elif cur_id_zn == 6:
        del_array.append(canvas.create_image(((cur_id-1)%(col)+1)*w+w//2+1,(cur_id-1)//(row)*w+w//2+1+w,image = img_array[6]))
        
        
    elif cur_id_zn == 7:
        del_array.append(canvas.create_image(((cur_id-1)%(col)+1)*w+w//2+1,(cur_id-1)//(row)*w+w//2+1+w,image = img_array[7]))
        
        
    elif cur_id_zn == 8:
        del_array.append(canvas.create_image(((cur_id-1)%(col)+1)*w+w//2+1,(cur_id-1)//(row)*w+w//2+1+w,image = img_array[8]))
        
def wina(ar_bomb,col,row):
    global id_array
    cnt = 0
    if (len(ar_otkr)+len(ar_bomb))== col*row:
        for i in bomb_ar:
            if ar_otkr.count(i)!=0:
                cnt+=1
        if cnt == 0:
            return 1
        else:
            return 0

def r_clck(event,w,id_array,bomb_ar,row,col,img_array,color,lbl):
    global flag_ar
    global kol,lbl2
    x = event.x
    y = event.y
    cnt = 0
    cur_id = id_array[y//w-1][x//w-1]
    
    if wina(bomb_ar,col,row)==1:
        for i in flag_ar:
            if bomb_ar.count(i)==1:
                cnt+=1
        if cnt == len(bomb_ar) and d==0:
            
            lbl1['text'] = "Поздравляем, Вы выиграли"
            
    if flag_ar.count(cur_id)==1:
        del_array.append(canvas.create_rectangle(((cur_id-1)%(col)+1)*w, (cur_id-1)//(row)*w+w,((cur_id-1)%(col)+1)*w+w,(cur_id-1)//(row)*w+w+w, fill = color))
        flag_ar.remove(cur_id)
        lbl.config(text = 'Мины: '+str(kol+1))
        kol +=1
    elif ar_otkr.count(cur_id)==0:
        del_array.append(canvas.create_image(((cur_id-1)%(col)+1)*w+w//2+1,(cur_id-1)//(row)*w+w//2+1+w,image = img_array[9]))
        flag_ar.append(cur_id)
        lbl.config(text = 'Мины: '+str(kol-1))
        kol-=1
    
def l_clck(event,w,id_array,bomb_ar,ar_znach,row,col,img_array):
    global d,lbl2
    x = event.x
    y = event.y
    ar_0 = []
    cnt =0
    cur_id = id_array[y//w-1][x//w-1]
    cur_id_zn = ar_znach[y//w-1][x//w-1]
    print(cur_id)
    
    
    if (x>w) and (x<=col*w+w) and (y>w) and (y<=row*w+w):
        clck_id = id_array[y//w-1][x//w-1]
        if bomb_ar.count(clck_id)!=0 and d==0:
            death(x,y,cur_id,col,row,w,bomb_ar)
        else:
            price(w,id_array,ar_znach,row,col,cur_id,cur_id_zn,img_array,ar_0,y//w-1,x//w-1)
            
    if wina(bomb_ar,col,row)==1 and d==0:
        
        lbl1['text'] = "Поздравляем, Вы выиграли"
  

def death(x,y,cur_id,col,row,w,bomb_ar):
    global lbl2,d,t
    d = 1
    del_array.append(canvas.create_image(((cur_id-1)%(col)+1)*w+w//2+1,(cur_id-1)//(row)*w+w//2+1+w,image = img_array[11]))
    
    for i in bomb_ar:
        if i != cur_id:
            del_array.append(canvas.create_image(((i-1)%(col)+1)*w+w//2+1,(i-1)//(row)*w+w//2+1+w,image = img_array[10]))
            del_array.append(canvas.create_image(((i-1)%(col)+1)*w+w//2+1,(i-1)//(row)*w+w//2+1+w,image = img_array[10]))
            time.sleep(0.05)
            win.update()
    
    lbl1['text'] = "Вы проиграли"
    
def restart():
    global lbl1,lbl,t,del_array,id_array,bomb_ar,flag_ar,ar_otkr,ar_znach,d,kol
    for i in range(len(del_array)):
        canvas.delete(del_array[i])
    lbl1.destroy()
    lbl.destroy()
    
    del_array = []
    bomb_ar = bomb(row,col)
    flag_ar = []
    ar_otkr = []
    ar_znach = znach(row,col)
    d = 0
    kol = len(bomb_ar)
    lbl1 = Label(text = 'ПКМ - флажок')
    lbl1.place(x = 160, y=10)
    lbl = Label(text = 'Мины: '+str(kol))
    lbl.place(x = (w*row//6), y=w+w*col+w//2)
    return id_array,bomb_ar,flag_ar,ar_otkr,ar_znach
    
win = Tk()
win.title('Cапёр')
win.resizable(0, 0)
row = 10
col = 10
w = 40
d = 0
color = 'SkyBlue3'
canvas = Canvas(win, width = (row + 2)*w , height = (col + 3)*w)
canvas.pack()
id_array = square(row, col,w,color)
bomb_ar = bomb(row,col)
flag_ar = []
ar_otkr = []
del_array = []
ar_znach = znach(row,col)
kol = len(bomb_ar)
lbl = Label(text = 'Мины: '+str(kol))
lbl.place(x = (w*row//6), y=w+w*col+w//2)
lbl1 = Label(text = 'ПКМ - флажок')
lbl1.place(x = 160, y=10)
btn = Button(win, text="Начать заново",command = restart)
btn.pack(side = 'top')


win.bind('<Button-3>', lambda event: r_clck(event,w,id_array,bomb_ar,row,col,img_array,color,lbl))#пкм
win.bind('<Button-1>', lambda event: l_clck(event,w,id_array,bomb_ar,ar_znach,row,col,img_array))#лкм

imge0 = Image.open("0.png")
imge1 = Image.open("1.png")
imge2 = Image.open("2.png")
imge3 = Image.open("3.png")
imge4 = Image.open("4.png")
imge5 = Image.open("5.png")
imge6 = Image.open("6.png")
imge7= Image.open("7.png")
imge8= Image.open("8.png")
imge9= Image.open("flag.png")
imge10= Image.open("bomb.png")
imge11= Image.open("bomb1.png")

imge0.thumbnail((w,w))
imge1.thumbnail((w,w))
imge2.thumbnail((w,w))
imge3.thumbnail((w,w))
imge4.thumbnail((w,w))
imge5.thumbnail((w,w))
imge6.thumbnail((w,w))
imge7.thumbnail((w,w))
imge8.thumbnail((w,w))
imge9.thumbnail((w,w))
imge10.thumbnail((w,w))
imge11.thumbnail((w,w))

img0 = ImageTk.PhotoImage(imge0)
img1 = ImageTk.PhotoImage(imge1)
img2 = ImageTk.PhotoImage(imge2)
img3 = ImageTk.PhotoImage(imge3)
img4 = ImageTk.PhotoImage(imge4)
img5 = ImageTk.PhotoImage(imge5)
img6 = ImageTk.PhotoImage(imge6)
img7 = ImageTk.PhotoImage(imge7)
img8 = ImageTk.PhotoImage(imge8)
img_flag = ImageTk.PhotoImage(imge9)
img_bomb = ImageTk.PhotoImage(imge10)
img_bomb1 = ImageTk.PhotoImage(imge11)


img_array = [img0,img1,img2,img3,img4,img5,img6,img7,img8,img_flag,img_bomb,img_bomb1]


win.mainloop()


