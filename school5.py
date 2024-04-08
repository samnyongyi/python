'''
a=200

if a<100:
    print("100보다 작군요.")
print("거짓이므로 이 문장은 안 보이겠죠?")

print("프로그램 끝")
'''

'''
##a=200
a=99

if a<100:
    print("100보다 작군요.")
    print("거짓이므로 이 문장은 안 보이겠죠?")

print("프로그램 끝")    
'''

'''
##a=200
a=99

if a<100:
    print("100보다 작군요.")
else:
    print("100보다 크군요.")
'''

'''
a=200

if a<100:
    print("100보다 작군요.")
    print("참이면 이 문장도 보이겠죠?")
else:
    print("100보다 크군요.")
    print("거짓이면 이 문장도 보이겠죠?")
print("프로그램 끝")

'''

'''
a=int(input("정수를 입력하세요:"))

if a%2==0:
    print("짝수를 입력했군요.")
else:
    print("홀수를 입력했군요.")
'''

'''
a=int(input("수를 입력"))

if a%3==0:
    print("3의 배수")
else:
    print("3의 배수가 아님")
'''

'''
##a=75
a=50

if a>50:
    if a<100:
        print("50보다 크고 100보다 작군요.")
    else:
        print("와~~100보다 크군요.")
else:
    print("에고~50보다 작군요.")
'''

'''
score=int(input("점수를 입력하세요:"))

if score>=95:
    print("A+")
elif score >=90:
    print("A")
elif score >=85:
    print("B+")
elif score >=80:
    print("B")
elif score >=75:
    print("C+")
elif score >=70:
    print("C")
elif score >=65:
    print("D+")
elif score >=60:
    print("D")
else:
    print("F")

print("학점입니다")
'''

'''
import turtle

swidth, sheight=500, 500
turtle.title('무지개색 원그리기')
turtle.shape('turtle')
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()
turtle.goto(0,-sheight/2)
turtle.pendown()
turtle.speed(1000)

for raidus in range(1,250):
    if raidus %6==0:
        turtle.pencolor('red')
    elif raidus %5==0:
        turtle.pencolor('orange')
    elif raidus %4==0:
        turtle.pencolor('yellow')
    elif raidus %3==0:
        turtle.pencolor('green')
    elif raidus %2==0:
        turtle.pencolor('blue')
    elif raidus %1==0:
        turtle.pencolor('navyblue')
    else:
        turtle.pencolor('purple')

    turtle.circle(raidus)

turtle.done()
'''

'''
import random

numbers=[]
for num in range(0,10):
    numbers.append(random.randrange(0,10))

print("생성된 리스트", numbers)

for num in range(0,10):
    if num not in numbers:
        print("숫자 %d는(은) 리스트에 없네요." %num)
'''

'''
select, answer, numStr, num1, num2=0,0,"",0,0

select=int(input("1.입력한 수식 계산 2. 두 수 사이의 합계:"))

if select==1:
    numStr=input("***수식을 입력하세요:")
    answer=eval(numStr)
    print("%s결과는 %5.1f입니다." %(numStr, answer))
elif select==2:
    num1=int(input("***첫번째 숫자를 입력하세요:"))
    num2=int(input("***두번쨰 숫자를 입력하세요:"))
    for i in range(num1, num2+1):
        answer=answer+i
    print("%d+...+%d는 %d입니다." %(num1,num2,answer))
else:
    print("1또는 2만 입력해야합니다.")
'''

'''
num1, num2, num3, total=0,0,0,0

num1=int(input("첫번째 숫자"))
num2=int(input("두번째 숫자"))
num3=int(input("세번째 숫자"))

for i in range(num1, num2+1,num3):
    total=total+i
         
print("%d+%d...+%d는 %d입니다."  %(num1, num1+num3, num2, total))
'''

'''
num1=0
num2=True

num1=int(input("숫자를 입력"))

for i in range(2, num1):
    if num1%i==0:
        num2=False

if num2==True:
    print("%d는 소수입니다" %(num1))
else:
    print("%d는 소수가 아닙니다"%(num1))
'''

'''
import random

dice1,dice2,dice3,dice4,dice5,dice6=[0]*6
throwCount,serialCount=0,0

if __name__=="__main__":
    while True:
        throwCount+=1
        dice1=random.randrange(1,7)
        dice2=random.randrange(1,7)
        dice3=random.randrange(1,7)
        dice4=random.randrange(1,7)
        dice5=random.randrange(1,7)
        dice6=random.randrange(1,7)

        if dice1==dice2==dice3==dice4==dice5==dice6 :
            print('6개의 주사위가 모두 동일한 숫자가 나왔다', dice1,dice2,dice3,dice4,dice5,dice6 )
            break
        
        elif(dice1==1 or dice2==1 or dice3==1 or dice4==1 or dice5==1 or dice6==1) and \
            (dice1==2 or dice2==2 or dice3==2 or dice4==2 or dice5==2 or dice6==2) and \
            (dice1==3 or dice2==3 or dice3==3 or dice4==3 or dice5==3 or dice6==3) and \
            (dice1==4 or dice2==4 or dice3==4 or dice4==4 or dice5==4 or dice6==4) and \
            (dice1==5 or dice2==5 or dice3==5 or dice4==5 or dice5==5 or dice6==5) and \
            (dice1==6 or dice2==6 or dice3==6 or dice4==6 or dice5==6 or dice6==6) :
            serialCount+=1
            
    print('6개가 동일한 숫자가 나올때까지 주사위를    던진 횟수' ,throwCount)
    print('6개가 동일한 숫자가 나올때까지, 1~6의 연속번호가 나온  횟수' ,serialCount)
'''


import turtle
import math
import random

t1,t2,t3=[None]*3
t1X,t1Y,t2X,t2Y,t3X,t3Y=[0]*6
swidth,sheight=300,300

if __name__=="__main__":
    turtle.title('거북 만나기')
    turtle.setup(width=swidth+50, height=sheight+50)
    turtle.screensize(swidth,sheight)

    t1=turtle.Turtle('turtle'); t1.color('red'); t1.penup()
    t2=turtle.Turtle('turtle'); t2.color('green'); t2.penup()
    t3=turtle.Turtle('turtle'); t3.color('blue'); t3.penup()

    t1.goto(-100, -100); t2.goto(0,0); t3.goto(100,100)
    t1.speed(1000); t2.speed(1000); t3.speed(1000)

    while True:
        angle=random.randrange(0,360)
        dist=random.randrange(1,50)
        t1.left(angle); t1.forward(dist)
        angle=random.randrange(0,360)
        dist=random.randrange(1,50)
        t2.left(angle); t2.forward(dist)
        angle=random.randrange(0,360)
        dist=random.randrange(1,50)
        t3.left(angle); t3.forward(dist)

        t1X=t1.xcor(); t1Y=t1.ycor()
        t2X=t2.xcor(); t2Y=t2.ycor()
        t3X=t3.xcor(); t3Y=t3.ycor()

        if math.sqrt(((t1X-t2X)*(t1X-t2X))+((t1Y-t2Y)*(t1Y-t2Y))) <= 20 or \
           math.sqrt(((t1X-t3X)*(t1X-t3X))+((t1Y-t3Y)*(t1Y-t3Y))) <= 20 or \
           math.sqrt(((t2X-t3X)*(t2X-t3X))+((t2Y-t3Y)*(t2Y-t3Y))) <= 20 :
            break
turtle.done()
