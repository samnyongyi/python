 # 배열로 구현된 리스트 클래스 
 class ArrayList:
    # 리스트의 데이터: 생성자에서 정의 및 초기화
    def __init__( self, capacity=100 ):	# 매개변수에서의 sef는 C++에서 this와 유사한 의미, 그저 멤버함수에서 객체 자신을 나타내는 변수라고 인식해도 무관
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    # 리스트의 연산: 클래스의 메소드
    def isEmpty( self ):
       return self.size == 0
    def isFull( self ):
       return self.size == self.capacity

    def getEntry(self, pos) :
        if 0 <= pos < self.size :
            return self.array[pos]
        else : return None

    def insert( self, pos, e ) :
        if not self.isFull() and 0 <= pos <= self.size :
            for i in range(self.size, pos,-1) :
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1
        else : pass # 예외상황 미처리

    def delete( self, pos ) :
        if not self.isEmpty() and 0 <= pos < self.size :
            e = self.array[pos]
            for i in range(pos, self.size-1) :
                self.array[i] = self.array[i+1]
            self.size -= 1
            return e
        else : pass # 예외상황 미처리

    def __str__( self ) :
        return str(self.array[0:self.size]) # 문자열 변환 연산자 str중복 함수, 유효한 항목들만(0~size-1)을 뽑아 문자열로 변환 후 반환
