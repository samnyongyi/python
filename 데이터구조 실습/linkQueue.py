 # LinkedQueue.py
 class Node:
    def __init__ (self, elem, next=None):
        self.data = elem 
        self.link = next

 # 원형으로 연결된 큐 클래스
 class LinkedQueue:
    def __init__( self ):
        self.tail = None

    def isEmpty( self ): return self.tail == None
    def isFull( self ): return False

    def enqueue( self, item ):
        node = Node(item, None)
        if self.isEmpty() :
           self.tail = node
           node.link = node
        else :
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node

    def dequeue( self ):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail : self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data

    def peek( self ):
        if not self.isEmpty():
            return self.tail.link.data

    # 원형으로 연결된 큐의 요소의 수 계산
    def size( self ):
        if self.isEmpty() : return 0
        else :
            count = 1
            node = self.tail.link
            while not node == self.tail :
                node = node.link
                count += 1
            return count

    # 문자열 변환을 위한 str 연산자 중복
    def __str__( self ):
        arr = []
        if not self.isEmpty() :
            node = self.tail.link	# node는 front노드
            while not node == self.tail :	# 반복문 종료 조건
                arr.append(node.data)	# 노드의 데이터를 리스트에 추가
                node = node.link	# 다음 노드로 진행
            arr.append(node.data)	# 마지막으로 rear의 데이터 추가
        return str(arr)	# 리스트를 문자열로 변환해 반환
