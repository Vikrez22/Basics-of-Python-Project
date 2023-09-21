#1.  Write a program that calculates the average student height from a List of heights.
# d avg. height can be calc. by add.. all d heig.. 2gether and  / by the total number of heights.
# solution starts

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
# total_height = 0
# for height in student_heights:
#     total_height += height
#
#
# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
#
# average_height = round(total_height / number_of_students)
# print(average_height)

# solution ends

# 2. Write a program that calculates the highest score from a list of scores.
# solution start

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The Highest score in the class is: {highest_score}")

# solution ends


# 3. add 1 to 100 using code. ans= 5050
# solution starts
total = 0
for number in range(1, 101):
    total += number
print(total)