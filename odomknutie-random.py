import tkinter as tk
import random
from PIL import Image, ImageTk, ImageDraw
import win32api

#Get screen size
s_width = win32api.GetSystemMetrics(0)
s_height = win32api.GetSystemMetrics(1)

#create image
background = Image.open('C:\\Users\\Martin Borcin\\OneDrive\\Documents\\py\\RSA\\background.png')
im = Image.new('RGBA', (s_width, s_height))
pix = im.load()

#color image
for x in range (s_width):
    for y in range (s_height):
        pix[x,y]=int(x/100),int(y/100),int(x%(y+1))
#im.save("backgound.jpg")

#create GUI with image background
#canvas = tk.Canvas()
GUI = tk.Tk()
GUI.title('RNDr. Pavol Galik')

layer2 = ImageTk.PhotoImage(im)
label2 = tk.Label(GUI, image = layer2)
label2.pack()

layer1 = ImageTk.PhotoImage(background)
label1 = tk.Label(GUI, image = layer1)
label1.pack()

#canvas.pack()

#declaring variables
xm = 0
ym = 0
kolko=1    
poleX = ""
poleY = ""

def start(suradnice):
    global xm
    global ym
    xm = abs(suradnice.x)
    ym = abs(suradnice.y)

def bod2 (suradnice):
    global poleX
    global poleY
    global im
    poleX = poleX + str(abs(suradnice.x))
    poleY = poleY + str(abs(suradnice.y))
    vytvor()#....zavolaj ked sa vymaze obrazok
    im.save("save.png")

def guma(suradnice):
    global xm
    global ym
    global poleX
    global poleY
    global pix
    xs=xm
    ys=ym
    xm = suradnice.x
    ym = suradnice.y
    poleX = poleX + str(abs(xm))
    poleY = poleY + str(abs(ym))
    draw = ImageDraw.Draw(im)
    draw.line(((xs, ys),(xm, ym)), fill=(255,255,255,0), width=50)

#    canvas.create_line(xs, ys, xm, ym, capstyle=tkinter.ROUND, width=70, fill="white")

def vytvor():
    global poleX
    global poleY
    
    for_q= int(float("0."+ str(poleX))* random.randrange(10**75,10**155))
    for_p= int(float("0."+ str(poleY))* random.randrange(10**75,10**155))
    print(for_q)
    print(for_p)
    print(len(poleX),len(poleY))

def scan_image():
    global im
    global pix
    
    w, h = (im.size)
    orig = pix[0,0]
    for x in range (w):
        for y in range (h):
            if (pix[x,y]) != orig:
                return False
    return True
    

GUI.bind('<Button-1>', start)
GUI.bind('<B1-Motion>', guma)
GUI.bind("<ButtonRelease-1>",bod2)

GUI.mainloop()
