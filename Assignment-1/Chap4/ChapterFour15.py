import random
lottery_num = random.randint(99,1000)

guess = eval(input("Enter a three-digit number:"))

guess_Int1 = guess%10
guess_Int3 = guess//100
guess_Int2 = (guess//10)%10

lottery_Num1 = lottery_num%10
lottery_Num3 = lottery_num//100
lottery_Num2 = (lottery_num//10)%10

match_count=0

if(guess_Int1==lottery_Num1 or guess_Int1 == lottery_Num2 or guess_Int1 == lottery_Num3):
    match_count +=1
    
if(guess_Int2==lottery_Num1 or guess_Int2 == lottery_Num2 or guess_Int2 == lottery_Num3):
    match_count +=1
if(guess_Int3==lottery_Num1 or guess_Int3 == lottery_Num2 or guess_Int3 == lottery_Num3):
    match_count +=1

print("randomly generated lottery number:",lottery_num)
print(str(match_count))

if(lottery_num == guess):
    print("Congratulations!! you have won $10,000")
elif(match_count == 3):
    print("Congratulations !! you have won $3,000")
elif(match_count>=1):
    print("congratulations!! you have won $1,000")
else:
    print("Better luck next time")