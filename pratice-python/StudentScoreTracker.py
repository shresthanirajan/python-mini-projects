students = {
    "Alex": [80, 90, 75],
    "Maya": [95, 88, 92],
    "Sam": [70, 65, 80]
}
def calculate_average(grades):
    average = sum(grades) / len(grades)
    return average

def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def student_status(average):
    if average >= 70:
        return "Pass"
    else:
        return "Fail"

highest_average = 0
highest_student = ""
for name, grade in students.items():
    average = calculate_average(grade)
    letter_grade = get_letter_grade(average)
    students_status = student_status(average)
    print(
        f"Student Name: {name} | "
        f"Average Grade: {round(average, 2)} | "
        f"Letter Grade: {letter_grade} | "
        f"Status: {students_status}"
    )



    if  average > highest_average:
        highest_average = average
        highest_student = name

print(f"highest_student: {highest_student}, highest_average: {round(highest_average,2)}")




