
class Stack(list):
    def __init__(self):
        super().__init__()
        
    def isEmpty(self):
        if super().len((self.__elements)) == 0:
            return True
        else:
            return False
        
    def peek(self):
        return self.__elements[super().len((self.__elements))-1]
        
    def push(self,value):
        self.__elements.super().append(value)
        
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements.super().pop()
        
    def getSize(self):
        return super.len((self.__elements))


input_list = input("Enter five strings: ")
strings = input_list.split()
print(strings)
s1 = Stack()
for each in strings:
    s1.push(each)

while not s1.isEmpty():
    print(s1.pop(),end = " ")