import sys
read = sys.stdin.readline

grade_dict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
         'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F':0.0}

total_score = 0
total_credit = 0

for _ in range(20):
    subject, credit, grade = read().split()

    if grade == 'P':
        continue

    credit = float(credit)
    total_credit += credit
    total_score += credit * grade_dict[grade]

avg_grade = total_score / total_credit

print(f"{avg_grade:.6f}")