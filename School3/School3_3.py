'''print(10|7)
print(123|456)
print(0xFFFF|0x0000)

a=ord('A')
mask=0x0F

print("%x&%x=%x" % (a,mask, a&mask))
print("%x|%x=%x" % (a,mask, a|mask))
maks=ord('a')-ord('A')

b=a^mask
print("%c^%d=%c" %(a,mask,b))
a=b^mask
print("%c^%d=%c" %(b,mask, a))

a=12345
print(~a+1)

a=10
print(a<<1, a<<2, a<<3, a<<4)
print(a>>1, a>>2, a>>3, a>>4)

a=100
result=0
i=0
for i in range(1,5):
    result=a<<i
    print("%d<<%d=%d"%(a,i,result))

for i in range(1,5):
    result=a>>i
    print("%d>>%d=%d"%(a,i,result))
'''
'''
inValue=0
count=0
result=0
i=0

inValue=int(input("시프트할 숫자"))
count=int(input("출력할 횟수"))

for i in range(1, count+1):
    result= inValue <<i
    print("%d<<%d=%d"%(inValue, i, result))
for i in range(1, count+1):
    result= inValue >>i
    print("%d>>%d=%d"%(inValue, i, result))
    '''
'''
year=int(input("연도"))
if(((year%4==0)and (year%100!=0))or(year%400==0)):
    print("%d년은 윤년"%year);
else:
    print("%d년은 윤년이 아님"%year);

'''
import turtle

num=0
swidth, sheight=1000,300
curX,curY=0,0


turtle.title('거북이로 2진수 표현하기')
turtle.shape('turtle')
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.left(90)

num=int(input("숫자를 입력"))

binary=bin(num)
print(num , binary)

curX=swidth/2
curY=0

for i in range(len(binary)-2):
    turtle.goto(curX,curY)

    if num &1:
        turtle.color('red')
        turtle.turtlesize(2)
    else:
        turtle.color('blue')
        turtle.turtlesize(1)

    turtle.stamp()
    curX-=50
    num>>=1
        
turtle.done()
