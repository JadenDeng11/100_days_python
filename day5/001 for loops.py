student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height=0
for total in student_heights:
    total_height += total


lenght=0
for leng in student_heights:
    lenght += 1

print(f"the average height is: {round(total_height/lenght,0)}")

