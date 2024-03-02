import re

students = []
courses = []
marks = {}

def is_valid_date_format(date):
    date_pattern = r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$"  # MM/DD/YYYY format
    return re.match(date_pattern, date) is not None

def input_number_of_students():
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            if num_students < 0:
                print("Number of students should be a positive integer. Please try again.")
            else:
                return num_students
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def input_student_info():
    num_students = input_number_of_students()
    for _ in range(num_students):
        while True:
            student_id = input("Enter student ID: ")
            student_name = input("Enter student's name: ")
            student_dob = input("Enter student's DoB (Date of Birth) in MM/DD/YYYY format: ")

            if not is_valid_date_format(student_dob):
                print("Invalid date format. Please enter the date in MM/DD/YYYY format.")
            else:
                students.append({"id": student_id, "name": student_name, "DoB": student_dob})
                break

def input_number_of_courses():
    while True:
        try:
            num_courses = int(input("Enter the number of courses: "))
            if num_courses < 0:
                print("Number of courses should be a positive integer. Please try again.")
            else:
                return num_courses
        except:
            print("Invalid input. Please enter a valid number.")

def input_course_info():
    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append({"id": course_id, "name": course_name})

def select_course_and_input_marks():
    while True:
        course_id = input("Enter the ID of course to input marks: ")
        if course_id not in [course['id'] for course in courses]:
            print("Invalid course ID. Please try again.")
        else:
            break
    marks[course_id] = []
    for student in students:
        while True:
            try:
                mark = float(input(f"Enter mark for student {student['name']} (ID: {student['id']}): "))
                # Additional validation for marks can be added here
                marks[course_id].append((student['id'], mark))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

def list_courses():
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def list_students():
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['DoB']}")

def show_student_marks_for_course():
    course_id = input("Enter the course ID to show marks: ")
    if course_id in marks:
        for student_id, mark in marks[course_id]:
            student_name = next(student['name'] for student in students if student['id'] == student_id)
            print(f"Student: {student_name}, Mark: {mark}")
    else:
        print("No marks recorded for this course.")

def main():
    while True:
        print("\n1. Input student information")
        print("2. Input course information")
        print("3. Input marks for a course")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks for a course")
        print("7. Exit")
        
        choice = input("Select your choice: ")

        if choice == '1':
            input_student_info()
        elif choice == '2':
            input_course_info()
        elif choice == '3':
            select_course_and_input_marks()
        elif choice == '4':
            list_courses()
        elif choice == '5':
            list_students()
        elif choice == '6':
            show_student_marks_for_course()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()