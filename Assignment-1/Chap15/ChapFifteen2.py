
def fib(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    elif index >=2 :
        prev = 1
        prev_to_prev = 0
        for num in range(2,index+1):
            current = prev + prev_to_prev
            prev_to_prev = prev
            prev = current
        return current
    
input_index = eval(input("Enter an index: "))
print("The Fibonacci number for index ",input_index," is ",fib(input_index))