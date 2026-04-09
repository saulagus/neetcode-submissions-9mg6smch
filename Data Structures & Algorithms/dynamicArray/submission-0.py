class DynamicArray:

    def __init__(self, capacity: int):
        if capacity > 0: 
            self.capacity = capacity
            self.size = 0
            self.data = [None] * capacity

    def get(self, i: int) -> int:
        if i < 0 or i >= self.size:
            raise Exception("Invalid Size") 
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self.size:
            raise Exception("Invalid size")
        self.data[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size == 0:
            raise Exception("Empty array")
        n = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return n
 

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_arr = [None] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.data[i]
        self.data = new_arr

    def getSize(self) -> int:
        return self.size
    def getCapacity(self) -> int:
        return self.capacity
