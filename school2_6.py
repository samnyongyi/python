def main():
    print('메인 함수 부분이 실행')
    myFunc()
    print('전역 변수 값:', gVar)

def myFunc():
    print('함수를 호출')

gVar=100

if __name__=='__main__':
    main()
