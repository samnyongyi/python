'''
a,b,c,d=0,0,0,0
hap=0

a= int(input("1번쨰 숫자: "))
b= int(input("2번쨰 숫자: "))
c= int(input("3번쨰 숫자: "))
d= int(input("4번쨰 숫자: "))

hap=a+b+c+d

print("합계 ==> %d" %hap)
'''
'''
aa=[0,0,0,0]
hap=0

aa[0]=int(input("1번쨰 숫자: "))
aa[1]= int(input("2번쨰 숫자: "))
aa[2]= int(input("3번쨰 숫자: "))
aa[3]= int(input("4번쨰 숫자: "))

hap=aa[0]+aa[1]+aa[2]+aa[3]

print("합계 ==> %d" %hap)
'''
'''
aa=[]
for i in range(0,4):
    aa.append(0)
hap=0

for i in range(0,4):
    aa[i]=int(input(str(i+1)+"번째 숫자:"))

hap=aa[0]+aa[1]+aa[2]+aa[3]

print("합계==> %d" %hap)
'''
'''
aa=[]
for i in range(0,10):
    aa.append(0)
hap=0

for i in range(0,10):
    aa[i]=int(input(str(i+1)+"번째 숫자:"))

i=0
while(i<10):
    hap+=aa[i]
    i+=1
    
print("합계==> %d" %hap)
'''
'''
aa=[]
bb=[]
value=0

for i in range(0,100):
    aa.append(value)
    value+=2

for i in range(0,100):
    bb.append(aa[99-i])

print("bb[0]에는 %d이, bb[99]에는 %d이 입력" %(bb[0],bb[99]))
'''
'''
aa=[]
bb=[]
value=0

for i in range(0,200):
    aa.append(value)
    value+=3

for i in range(0,200):
    bb.append(aa[199-i])

print("bb[0]에는 %d이, bb[199]에는 %d이 입력" %(bb[0],bb[199]))
'''
'''
myList=[30,10,20]
print("현재 리스트: %s" %myList)

myList.append(40)
print("append(40) 후의 리스트: %s" %myList)

print("pop()으로 추출한 값: %s" %myList.pop())
print("pop()후의 리스트: %s" %myList)

myList.sort()
print("sort()후의 리스트: %s" %myList)

myList.reverse()
print("reverse()후의 리스트: %s" %myList)

print("20값의 위치: %d" %myList.index(20))

myList.insert(2,222)
print("insert(2,222)후의 리스트: %s: " %myList)

myList.remove(222)
print("remove(222)후의 리스트: %s: " %myList)

myList.extend([77,88,77])
print("extend([77,88,77])후의 리스트: %s" %myList)

print("77값의 개수: %d" %myList.count(77))
'''
'''
list1=[]
list2=[]
value=1

for i in range(0,3):
    for k in range(0,4):
        list1.append(value)
        value+=1
    list2.append(list1)
    list1=[]

for i in range(0,3):
    for k in range(0,4):
        print("%3d" %list2[i][k], end=" ")
    print("")
'''
'''
list1=[]
list2=[]
value=0

for i in range(0,4):
    for k in range(0,5):
        list1.append(value)
        value+=3
    list2.append(list1)
    list1=[]

for i in range(0,4):
    for k in range(0,5):
        print("%3d" %list2[i][k], end=" ")
    print("")
'''
import turtle
import random

myTurtle, tX,tY,tColor,tSize, tShape=[None]*6
shapeList=[]
playerTurtles=[]
swidth,sheight=500,500

if __name__=="__main__":
    turtle.title('거북 리스트 활용')
    turtle.setup(width=swidth+50, height=sheight+50)
    turtle.screensize(swidth,sheight)

    shapeList=turtle.getshapes()
    for i in range(0,100):
        random.shuffle(shapeList)
        myTurtle=turtle.Turtle(shapeList[0])
        tX=random.randrange(int(-swidth/2), int(swidth/2))
        tY=random.randrange(int(-sheight/2), int(sheight/2))
        r=random.random(); g=random.random(); b=random.random()
        tSize=random.randrange(1,3)
        playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b])

    for tList in playerTurtles:
        myTurtle=tList[0]
        myTurtle.color((tList[4], tList[5],tList[6]))
        myTurtle.pencolor((tList[4], tList[5],tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.goto(tList[1], tList[2])
    turtle.done()





