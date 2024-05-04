'''
구조 변경 불가, 변경시 리스트
tt=((1,2,3),(4,5,6),(7,8,9))
for i in range(0,3):
    for k in range(0,3):
        print("%3d" %tt[i][k], end=" ")
    print("")
'''
'''
singer={}

singer['이름']='트와이스'
singer['구성원 수']=9
singer['데뷔']='서바이벌 식스틴'
singer['대표곡']='SIGNAL'

for k in singer.keys():
    print('%s-->%s'%(k,singer[k]))
'''
'''
import operator

trainDic, trainList={},[]

trainDic={'Thomas':'토마스','Edward':'에드워드','Henry':'헨리','Gothen':'고든','James':'제임스'}

trainList=sorted(trainDic.items(),key=operator.itemgetter(1))

print(trainList)
'''
'''
foods={"떡볶이":"오뎅", "짜장면":"단무지","라면":"김치","피자":"피클","맥주":"땅콩","치킨":"치킨무","삼겹살":"상추"};

while(True):
    myfood=input(str(list(foods.keys()))+"중 좋아하는 음식은?")
    if myfood in foods:
        print("<%s>궁합 음식은 <%s>입니다." %(myfood, foods.get(myfood)))
    elif myfood=="끝":
        break
    else:
        print("그런 음식이 없습니다. 확인해 보세요.")
'''
'''
animals={"개":"강아지","호랑이":"개호주","말":"망아지","곰":"능소니","닭":"병아리","고등어":"고도리","명태":"노가리"};

while(True):
    myPet=input(str(list(animals.keys()))+"중 새끼 이름을 알고 싶은 동물은?")
    if myPet in animals:
        print("<%s>의 새끼는 <%s>입니다." %(myPet, animals.get(myPet)))
    elif myPet=="끝":
        break
    else:
        print("그런 동물이 없습니다. 확인해 보세요.")
'''
'''
import random

data=[]
i,k=0,0

if __name__=="__main__":
    for i in range(0,10):
        tmp=hex(random.randrange(0,100000))
        data.append(tmp)
    print('초기 데이터:', end=' ')
    [print(num,end=' ') for num in data]; print(""); print("")
    for i in range(0,len(data)-1):
        for k in range(i+1, len(data)):
            if int(data[i],16)>int(data[k],16):
                tmp=data[i]
                data[i]=data[k]
                data[k]=tmp
        print(str(i+1)+'단계정렬: ',end=' ')
        [print(num,end=' ') for num in data]; print(""); print("")
'''

voca={}
tempList=[]
temp=""
menu=0

while(True):
    menu=input("메뉴를 선택하세요.(단어 입력=1, 단어 출력=2, 단어 검색=3, 종료=0)")
    if menu=='1'
        temp=input("등록할 단어 입력(영어-한글): ")
           
    
