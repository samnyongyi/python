 # 정렬되지 않은 배열을 이용한 우선순위 큐 클래스
 class PriorityQueue :
    def __init__( self, capacity = 10 ) :
        self.capacity = capacity        # 용량(고정)
        self.array = [None] * capacity  # 요소들을 저장할 배열
        self.size = 0                   # size는 요소의 수

    def isEmpty( self ) :
       return self.size == 0    # 공백상태 조건

    def isFull( self ) :
       return self.size == self.capacity    # 포화상태 조건

    def enqueue( self, e ):
        if not self.isFull():
            self.array[self.size] = e   # 새로운 요소는 배열의 맨 뒤에 추가
            self.size += 1  # 삽입 후 size 증가

    def findMaxIndex( self ):   # 공백이 아니면 우선순위가 가장 높은 요소의 인덱스 highest를 구해 반환
        if self.isEmpty(): return -1
        highest = 0
        for i in range(1, self.size) :
            if self.array[i] > self.array[highest] :
                highest = i
        return highest

    def dequeue( self ):    # highest요소를 찾아 마지막 요소와 교환 후 마지막 요소를 반환
        highest = self.findMaxIndex()   # 우선순위가 가장 높은 요소 삭제
        if highest != -1 :
            self.size -= 1  # size 1 감소
            self.array[highest], self.array[self.size] = self.array[self.size], self.array[highest]
            return self.array[self.size]

    def peek( self ):   # 배열에서 우선순위가 가장 높은 요소를 찾아 배열에서 꺼내지 않고 참조하는 연산
        highest = self.findMaxIndex()
        if highest != -1 :
            return self.array[height]

    def __str__(self):  # 문자열 변환 연산자 중복함수
        return str(self.array[0:self.size])
