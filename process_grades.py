PASSING_AVERAGE = 60


def process_grades(students):
    passed = []
    failed = []

    for student in students:
        average = sum(student['grades']) / len(student['grades'])
        if average >= PASSING_AVERAGE:
            passed.append(student['name'])
        else:
            failed.append(student['name'])

    return {'passed': passed, 'failed': failed}
