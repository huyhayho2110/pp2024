import re

students = []
courses = []
marks = {}
def DoB_format(date):
    date_pattern = r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$"  # MM/DD/YYYY format
    return re.match(date_pattern, date) is not None

def input_number_students():
    while True:
        number_student_ver1 = int(input("Enter the number of student in a class: "))
        if number_student_ver1 < 0:
            print("Number of student must be a positive number")
        elif number_student_ver1 == 0:
            print("Number of student must be exist")
        else:
            return number_student_ver1
def input_student_info():
    number_student_ver2 = input_number_students()
    for i in range(1, number_student_ver2 + 1):
        student_id = input(f"Enter student ID for student {i}: ")
        student_name = input(f"Enter student name for student {i}: ")
        while True:
            student_DoB = input(f"Enter student DoB (Date of Birth) for student {i} in MM/DD/YYYY format: ")
            if not DoB_format(student_DoB):
                print("Wrong format. Please enter the DoB in MM/DD/YYYY format.")
            else:
                students.append({"ID": student_id, "Name": student_name, "DoB": student_DoB})
                break 

def input_course_number():
    while True:
        number_course_ver1 = int(input("Enter the number of course: "))
        if number_course_ver1 < 0:
            print("Number of course must be a positive number")
        elif number_course_ver1 == 0:
            print("Number of course must be exist")
        else:
            return number_course_ver1

def input_course_info():
    number_course_ver2 = input_course_number()
    for i in range(1, number_course_ver2 + 1):
        course_id = input(f"Enter course id for course {i}: ")
        course_name = input(f"Enter course name for course {i}: ")
        courses.append({"ID": course_id, "Name": course_name})
def select_course_and_input_marks():
    while True:
        course_id = input("Enter the ID of course to input marks (or 'q' to quit): ")
        if course_id == 'q':
            break
        elif course_id not in [i['ID'] for i in courses]:
            print(f"The course with id {course_id} does not exist")
        else:
            marks[course_id] = []
            for student in students:
                while True:
                    mark = float(input(f"Enter mark for student {student['Name']} (ID: {student['ID']}): "))
                    if 0 <= mark <= 20:
                        marks[course_id].append((student['ID'], mark))
                        break
                    else:
                        print("Invalid mark. Please enter a mark between 0 and 20.")
def list_courses():
    for course in courses:
        print(f"ID: {course['ID']}, Name: {course['Name']}")

def list_students():
    for student in students:
        print(f"ID: {student['ID']}, Name: {student['Name']}, DoB: {student['DoB']}")

def show_student_marks_for_course():
    course_id = input("Enter the course ID to show marks: ")
    if course_id in marks:
        for student_id, mark in marks[course_id]:
            student_name = next(student['Name'] for student in students if student['ID'] == student_id)
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
        
        choice = input("\nSelect your choice: ")

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
    
