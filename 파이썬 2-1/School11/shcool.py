'''list11,2,3,4]
list2=[10,20,30,40]
myList=list(map(lambda num1, num2: num1+num2, list1, list2))
print(myList)
'''
'''
def count(num):
    if num>=1:
        print(num, end=' ')
        count(num-1)
    else:
        return
count(10)
print("")
count(20)
'''
'''
def factorial(num):
    if num<=1:
        return num
    else:
        return num*factorial(num-1)
print(factorial(4))
print(factorial(10))
'''
'''
def genFunc():
    yield 1 
    yield 2
    yield 3

print(list(genFunc()))
'''
'''
def genFunc(num):
    for i in range(0,num):
        yield i
        print('제너레이터 진행중')
for data in genFunc(5):
    print(data)
'''
'''
import random

def getNumber(strData):
    numStr=''
    for ch in strData:
        if ch.isdigit():
            numStr+=ch
    return int(numStr)
data=[]
i,k=0,0
if __name__=="__main__":
    for i in range(0,10):
        tmp=hex(random.randrange(0,100000))
        tmp=tmp[2:]
        data.append(tmp)
    print("정렬 전 데이터:", end="")
    [print(num,end=" ")for num in data]
    for i in range(0,len(data)-1):
        for k in range(i+1, len(data)):
            if getNumber(data[i])>getNumber(data[k]):
                tmp=data[i]
                data[i]=data[k]
                data[k]=tmp
    print("\n정렬 후 데이터:", end="")
    [print(num, end=" ") for num in data]
'''
'''
from time import*
from datetime import*

def countDays(date1, date2):
    retDays=0
    year, month, day=date1.split('/')
    sDay=date(int(year), int(month),int(day))
    year,month,day=date2.split('/')
    eDay=date(int(year),int(month),int(day))
    diffDays=eDay-sDay
    retDays=diffDays.days
    return retDays
def getDay(t):
    weeks=['월','화','수','목','금','토','일']
    return weeks[t.tm_wday]
startDate,curDate,tm='','',None
if __name__=="__main__":
    startDate=input("시작날짜(연/월/일)-->")
    tm=localtime()
    curDate=str(tm.tm_year)+'/'+str(tm.tm_mon)+'/'+str(tm.tm_mday)
    print(startDate,'부터 오늘(',curDate,')까지는',countDays(startDate, curDate),'일이 지났습니다')
    print("그리고 오늘은 ",getDay(tm),"요일입니다")
'''
'''
from tkinter import*

window=Tk()
window.title("윈도창 연습")
window.geometry("400x100")
window.resizable(width=FALSE, height=FALSE)

window.mainloop()
'''
'''
from tkinter import*
window=Tk()

label1=Label(window, text="COOKBOOK~~Python을")
label2=Label(window, text="열심히",font=("궁서체",30),fg="blue")
label3=Label(window, text="공부 중입니다.",bg="magenta",width=20, height=5,anchor=SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()
'''
'''
from tkinter import*
window=Tk()
photo=PhotoImage(file="gif/dog.gif")
label1=Label(window,image=photo)

label1.pack()
window.mainloop()
'''
'''
from tkinter import*
window=Tk()
window.title("냥이들^^")

photo1=PhotoImage(file="gif/cat.gif")
label1=Label(window, image=photo1)

photo2=PhotoImage(file="gif/cat2.gif")
label2=Label(window, image=photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)

window.mainloop()
'''
'''
from tkinter import*
window=Tk()

butoon1=Button(window, text="파이썬종료",fg="red",command=quit)

butoon1.pack()

window.mainloop()
'''
'''
from tkinter import*
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("강아지 버튼","강아지가 귀엽죠?^^")
window=Tk()

photo=PhotoImage(file="gif/dog2.gif")
button1=Button(window,image=photo,command=myFunc)
button1.pack()
window.mainloop()
'''
'''
from tkinter import*
from tkinter import messagebox
window=Tk()

def myFunc():
    if chk.get()==0:
        messagebox.showinfo("","체크버튼이 꺼졌어요.")
    else:
        messagebox.showinfo("","체크버튼이 켜졌어요.")
chk=IntVar()
cb1=Checkbutton(window, text="클릭하세요",variable=chk, command=myFunc)
cb1.pack()
window.mainloop()
'''
from tkinter import*
window=Tk()

def myFunc():
    if var.get()==1:
        label1.configure(text="파이썬")
    elif var.get()==2:
        label1.configure(text="C++")
    else:
        label1.configure(text="Java")
var=IntVar()
rb1=Radiobutton(window, text="파이썬",variable=var,value=1,command=myFunc)
rb2=Radiobutton(window, text="C++",variable=var,value=2,command=myFunc)
rb3=Radiobutton(window, text="Java",variable=var,value=3,command=myFunc)

label1=Label(window,text="선택한 언어: ",fg="red")
rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()
