# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#Stores biggest number
big = 0
#Stores current number
num = 0

#Option 1
# for n in student_scores:
#     num = n #Num = number in list
#     if num < big: #If num is less than big, num will stay the same
#         num = num
#     elif num > big: #If num is greater than big, num will be new big
#         big = num
#     else:
#         num = num

#Option 2
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")