 # 단순연결노드 클래스
 class Node:
    def __init__ (self, elem, link=None):   # link는 디폴트 값으로 None을 사용
        self.data = elem    # 노드의 데이터 
        self.link = link    # 다음 노드를 가리키는 링크

 # 연결된 스택 클래스
 class LinkedStack :
    def __init__( self ):   # 연결된 스택의 생성자
        self.top = None # 시작노드를 가리키는 top

    def isEmpty( self ):
        return self.top == None # 공백상태는 top이 None인 경우

   # def isFull(self): return False  # 포화 상태는 의미 없으므로 항상 False 반환
    
    def push( self, item ):
        self.top = Node(item, self.top) # 요소 e를 사용하여 노드를 생성후 링크를 top로 연결

    def peek( self ):
        if not self.isEmpty():  # 공백이 아닐경우
            return self.top.data    # 머리노드의 데이터 반환

    def pop( self ):    # 삭제연산, 공백검사 선행 필
        if not self.isEmpty():
            data = self.top.data    
            self.top = self.top.link
            return data

    # 연결된 스택의 전체 요소의 수 계산
    def size( self ):
        node = self.top
        count = 0
        while not node == None :
            node = node.link
            count += 1

    # 문자열 변환을 위한 str 연산자 중복
    def __str__(self):
        arr = []	# 요소들을 저장할 공백 리스트 준비
        node = self.top
        while not node == None :
            arr.append(node.data)	# 각 노드의 데이터를 리스트에 추가
            node = node.link	
        return str(arr)	# 리스트를 문자열로 변환하여 반환
