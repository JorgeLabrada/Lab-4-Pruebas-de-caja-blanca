import pytest
import process_grades



@pytest.mark.parametrize("students, expected", [
    ([{'name': 'Ana', 'grades': [60, 60, 60]}], ['Ana']),
])
def test_process_grades_passed(students, expected):
    result = process_grades.process_grades(students)
    assert result['passed'] == expected

@pytest.mark.parametrize("students, expected", [
    ([{'name': 'Marta', 'grades': [40, 45, 50]}], ['Marta']),
])
def test_process_grades_failed(students, expected):
    result = process_grades.process_grades(students)
    assert result['failed'] == expected 