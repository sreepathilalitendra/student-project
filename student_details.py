students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    student = {
        "Name": name,
        "Roll": roll,
        "Marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")


def display_students():
    if not students:
        print("No student records found.\n")
    else:
        print("\nStudent Records:")
        print("-------------------")
        for student in students:
            print(f"Name: {student['Name']}")
            print(f"Roll: {student['Roll']}")
            print(f"Marks: {student['Marks']}")
            print("-------------------")


def delete_student():
    roll = input("Enter roll number to delete: ")
    for student in students:
        if student["Roll"] == roll:
            students.remove(student)
            print("Student deleted successfully!\n")
            return
    print("Student not found.\n")


while True:
    print("===== Student Record Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")