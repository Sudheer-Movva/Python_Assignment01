class Stack(list):
    def __init__(self):
        super(Stack,self).__init__()
    
    def is_Empty(self):
        return len(self)==0
    
    def peek(self):
        return self[len(self)-1]
    
    def push(self,value):
        self.append(value)
    
    def pop(self):
        if self.is_Empty():
            return ''
        else:
            temp = self[len(self)-1] 
            self.remove(self[len(self)-1])
            return temp
    def get_Size(self):
        return len(self)

def main():
    stack = Stack()
    for i in range(5):
        strng = input("Please enter a string:")
        stack.push(strng)
    print("Popping elements of stack ")
    while not stack.is_Empty():
        print(stack.pop())
    print("Size of the stack after popping : "+str(stack.get_Size()))
    
main()