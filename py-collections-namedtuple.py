from collections import namedtuple

n = int(input())
tuple_fields = input().split()
Student = namedtuple('Student', tuple_fields)
students = []
while n > 0:
    fields = list(input().split())
    students.append(Student(*fields))
    n -= 1
marks_sum = 0

for student in students:
    marks_sum += int(student.MARKS)

print(marks_sum / len(students))
