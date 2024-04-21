 from ArrayList import ArrayList
 # 배열구조의 리스트를 이용한 라인 편집기 프로그램
 list = ArrayList()  # 라인 편집기로 사용할 리스트 객체 생성
 while True :
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q- 종료=> ")

    if command == 'i' :
        pos = int( input("  입력행 번호: ") )
        str = input("  입력행 내용: ")
        list.insert(pos, str)

    elif command == 'd' :
        pos = int( input("  삭제행 번호: ") )
        list.delete(pos)

    elif command == 'r' :
        pos = int( input("  변경행 번호: ") )
        str = input("  변경행 내용: ");
        list.replace(pos, str)

    elif command == 'p' :
        print('Line Editor')
        for line in range (list.size) :
            print('[%2d] '%line, end='')
            print(list.getEntry(line))
        print()

    elif command == 'q' : exit()

    elif command == 'l' :   # 파일 읽기 명령은 test.txt 파일의 모든 라인을 읽어 라인 편집기의 맨 뒤에 순서대로 저장
        filename = 'test.txt'  
        infile = open(filename , "r")    # 파일을 읽기 전용으로 열기
        lines = infile.readlines();  # 파일의 모든 라인을 읽어 lines에 저장
        for line in lines:	# 라인들을 순서대로 리스트의 맨뒤에 삽입
            list.insert(list.size, line.rstrip('\n'))	# 각 문자열 마지막에 \n이 있을 경우 이를 제거하기 위해 문자열 클래스의 rstrip()함수 사용
        infile.close()  # 파일 닫기

    elif command == 's' :   # 파일 쓰기 명령이면 현재 편집기의 모든 라인을 test.txt 파일에 저장
        filename = 'test.txt'
        outfile = open(filename , "w")
        len = list.size
        for i in range(len) :
            outfile.write(list.getEntry(i)+'\n')
        outfile.close()
