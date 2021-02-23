print("What is the highest score?")
student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

x = (sorted(student_scores)[-1])
print(f"The highest score in the class is: {x}")

