 # 배열로 구현된 리스트(함수버전) 
 # 리스트의 데이터: 전역 변수
 capacity = 100           # 리스트 용량
 array = [None]*capacity  # 요소 배열: [None, .., None] (길이가 capacity), 크기는  capacity로 고정
 size = 0                 # 상단의 인덱스: 리스트 항목들의 개수 
 # 리스트의 연산: 일반 함수
 def isEmpty( ) :
    if size == 0 : return True	
    else : return False			
 def isFull( ) :
   return size == capacity	    
 def getEntry(pos) :
    if 0 <= pos < size :
        return array[pos]
    else : return None
 def insert( pos, e ) :
    global size                     # size는 전역변수
    if not isFull() and 0 <= pos <= size :
        for i in range(size, pos,-1) :
            array[i] = array[i-1]   # 한 칸씩 뒤로 옮김
        array[pos] = e              # pos위치에 새로운 요소 추가
        size += 1                   # 요소의 수가 하나 증가
    else : 
        print("리스트 overflow 또는 유효하지 않은 삽입 위치")
        exit()
 def delete( pos ) :
    global size                     # size는 전역변수
    if not isEmpty() and 0 <= pos < size :
        e = array[pos]
        for i in range(pos, size-1) :
            array[i] = array[i+1]   # 한 칸씩 앞으로 당김
        size -= 1                   # 요소의 수가 하나 감소
        return e
    else : 
        print("리스트 underflow 또는 유효하지 않은 삭제 위치")
        exit()
 # 추가 연산들
 def find(e) :
    for i in range(size) :
        if e == array[i] :
            return i
    return -1

 def display(msg='ArrayList:' ):
    print(msg, array[0:size])
