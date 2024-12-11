import random
target=random.randint(1,5)
n=int(input("guess the no. between 1 to 5"))
while n!=target:
    if n<target:
        print("no. guessed is less than target")
    elif n>target:
        print("no. guessed is greater than target")
    n=int(input("guess again : "))
print("you have guessed correctly")
print("game over")

        
