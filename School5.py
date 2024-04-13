'''
i, hap=0,0

for i in range(1,11,1):
    hap=hap+i

print("1에서 10까지의 합: %d" %hap)
'''
'''
i, hap=0,0

for i in range(1,101,1):
    hap=hap+i

print("1에서 100까지의 합: %d" %hap)
'''
'''
i, hap=0,0

for i in range(501,1001,2):
    hap=hap+i

print("500에서 1000사이에 있는 홀수의 합: %d" %hap)
'''
'''
i, hap=0,0

for i in range(2,1001,2):
    hap=hap+i

print("0에서 1000사이에 있는 짝수의 합: %d" %hap)
'''
'''
i, hap=0,0

for i in range(0,101,7):
    hap=hap+i

print("0에서 1000사이에 있는 7배수수의 합: %d" %hap)
'''
'''
i, hap=0,0
num=0

num=int(input("값을 입력: "))

for i in range(1,num+1,1):
    hap=hap+i

print("1에서 %d까지의 합: %d" %(num,hap))
'''
'''
i, hap=0,0
num1,num2,num3=0,0,0

num=int(input("시작값을 입력: "))
num2=int(input("끝값을 입력: "))
num3=int(input("증가값을 입력: "))

for i in range(num1,num2+1,num3):
    hap=hap+i

print("%d에서 %d까지 %d씩 증가시킨 값의 합: %d" %(num1, num2, num3,hap))
'''
'''
i, dan=0,0

dan=int(input("단을 입력:"))

for i in range(1,10,1):
    print("%d X %d=%2d" %(dan, i,dan*i))
'''
'''
i, dan=0,0

dan=int(input("단을 입력:"))

for i in range(9,0,-1):
    print("%d X %d=%2d" %(i, dan,dan*i))
'''
'''
i,k=0,0

for i in range(2,10,1):
    for k in range(1,10,1):
        print("%d X %d=%2d" %(i,k,i*k))
    print("")
'''
'''
i,k=0,0

for i in range(2,10,1):
    print("%d단" %(i))
    for k in range(1,10,1):
        print("%d X %d=%2d" %(i,k,i*k))
    print("")
'''
'''
i,k,guguLine=0,0,""

for i in range(2,10):
    guguLine=guguLine+("# %d단 #" %i)

print(guguLine)

for i in range(1,10):
    guguLine=""
    for k in range(2,10):
        guguLine=guguLine+str("%2d X %2d=%2d" %(k,i,k*i))
    print(guguLine)
'''
'''
i,k,num=0,0,""

for i in range(2,10):
    num=""
    for k in range(1,10):
        num=num+str("%dX%d=%2d\t" %(i,k,k*i))
    print(num)
'''
'''
i,k,num=0,0,""

ary=""

for i in range(9,1,-1):
    ary=ary+("%d단\t" %i)
print(ary)

for i in range(9,0,-1):
    num=""
    for k in range(9,1,-1):
        num=num+str("%dX%d=%2d\t" %(k,i,k*i))
    print(num)
'''
'''
i, hap=0,0

i=1
while i<11:
    hap=hap+i
    i=i+1

print("1에서 10까지의 합: %d" %hap)
'''
'''
num,num2,num3=0,0,0
total=num

num=int(input("시작값을 입력: "))
num2=int(input("끝값을 입력: "))
num3=int(input("증가값을 입력: "))

while num<num2+1:
    total=total+num
    num=num+num3
    
print("%d에서 %d까지 %d씩 증가시킨 값의 합: %d" %(num, num2, num3,total))
'''
'''
hap=0
a, b=0,0

while True:
    a=int(input("더할 첫 번째 수를 입력: "))
    b=int(input("더할 두 번째 수를 입력: "))
    hap=a+b
    print("%d+%d=%d" %(a,b, hap))
'''
'''
ch=""
a,b=0,0

while True:
    a=int(input("더할 첫 번째 수를 입력: "))
    b=int(input("더할 두 번째 수를 입력: "))
    ch=input("계산할 연산자를 입력: ")

    if(ch=="+"):
        print("%d+%d=%d" %(a,b, a+b))
    elif(ch=="-"):
        print("%d-%d=%d" %(a,b, a-b))
    elif(ch=="*"):
        print("%d*%d=%d" %(a,b, a*b))
    elif(ch=="/"):
        print("%d/%d=%d" %(a,b, a/b))
    else:
        print("잘못 입력")
'''
'''
hap=0
a,b=0,0

while True:
    a=int(input("첫번째 수 입력"))
    if a==0:
        break
    b=int(input("더할 두 번째 수를 입력: "))
    hap=a+b
    print("%d+%d=%d" %(a,b, hap))
print("0을 입력해 반복문 탈출")
'''
'''
ch=""
a,b=0,0

while True:
    a=int(input("첫번째 수 입력: "))
    if a==0:
        break
    b=int(input("두 번째 수를 입력: "))
    ch=input("계산할 연산자를 입력: ")

    if(ch=="+"):
        print("%d+%d=%d" %(a,b, a+b))
    elif(ch=="-"):
        print("%d-%d=%d" %(a,b, a-b))
    elif(ch=="*"):
        print("%d*%d=%d" %(a,b, a*b))
    elif(ch=="/"):
        print("%d/%d=%d" %(a,b, a/b))
    elif(ch=="//"):
        print("%d/%d=%d" %(a,b, a//b))
    elif(ch=="/"):
        print("%d**d%d=%d" %(a,b, a**b))
    else:
        print("잘못 입력")
'''
'''
hap,i=0,0

for i in range(1,101):
    hap+=i

    if hap>=1000:
        break

print("1~100의 합계를 최초로 1000이 넘게 하는 숫자: %d" %i)
'''
'''
hap,i=0,1

while i<101:
    hap+=i
    if hap>=1000:
        break
    i=i+1

print("1~100의 합계를 최초로 1000이 넘게 하는 숫자: %d" %i)
'''
'''
hap,i=0,0

for i in range(1,101):
    if i%3==0:
        continue

    hap+=i

print("1~100의 합계(3의 배수 제외): %d" %hap)
'''
'''
i=0
while i<9:
    if i<5:
        k=0
        while k<4-i:
            print('  ', end='')
            k+=1
        k=0
        while k<i*2+1:
            print('\u2605', end='')
            k+=1
    else:
        k=0
        while k<i-4:
            print('  ', end='')
            k+=1
        k=0
        while k<(9-i)*2-1:
            print('\u2605', end='')
            k+=1
    print()
    i+=1
'''
'''
i=0
while i<9:
    if i<5:
        k=0
        while k<4-i:
            print('  ', end='')
            k+=1
        k=0
        while k<i*2+1:
            print('\u2665', end='')
            k+=1
    else:
        k=0
        while k<i-4:
            print('  ', end='')
            k+=1
        k=0
        while k<(9-i)*2-1:
            print('\u2665', end='')
            k+=1
    print()
    i+=1
'''
'''
i,k,heartNum=0,0,0
numStr,ch,heartStr="","",""

if __name__=="__main__":
    numStr=input("숫자를 여러 개 입력하세요: ")
    print("")
    i=0
    ch=numStr[i]
    while True:
        heartNum=int(ch)

        heartStr=""
        for k in range(0,heartNum):
            heartStr+="\u2665"
            k+=1
        print(heartStr)

        i+=1
        if(i>len(numStr)-1):
            break
        ch=numStr[i]
'''
