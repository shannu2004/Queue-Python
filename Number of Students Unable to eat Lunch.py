from collections import deque
def countStudents(students,sandwiches):
    students=deque(students)
    count=0
    while students:
        if students[0]==sandwiches[0]:
            students.popleft()
            sandwiches.pop(0)
            count=0
        else:
            students.append(students.popleft())
            count+=1

        if count==len(students):
            break
    return len(students)

students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
remaining_students = countStudents(students, sandwiches)
print(remaining_students)
