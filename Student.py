import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    try:
        marks = float(marks)
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100!")
            return
    except ValueError:
        print("Please enter valid marks!")
        return

    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "marks": marks
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No student records found!")
        return

    for student in students:
        print("\nStudent ID:", student["id"])
        print("Name:", student["name"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])


def search_student(students):
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])
            return

    print("Student not found!")


def update_student(students):
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter new name: ")
            student["course"] = input("Enter new course: ")

            try:
                marks = float(input("Enter new marks: "))
                if not 0 <= marks <= 100:
                    print("Marks must be between 0 and 100!")
                    return
                student["marks"] = marks
            except ValueError:
                print("Invalid marks!")
                return

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found!")


def delete_student(students):
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found!")


def main():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
          
