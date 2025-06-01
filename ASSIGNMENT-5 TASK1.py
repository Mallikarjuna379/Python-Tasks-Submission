STUDENTS = {
    'Alice': 85,
    'Arjuna': 100,
    'Sreeleela': 9,
    'TUTEDUDE': 5
}

name = input("Enter the student's name: ")

if name in STUDENTS:
    print(name + "'s marks are", STUDENTS[name])
else:
    print("Student not found")
