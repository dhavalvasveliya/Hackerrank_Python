n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

def outputKeyPair(student_marks):
    for names in student_marks:
        if query_name == names:
            result = sum(student_marks[names])/len(student_marks[names])
            print(result)

outputKeyPair(student_marks)