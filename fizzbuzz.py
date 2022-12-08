#Write your code below this row 👇

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0: #If the number is divisible by both 3 and 5
        print("FizzBuzz")
    elif number % 3 == 0: #If the number is only divisible by 3
        print("Fizz")
    elif number % 5 == 0: #If the number is only divisible by 5
        print("Buzz")
    else:
        print(number) #If the number is not divisible by 3 or 5