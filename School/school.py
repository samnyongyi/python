"""
from tkinter import*
window=Tk()
button1=Button(window, text="버튼1")
button2=Button(window, text="버튼2")
button3=Button(window, text="버튼3")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
window.mainloop()
"""
"""
from tkinter import*
window=Tk()

btnList=[None]*3
for i in range(0,3):
    btnList[i]=Button(window, text="버튼"+str(i+1))
for btn in btnList:
    btn.pack(side=RIGHT)
window.mainloop()
"""
"""
from tkinter import*

btnList=[None]*9
fnameList=["froyo.gif","gingerbread.gif","honeycomb.gif","icecream.gif",
           "jellybean.gif","kitkat.gif","lollipop.gif","marshmallow.gif","nougat.gif"]
photoList=[None]*9
i,k=0,0
xPos,yPos=0,0
num=0

window=Tk()
window.geometry("210x210")

for i in range(0,9):
    photoList[i]=PhotoImage(file="gif/"+fnameList[i])
    btnList[i]=Button(window,image=photoList[i])
for i in range(0,3):
    for k in range(0,3):
        btnList[num].place(x=xPos, y=yPos)
        num+=1
        xPos+=70
    xPos=0
    yPos+=70
    
window.mainloop()
"""
"""
from tkinter import *
from time import *

fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif",
             "jeju8.gif", "jeju9.gif"]
photoList = [None] * 9
num = 0

def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file="gif/" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    nameLabel.configure(text=fnameList[num])

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file="gif/" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    nameLabel.configure(text=fnameList[num])

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text="<<이전", command=clickPrev)
btnNext = Button(window, text="다음>>", command=clickNext)

photo = PhotoImage(file="gif/" + fnameList[0])
pLabel = Label(window, image=photo)

nameLabel=Label(window,text=fnameList[0])

btnPrev.place(x=250, y=10)
nameLabel.place(x=330,y=10)
btnNext.place(x=400, y=10)
pLabel.place(x=15, y=50)

window.mainloop()
"""
"""
from tkinter import*
from tkinter import messagebox

def clickLeft(event):
    messagebox.showinfo("마우스", "마우스 왼쪽 버튼이 클릭됨")
window=Tk()
window.bind("<Button-1>",clickLeft)
window.mainloop()
"""
"""
from tkinter import*
from tkinter import messagebox

def clickImage(event):
    messagebox.showinfo("마우스","토끼에서 마우스가 클릭됨")

window=Tk()
window.geometry("400x400")

photo=PhotoImage(file="gif/rabbit.gif")
label1=Label(window,image=photo)
label1.bind("<Button>",clickImage)

label1.pack(expand=1,anchor=CENTER)
window.mainloop()
"""
"""
from tkinter import*

def clickMouse(event):
    txt=""

    if event.num==1:
        txt+="마우스 왼쪽 버튼이("
    elif event.num==3:\
        txt+="마우스 오른쪽 버튼이("
    txt+=str(event.y)+","+str(event.x)+")에서 클릭됨"
    label1.configure(text=txt)

window=Tk()
window.geometry("400x400")
label1=Label(window,text="이곳이 바뀜")
window.bind("<Button>",clickMouse)
label1.pack(expand=1, anchor=CENTER)
window.mainloop()
"""
"""
from tkinter import*
from tkinter import messagebox

def keyEvent(event):
    messagebox.showinfo("키보드 이벤트","눌린 키:"+chr(event.keycode))

window=Tk()
window.bind("<Key>",keyEvent)
window.mainloop()
"""
"""
from tkinter import*
from tkinter import messagebox

def keyEvent(event):
    txt="눌린 키:Shift +"
    if event.keycode==37:
        txt+="왼쪽 화살표"
    elif event.keycode==38:
        txt+="위쪽 화살표"
    elif event.keycode==38:
        txt+="오른쪽 화살표"
    elif event.keycode==39:
        txt+="아래쪽 화살표"

    messagebox.showinfo("키보드 이벤트",txt)
window=Tk()
window.bind("<Shift-Up>",keyEvent)
window.bind("<Shift-Down>",keyEvent)
window.bind("<Shift-Left>",keyEvent)
window.bind("<Shift-Right>",keyEvent)
window.mainloop()
"""
"""
from tkinter import*
from tkinter import messagebox
def func_open():
    messagebox.showinfo("메뉴선택","열기 메뉴를 선택함")
def func_exit():
    window.quit()
    window.destroy()
window=Tk()
mainMenu=Menu(window)
window.config(menu=mainMenu)

fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)

window.mainloop()
"""
"""
from tkinter import*
from tkinter.simpledialog import*

window=Tk()
window.geometry("400x100")
label1=Label(window,text="입력된 값")
label1.pack()
value=askinteger("확대배수","주사위 숫자(1~6)을 입력하세요",minvalue=1, maxvalue=6)
label1.configure(text=str(value))
window.mainloop()
"""
"""
from tkinter import*
from tkinter.filedialog import*
window=Tk()
window.geometry("400x100")
label1=Label(window, text="선택된 파일 이름")
label1.pack()
saveFp=asksaveasfile(parent=window, mode="w",defaultextension=".jpg",filetypes=(("JPG파일","*.jpg;*.jpeg"),("모든 파일","*.*")))
label1.configure(text=saveFp)
saveFp.close()
window.mainloop()
"""
"""
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.simpledialog import*

def func_open():
    filename = askopenfilename(parent=window, filetypes=(("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file=filename)
    width=photo.width()
    height=photo.height()
    for i in range(height):
        for k in range(width):
            r,g,b=photo.get(k,i)
            grey=int((r+g+b)/3)
            photo.put("#%02x%02x%02x"%(grey,grey,grey),(k,i))
    pLabel.configure(image=photo)
    pLabel.image = photo  

def func_exit():
    window.quit()
    window.destroy()

window = Tk()
window.geometry("400x400")
window.title("명화 감상하기")

photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

window.mainloop()
"""
"""
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.simpledialog import askinteger

def mouseClick(event):
    global x1, y1
    x1 = event.x
    y1 = event.y

def mouseDrop(event):
    global x1, y1, x2, y2, penWidth, penColor
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1, y1, x2, y2, width=penWidth, fill=penColor)

def getColor():
    global penColor
    color = askcolor()
    penColor = color[1]

def getWidth():
    global penWidth
    penWidth = askinteger("선 두께", "선 두께(1~10)를 입력하세요", minvalue=1, maxvalue=10)

window = None
canvas = None
x1, y1, x2, y2 = None, None, None, None
penColor = "black"
penWidth = 5

if __name__ == "__main__":
    window = Tk()
    window.title("그림판과 비슷한 프로그램")
    canvas = Canvas(window, width=400, height=400)
    canvas.bind("<Button-1>", mouseClick)
    canvas.bind("<ButtonRelease-1>", mouseDrop)
    canvas.pack()  

    mainMenu = Menu(window)
    window.config(menu=mainMenu)
    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="설정", menu=fileMenu)
    fileMenu.add_command(label="선 색상 선택", command=getColor)
    fileMenu.add_separator()
    fileMenu.add_command(label="선 두께 설정", command=getWidth)

    window.mainloop()
"""
from tkinter import*
from tkinter import ttk

window=Tk()
window.iconbitmap('python.ico')
baseTab=ttk.Notebook(window)
tabDog=ttk.Frame(baseTab)
baseTab.add(tabDog,text='강아지')
tabCat=ttk.Frame(baseTab)
baseTab.add(tabCat,text='고양이')
baseTab.pack(expand=1,fill="both")
photoDog=PhotoImage(file="gif/dog7.gif")
labelDog=Label(tabDog,image=photoDog)
labelDog.pack()
photoCat=PhotoImage(file="gif/cat5.gif")
labelCat=Label(tabCat,image=photoCat)
labelCat.pack()
window.mainloop()
