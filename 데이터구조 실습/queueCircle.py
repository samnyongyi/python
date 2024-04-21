 # 배열로 구현된 원형 큐 클래스
 class CircularQueue :
    def __init__( self, capacity = 8 ) :
        self.capacity = capacity        # 용량(고정)
        self.array = [None] * capacity  # 요소들을 저장할 배열
        self.front = 0                  # 전단의 인덱스
        self.rear = 0                   # 후단의 인덱스
    def isEmpty( self ) :
       return self.front == self.rear   # 공백상태
    def isFull( self ) :
       return self.front == (self.rear+1)%self.capacity # front이 rear와 같으면 포화상태
    def enqueue( self, item ):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity # rear 시계방향 회전
            self.array[self.rear] = item    # 요소 저장
    def dequeue( self ):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity   # front 회전
            return self.array[self.front]   # 위치의 요소 반환
    def peek( self ):	# front 자체는 미변경
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else: pass

    # 큐의 전체 요소의 수 계산
    def size( self ) :
       return (self.rear - self.front + self.capacity) % self.capacity

    # 문자열 변환을 위한 str 연산자 중복
    def __str__(self):
        if self.front < self.rear :
            return str(self.array[self.front+1:self.rear+1])
        else :
            return str(self.array[self.front+1:self.capacity] + \	# \, 문자열연결연산자
                       self.array[0:self.rear+1] )
