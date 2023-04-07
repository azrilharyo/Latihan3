class keg1:
    def __init__(self, size):
        self.maxSize = size
        self.stackArray = [None] * self.maxSize
        self.top = -1

    def push(self, value):
        self.top += 1
        self.stackArray[self.top] = value

    def pop(self):
        value = self.stackArray[self.top]
        self.top -= 1
        return value

    def peek(self):
        return self.stackArray[self.top]

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.maxSize - 1

    def search(self, value):
        index = self.top
        while index >= 0:
            if self.stackArray[index] == value:
                return self.top - index + 1
            index -= 1
        return -1

az = keg1(5)
az.push("Aku")
az.push("Anak")
az.push("Indonesia")

print("Next : " + az.peek())
az.push("Raya")
print(az.pop())

count = az.search("Aku")
while count > 1:
    az.pop()
    count -= 1
print(az.pop())
print(az.isEmpty())