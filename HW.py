voca = {}  
temp_list = []  
temp = ""
menu = 0

while True:
    menu = input("메뉴를 선택하세요.(단어 입력=1, 단어 출력=2, 단어 검색=3, 종료=0)")
    
    if menu == '1':
        print(end="\n")
        i = 0
        temp = input("등록할 단어 입력(영어-한글): ")
        temp_list = temp.split('-')
        voca[temp_list[0]] = temp_list[1] 
    elif menu == '2':
        print(end="\n")
        print(" [단어장 출력]")
        for i in voca: 
            print(i + " - " + voca[i])
        print(end="\n")
    elif menu == '3':
        temp = input("검색할 단어: ")
        print(end="\n")
        print("[검색 결과]")
        if temp not in voca:
            print(" 등록되지 않은 단어입니다")
            print(end="\n")
        else:
            print(" "+temp+"("+voca[temp]+")")
            print(end="\n")
    elif menu == '0':
        break

