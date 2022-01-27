#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def before_rounding():
    grades = []
    n = int(input("How many students?: "))
    for _ in range(n):
        grade_item = int(input("note: ?"))
        grades.append(grade_item)
    return grades


def gradingStudents(grades):
    # Write your code here
    for index, value in enumerate(grades):
        if value >= 38:
            next_item = value
            while next_item%5 != 0:
                next_item +=1
            if next_item - value < 3:
                grades[index] = next_item
    return grades
if __name__ == '__main__':
    grades = before_rounding()
    result = gradingStudents(grades)
    print(result)
