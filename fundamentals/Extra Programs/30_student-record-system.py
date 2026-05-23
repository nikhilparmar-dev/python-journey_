students = []

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully.")


def view_students():
    if len(students) == 0:
        print("No student records found.")

    else:
        print("\n===== STUDENT RECORDS =====")

        for student in students:
            print(f"Name: {student['name']} | Marks: {student['marks']}")


def search_student():
    name = input("Enter student name to search: ").lower()

    found = False

    for student in students:
        if student["name"].lower() == name:
            print(f"Found -> Name: {student['name']}, Marks: {student['marks']}")
            found = True
            break

    if not found:
        print("Student not found.")


def topper_student():
    if len(students) == 0:
        print("No student records found.")

    else:
        topper = students[0]

        for student in students:
            if student["marks"] > topper["marks"]:
                topper = student

        print("\n===== TOPPER STUDENT =====")
        print(f"Name: {topper['name']}")
        print(f"Marks: {topper['marks']}")


while True:
    print("\n===== STUDENT RECORD SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Topper Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        topper_student()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")