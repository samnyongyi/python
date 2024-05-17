'''
coffee=0
coffee=int(input("어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙)"))
print()
print("#1.뜨거운 물을 준비한다.")
print("#2.종이컵을 준비한다.")
if coffee==1:
    print("#3.보통커피를 탄다.")
elif coffee==2:
    print("#3.설탕커피를 타다.")
elif coffee==3:
    print("#3.블랙커피를 탄다.")
else:
    print("#3.아무거나 탄다.\n")

print("#4.물을 붓는다.")
print("#5.스푼으로 젓는다.")
print()
print("손님~커피 여기 있습니다.")
'''
'''
def plus(v1,v2):
    result=0
    result=v1+v2
    return result
hap=0
hap=plus(100,200)
print("100과 200의 plus()함수 결과는 %d" %hap)
'''
'''
def calc(v1,v2,op):
    result=0
    if op=="+":
        result=v1+v2
    elif op=="-":
        result=v1-v2
    elif op=="*":
        result=v1*v2
    elif op=="/":
        result=v1/v2
    return result
res=0
var,var2,oper=0,0,""
oper=input("계산을 입력하세요(+,-,*,/):")
var1=int(input("첫 번째 수를 입력하세요:"))
var2=int(input("두 번 수를 입력하세요:"))
res=calc(var1,var2,oper)
print("##계산기:%d%s%d=%d"%(var1,oper,var2,res))
'''
'''
def calc(v1,v2,op):
    result=0
    if op=="+":
        result=v1+v2
    elif op=="-":
        result=v1-v2
    elif op=="*":
        result=v1*v2
    elif op=="/":
        result=v1/v2
    elif op=="**":
        result=v1**v2
    return result
res=0
var,var2,oper=0,0,""
var1=int(input("첫 번째 수를 입력하세요:"))
oper=input("계산을 입력하세요(+,-,*,/,**):")
var2=int(input("두 번 수를 입력하세요:"))
if var2==0:
    print("0으로 나누면 안됩니다ㅠㅠ")
else:
    res=calc(var1,var2,oper)
    print("##계산기:%d%s%d=%d"%(var1,oper,var2,res))
'''
'''
def func1():
    a=10
    print("func1()에서 a값 %d"%a)
def func2():
    print("func2()에서 a값 %d"%a)
a=20
func1()
func2()
'''
'''
def func1():
    global a
    a=10
    print("func1()에서 a값 %d" %a)
def func2():
    print("func2()에서 a값 %d" %a)
a=20
func1()
func2()
'''
'''
def func1():
    result=100
    return result
def func2():
    print("반환값이 없는 함수 실행")
hap=0
hap=func1()
print("func1()에서 돌려준 값==>%d" %hap)
func2()
'''
'''
def multi(v1,v2):
    retList=[]
    res1=v1+v2
    res2=v1-v2
    retList.append(res1)
    retList.append(res2)
    return retList
myList=[]
hap,sub=0,0
myList=multi(100,200)
hap=myList[0]
sub=myList[1]
print("multi()에서 돌려준 값==>%d,%d"%(hap,sub))
'''
'''
def multi(v1,v2):
    retList=[]
    res1=v1+v2
    res2=v1-v2
    return res1,res2
myList=[]
hap,sub=0,0
hap,sub=multi(100,200)
print("multi()에서 돌려준 값==>%d,%d"%(hap,sub))
'''
'''
def para2_func(v1,v2):
    result=0
    result=v1+v2
    return result
def para3_func(v1,v2,v3):
    result=0
    result=v1+v2+v3
    return result
hap=0
hap=para2_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과==>%d"%hap)
hap=para3_func(10,20,30)
print("매개변수가 3개인 함수를 호출한 결과==>%d"%hap)
'''
'''
def para_func(v1,v2,v3=0):
    result=0
    result=v1+v2+v3
    return result
hap=0
hap=para_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과==>%d"%hap)
hap=para_func(10,20,30)
print("매개변수가 3개인 함수를 호출한 결과==>%d"%hap)
'''
'''
def f(n1,n2,n3=0,n4=0,n5=0,n6=0,n7=0,n8=0,n9=0,n10=0):
    result=0
    result=n1+n2+n3+n4+n5+n6+n7+n8+n9+n10
    return result
hap=0
hap=f(10,20)
print("매개변수가 2개인 함수를 호출한 결과==>%d"%hap)
hap=f(10,20,30,40,50,60,70,80,90,100)
print("매개변수가 3개인 함수를 호출한 결과==>%d"%hap)
'''
'''
def para_func(*parp):
    result=0
    for num in para:
        result=result+num

    return result
hap=0
hap=para_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과==>%d"%hap)
hap=para_func(10,20,30)
print("매개변수가 3개인 함수를 호출한 결과==>%d"%hap)
'''
'''
import random

def getNumber():
    return random.randrange(1,46)
lotto=[]
num=0
print("**로또 추첨을 시작합니다.**\n")
while True:
    num=getNumber()

    if lotto.count(num)==0:
        lotto.append(num)
    if len(lotto)>=6:
        break
print("추첨된 로또 번호==>",end='')
lotto.sort()
for i in range(0,6):
    print("%d " %lotto[i],end='')
'''
'''
def func1():
    print("school.py의 func1()이 호출됨.")
def func2():
    print("school.py의 func2()이 호출됨.")
def func3():
    print("school.py의 func3()이 호출됨.") 
'''
'''
import sys
print(sys.builtin_module_names)

import math
dir(math)
'''
from myTurtle import*
import turtle

inStr=''
swidth, sheight=300,300
tX,tY, tAngle,tSize=[0]*4

turtle.title('거북이 글자 쓰기(모듈버전)')
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()
turtle.speed(5)

inStr=getString()
for ch in inStr:
    tX,tY,tAngle, tSize=getXYAS(swidth, sheight)
    r,g,b=getRGB()

    turtle.goto(tX,tY)
    turtle.left(tAngle)

    turtle.pencolor((r,g,b))
    turtle.write(ch,font=('맑은고딕',tSize,'bold'))

turtle.done()
