# Write a program that calculates your current grade in a course with 5 categories of assignments:
# Quizzes, Projects, Activities, Attendance, Exams

student_name = input("Enter the student's name: ")
course_name = input("Enter the name of the course: ")

quizzes_weight = float(input("\nEnter the quizzes weight (the weights of the 5 areas must total to 1): "))
projects_weight = float(input("Enter the projects weight: "))
activities_weight = float(input("Enter the activities weight: "))
attendance_weight = float(input("Enter the attendance weight: "))
exams_weight = float(input("Enter the exams weight: "))

quizzes_average = float(input("\nEnter the quizzes average (a number between 0 and 1): "))
projects_average = float(input("Enter the projects average: "))
activities_average = float(input("Enter the activities average: "))
attendance_average = float(input("Enter the attendance average: "))
exams_average = float(input("Enter the exams average: "))

current_grade = ((quizzes_weight * quizzes_average) + (projects_weight * projects_average) + (activities_weight *
                                                                                              activities_average) +
                 (attendance_weight * attendance_average) + (exams_weight * exams_average)) * 100

print("\nHi", student_name, ",")
print("You have a", current_grade, "% in your", course_name, "class.")
