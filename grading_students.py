def before_rounding():
    grades = []
    n = int(input("How many students?: "))
    for _ in range(n):
        grade_item = int(input("note: ?"))
        grades.append(grade_item)
    return grades


def gradingStudents(grades):
    """
    :param grades: list of student's note
    :return: list new grades after rounding
    """
    for index, value in enumerate(grades):
        if value >= 38:
            next_item = value
            while next_item % 5 != 0:
                next_item += 1
            if next_item - value < 3:
                grades[index] = next_item
    return grades


if __name__ == '__main__':
    grades = before_rounding()
    result = gradingStudents(grades)
    print(result)
