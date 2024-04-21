 # 원형 덱: 큐를 상속한 클래스 정의
 from CircularQueue import * # 원형 큐 클래스를 작성한 CircularQueue.py를 상속

 class CircularDeque(CircularQueue) :    # 생성자는 상속되지 않기에 작성
    def __init__( self, capacity=10 ) : # 부모를 부르는 함수 super()를 사용하여 생성자 __init()__호출
        super().__init__(capacity)  # 추가로 정의 할 데이터 멤버는 없으므로 
CircularQueue의 생성자 호출

    # 원형 덱: 동작이 동일한 연산들, 각각 부모 클래스의 해당 연산 호출
    def addRear( self, item ):
       self.enqueue(item )

    def deleteFront( self ):
       return self.dequeue()	# 원형 큐의 해당 연산 결과 반환

    def getFront( self ):
       return self.peek()	# 원형 큐의 해당 연산 결과 반환

    # 새로 구현이 필요한 연산들
    def addFront( self, item ):
        if not self.isFull():
            self.array[self.front] = item   # 전단 삽입은 덱이 포화상태가 아닌 경우 처리 가능
            self.front = (self.front - 1 + self.capacity) % self.capacity   # 현재 front에 새로운 요소 저장 후 반시계방향 회
        else: pass

    def deleteRear( self ):
        if not self.isEmpty():
            item = self.array[self.rear];   # 후단 삭제는 공백이 아닌경우 처리가능
            self.rear = (self.rear - 1 + self.capacity) % self.capacity # 현재 rear에 요소 저장 후 rear를 반시계방향으로 회전 후 마지막으로 저장했던 요소 반환
            return item
        else: pass

    def getRear( self ): 
        if not self.isEmpty():
            return self.array[self.rear]    # 후단 참조는 현재의 rear요소 반환
        else: pass
