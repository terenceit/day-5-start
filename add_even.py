#Write your code below this row 👇

#Variable for total
total = 0

# #For every 2 numbers in the range starting from zero
# for number in range(0, 101, 2):
#     total += number #Add that number to the total
# print(total)

#For each number in range
for number in range(0, 101): 
    if number % 2 == 0: #Check if it is evenly divisible by 2
        total += number
print(total)