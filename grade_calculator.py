# Grade Calculator

homework = float(input("Enter homework average: "))
quiz = float(input("Enter quiz average: "))
test = float(input("Enter test average: "))

# Calculate weighted average
overall_grade = homework * 0.2 + quiz * 0.3 + test * 0.5

print("\nOverall grade:", round(overall_grade, 1))

# Determine letter grade
if overall_grade >= 93:
    print("Letter grade: A")
elif overall_grade >= 90:
    print("Letter grade: A-")
elif overall_grade >= 87:
    print("Letter grade: B+")
elif overall_grade >= 83:
    print("Letter grade: B")
elif overall_grade >= 80:
    print("Letter grade: B-")
elif overall_grade >= 77:
    print("Letter grade: C+")
elif overall_grade >= 73:
    print("Letter grade: C")
elif overall_grade >= 70:
    print("Letter grade: C-")
else:
    print("Letter grade: F")