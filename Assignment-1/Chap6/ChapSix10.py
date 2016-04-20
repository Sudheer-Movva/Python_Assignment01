
def isPrime(number):
    divisor = 2
    while divisor <= number // 2:
        if number % divisor == 0:
            return False
        divisor += 1
    
    return True

prime_count = 0

for number in range(2,10000):
    if isPrime(number):
        prime_count += 1
        
print("Number of prime number less than 10,000 is ", prime_count)