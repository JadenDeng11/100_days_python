student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

hightest_score=0
for score in student_scores:
    if score>hightest_score:
        hightest_score=score

print(hightest_score)