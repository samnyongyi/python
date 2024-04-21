 # 배열로 구현된 스택(함수버전)
 capacity = 10            # 스택 용량
 array = [None]*capacity  # 요소 배열
 top = -1                 # 상단의 인덱스: 공백상태(-1)로 초기화

 def isEmpty( ) :
    if top == -1 : return True	# 공백이면 True 반환
    else : return False			
 
 def isFull( ) :
   return top == capacity-1	    # 비교 연산 결과를 바로 반환

 def push( e ) :
    global top  # top은 전역변수
    if not isFull() :		    # 포화상태가 아닌 경우
        top += 1			    # top 증가(global top 선언 필요)
        array[top] = e
    else :			            # 포화상태: overflow 
        print("stack overflow")
        exit()

 def pop( ) :
    global top
    if not isEmpty():		    # 공백상태가 아닌 경우
        top -= 1			    # top 감소(global top 선언 필요)
        return array[top+1]
    else:			            # 공백상태: underflow 
        print("stack underflow")
        exit()

 def peek( ) :
    if not isEmpty():		    # 공백상태가 아닌 경우
        return array[top]
    else: pass			        # underflow 예외는 처리하지 않았음

 #  스택의 size() 연산
 def size( ) : return top+1	    # 현재 요소의 수는 top+1
스택은 선입후출이기에 입력한 문자열이 역순으로 출력
