def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")
    age=input("Enter the age: ")
    dob=input("Enter date of birth: ")

    with open("students.txt", "a") as file:
        file.write(f"{name},{roll},{marks},{age},{dob}\n")
    
    print(" Student added successfully!\n")

def view_students():
    try:
        with open("students.txt", "r") as file:
            records = file.readlines()
            
            if not records:
                print(" No student records found.\n")
                return

            print("\n Student Records:")
            print("-" * 30)
            for record in records:
                name, roll, marks, age, dob = record.strip().split(",")
                print(f"Name : {name}")
                print(f"Roll : {roll}")
                print(f"Marks: {marks}")
                print(f"Age : {age}")
                print(f"Date Of Birth : {dob}")
                print("-" * 30)

    except FileNotFoundError:
        print(" 'students.txt' file not found. Add students first.\n")

def delete_student():
    roll_to_delete = input("Enter roll number of the student to delete: ")
    found = False

    with open("students.txt", "r") as file:
        lines = file.readlines()

    with open("students.txt", "w") as file:
        for line in lines:
            name, roll, marks,age,dob = line.strip().split(",")
            if roll != roll_to_delete:
                file.write(line)
            else:
                found = True

    if found:
        print(f" Student with Roll No {roll_to_delete} deleted successfully.\n")
    else:
        print(f" No student found with Roll No {roll_to_delete}.\n")

def update_student():
    roll_to_update = input("Enter roll number of the student to update: ")
    found = False

    with open("students.txt", "r") as file:
        lines = file.readlines()

    with open("students.txt", "w") as file:
        for line in lines:
            name, roll, marks, age, dob = line.strip().split(",")
            if roll == roll_to_update:
                print("Enter new details (leave blank to keep current):")
                new_name = input(f"New name (current: {name}): ") or name
                new_roll = input(f"New roll number (current: {roll}): ") or roll
                new_marks = input(f"New marks (current: {marks}): ") or marks
                new_age = input(f"New age (current: {age}): ") or age
                new_dob = input(f"New DOB (current: {dob}): ") or dob

                file.write(f"{new_name},{new_roll},{new_marks},{new_age},{new_dob}\n")
                found = True
            else:
                file.write(line)

    if found:
        print(f"Student with Roll No {roll_to_update} updated successfully.\n")
    else:
        print(f"No student found with Roll No {roll_to_update}.\n")

while True:
    print("\nStudent Record Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Update Student Details")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        print(" Exiting ")
        break
    else:
        print(" Invalid choice. Please enter 1, 2, 3, 4, or 5.")
