student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score >=90:
        student_grades[student] = 'A'
    elif 70<score<90:
        student_grades[student] = 'B'
    elif 60<=score<70:
        student_grades[student] = 'C'
    else:
        student_grades[student] = 'D'

print(student_grades)