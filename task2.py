
# University Scholarship Allocation System

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details for Student", i + 1)

    name = input("Student name: ")
    roll_no = input("Roll number: ")

    aggregate = float(input("Aggregate marks (%): "))

    subject1 = float(input("Subject 1 marks (%): "))
    subject2 = float(input("Subject 2 marks (%): "))
    subject3 = float(input("Subject 3 marks (%): "))

    attendance = float(input("Attendance (%): "))
    income = float(input("Annual family income (Rs.): "))

    # Eligibility criteria
    eligible = (
        aggregate >= 75
        and subject1 >= 60
        and subject2 >= 60
        and subject3 >= 60
        and attendance >= 75
        and income <= 250000
    )

    if eligible:
        students.append({
            "name": name,
            "roll_no": roll_no,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

# Rank eligible students
# Tie-breaking rules:
# 1. Higher aggregate marks
# 2. Higher attendance
# 3. Lower family income
# 4. Roll number in ascending order

students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        s["roll_no"]
    )
)

# Display results
print("\n===== SCHOLARSHIP RESULTS =====")

if not students:
    print("No students are eligible for the scholarship.")
else:
    print("\nEligible Students Ranked by Merit:")

    for rank, student in enumerate(students, start=1):
        print("\nRank:", rank)
        print("Name:", student["name"])
        print("Roll Number:", student["roll_no"])
        print("Aggregate Marks:", student["aggregate"], "%")
        print("Attendance:", student["attendance"], "%")
        print("Annual Family Income: Rs.", student["income"])
        print("Status: Eligible")
