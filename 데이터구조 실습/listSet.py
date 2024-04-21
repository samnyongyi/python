# setA는 사용자가 입력하는 집합, setC는 임시로 사용하는 집

 class ArraySet:
    def __init__( self, capacity=100 ):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    def isEmpty( self ):
       return self.size == 0

    def isFull( self ):
       return self.size == self.capacity

    def __str__( self ) :
        return str(self.array[0:self.size])

    def contains(self, e) :	
        for i in range(self.size) :	# 시간 복잡도는 O(n)
            if self.array[i] == e :
                return True
        return False

    def insert(self, e) :
        if not self.contains(e) and not self.isFull() :	# 시간 복잡도는 최소 O(n)
           self.array[self.size] = e
           self.size += 1
        else : pass

    def delete(self, e) :
        for i in range(self.size) :	# 최악의 경우 시간 복잡도는 O(n)
            if self.array[i] == e :
                self.array[i] = self.array[self.size-1]
                self.size -= 1

    def union( self, setB ):
        setC = ArraySet()
        for i in range(self.size) :	# 시간 복잡도는 O(n^2)
            setC.insert(self.array[i])
        for i in range(setB.size) :
            if not setC.contains(setB.array[i]) :
                setC.insert(setB.array[i])
        return setC

    def intersect( self, setB ):            
        setC = ArraySet()
        for i in range(setB.size) :	# 시간 복잡도는 O(n^2)
            if self.contains(setB.array[i]) :
                setC.insert(setB.array[i])
        return setC

    def difference( self, setB ):            
        setC = ArraySet()
        for i in range(self.size) :	# 시간 복잡도는 O(n^2)
            if not setB.contains(self.array[i]) :
                setC.insert(self.array[i])
        return setC

    def __eq__( self, setB ):
        if self.size != setB.size :
            return False
        for i in range(self.size) :
            if not setB.contains(self.array[i]) :
                return False
        return True
