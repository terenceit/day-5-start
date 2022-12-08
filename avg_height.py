# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
height_sum = 0
num_students = 0

for heights in student_heights:
    height_sum += heights  #Add the next height in the list
    num_students += 1  #Keep track of loop count

avg = round(height_sum / num_students)  #Take average of heights and round up
print(avg)
