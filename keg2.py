class keg2:

    def __init__(self, size):
        self.maxSize = size
        self.queueArray = [None] * self.maxSize
        self.front = 0
        self.rear = -1
        self.size = 0

    def add(self, value):
        if self.isFull():
            print("Queue is full")
            return
        self.rear += 1
        self.queueArray[self.rear] = value
        self.size += 1

    def offer(self, value):
        if self.isFull():
            print("Queue is full")
            return
        if self.rear == self.maxSize - 1:
            self.rear = -1
        self.rear += 1
        self.queueArray[self.rear] = value
        self.size += 1

    def remove(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        value = self.queueArray[self.front]
        self.front += 1
        if self.front == self.maxSize:
            self.front = 0
        self.size -= 1
        return value

    def poll(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        value = self.queueArray[self.front]
        self.front += 1
        if self.front == self.maxSize:
            self.front = 0
        self.size -= 1
        return value

    def element(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.queueArray[self.front]

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.queueArray[self.front]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.maxSize

    def _str_(self):
        result = "["
        if not self.isEmpty():
            result += str(self.queueArray[self.front])
            for i in range(self.front + 1, self.rear + 1):
                result += ", " + str(self.queueArray[i])
        result += "]"
        return result
az = keg2(4)
az.add("Java")
az.add("DotNet")
az.offer("PHP")
az.offer("HTML")


print("Remove: " + az.remove())
print("Element: " + az.element())
print("Poll: " + az.poll())
print("Peek: " + az.peek())