import random
import math
lower_range=int(input("Enter a lower range:"))
upper_range=int(input("Enter a upper range:"))
x=random.randint(lower_range,upper_range)
print("you have only",round(math.log(upper_range-lower_range+1,2)),"chance to guess the number")
count=0
while count<math.log(upper_range-lower_range+1,2):
    count+=1
    guess=int(input("Guess the number:"))
    if x==guess:
        print("Congrats your guessing is right ")
        break
    elif x>guess:
        print("your guessing is too small please give high number")
    elif x<guess:
        print("your guessing is too high please give small number")
    if count>=math.log(upper_range-lower_range+1,2):
        print(x)
        print("Good luck for next time")