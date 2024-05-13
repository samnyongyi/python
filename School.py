'''
ss="파이썬짱!"
sslen=len(ss)
for i in range(0, sslen):
    print(ss[i]+'$', end='')
'''
'''
inStr, outStr="",""
count, i=0,0

inStr=input("문자열을 입력하세요:")
count=len(inStr)

for i in range(0,count):
    outStr+=inStr[count-(i+1)]

print("내용을 거꾸로 출력--> %s" %outStr)
'''
'''
ss='Phython is Easy. 그래서 programming이 재미있습니다.'
print(ss.upper())
print(ss.lower())
print(ss.swapcase())
print(ss.title())
'''
'''
ss="파이썬 공부는 즐겁습니다. 물론 모든 공부가 재미있지는 않죠.^^"
print(ss.count('공부'))
print(ss.find('공부'), ss.rfind('공부'),ss.find('공부',5),ss.find('없다'))
print(ss.index('공부'),ss.rindex('공부'),ss.index('공부',5))
print(ss.startswith('파이썬'), ss.startswith('파이썬', 10), ss.endswith('^^'))
'''
'''
ss=input("입력 문자열==>")
print("출력 문자열==>",end='')

if ss.startswith('(')==False:
    print("(",end='')

print(ss, end='')   #end='' 줄미바꿈

if ss.endswith(')')==False:
    print(")",end='')
'''
'''
inStr=" 한글 Phyton 프로그래밍 "
outStr=""

for i in range(0,len(inStr)):
    if inStr[i]!='':
        outStr+=inStr[i]

print("원래 문자열==>"+'['+inStr+']')
print("공백 삭제 문자열==>"+'['+outStr+']')
'''
'''
inStr="<<<파<이>썬>>>"
outStr=""

for i in range(0,len(inStr)):
    if inStr[i]!='<'and inStr[i]!='>':
        outStr+=inStr[i]
print("원래 문자열==>"+'['+inStr+']')
print("공백 삭제 문자열==>"+'['+outStr+']')
'''
'''
ss=input("입력 문자열==>")

print("출력 문자열==>",end='')
for i in range(0,len(ss)):
    if ss[i]!='o':
        print(ss[i], end='')
    else:
        print('$', end='')
'''
'''
ss=input("입력 문자열==>")

print("출력 문자열==>",end='')
print(ss.replace('o','$'))
'''
'''
ss='Phyton을 열심히 공부 중'
print(ss.split())
ss='하나:둘:셋'
print(ss.split(':'))
ss='하나\n둘\n셋'
print(ss.splitlines())
ss='%'
print(ss.join('파이썬'))
'''
'''
ss=input("날짜(연/월/일)입력==>")

ssList=ss.split('/')

print("입력한 날짜의 10년후==>",end='')
print(str(int(ssList[0])+10)+"년",end='')
print(ssList[1]+"월", end='')
print(ssList[2]+"일")
'''
'''
ss='파이썬'
print(ss.center(10))
print(ss.center(10,'-'))
print(ss.ljust(10))
print(ss.rjust(10))
print(ss.zfill(10))
'''
'''
while(True):
    str=input("문자열 입력:")
    if str=='0':
        break
    elif str.isdigit():
        print("숫자입니다.")
    elif str.isalpha():
        print("글자입니다.")
    elif str.isalnum():
        print("글자+숫자입니다.")
    else:
        print("모르겠습니다.ㅠㅠ")
'''
'''
import turtle
import random
from tkinter.simpledialog import*

inStr=''
swidth, sheight=300,300
tX,tY,txtSize=[0]*3

turtle.title('거북 글자쓰기')
turtle.shape('turtle')
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth, sheight)
turtle.penup()

inStr=askstring('문자열 입력', '거북이 쓸 문자열을 입력')

for ch in inStr:
    tX=random.randrange(int(-swidth/2), int(swidth/2))
    tY=random.randrange(int(-sheight/2),int(sheight/2))
    r=random.random(); g=random.random(); b=random.random()
    txtSize=random.randrange(10,50)

    turtle.goto(tX,tY)

    turtle.pencolor((r,g,b))
    turtle.write(ch,font=('맑은 고딕', txtSize, 'bold'))

turtle.done()
'''
