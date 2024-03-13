import re

list_student = []
list_course = []
dict_mark = {}

def DoB_format(date):
    date_pattern = r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$"  # MM/DD/YYYY format
    return re.match(date_pattern, date) is not None
    
def number_student():
    while True:
        try:
            number_student_ver1 = int(input("Enter the number of students: "))
            if number_student_ver1 <= 0:
                print("Number of students must be positive.")
            else:
                return number_student_ver1
        except ValueError:
            print("Please enter a valid integer.")

def info_students():
    number_students = number_student()
    for i in range(1,number_students + 1):
        id_student = input(f"Enter student {i} id: ")
        name_student = input(f"Enter student {i} name: ")
        while True:
            try:
                DoB_student = input("Enter DoB, follow format: MM/DD/YYYY: ")
                if not DoB_format(DoB_student):
                    print("Please enter in the format: MM/DD/YYYY")
                else:
                    list_student.append({'id': id_student, 'name': name_student, 'DoB': DoB_student})
                    break
            except ValueError:
                print("Please try again")

def number_course():
    while True:
        try:
            number_courses = int(input("Enter the number of courses: "))
            if number_courses <= 0:
                print("Number of courses must be positive")
            else:
                return number_courses
        except ValueError:
            print("Please try again")

def info_courses():
    infor_course = number_course()
    for i in range(1, infor_course + 1):
        id_course = input(f"Enter the id of course {i}: ")
        name_course = input(f"Enter the name of course {i}: ")
        list_course.append({"id": id_course, "name": name_course})

def select_and_input_marks_in_course():
    while True:
        try:
            check_course_id = input("Enter the course id of course to input marks or 'q' to quit: ")
            if check_course_id == 'q':
                break
            elif check_course_id not in [i['id']for i in list_course]:
                print(f"The course with id {check_course_id} does not exist")
            else:
                dict_mark[check_course_id] = []
                for student in list_student:
                    while True:
                        mark = float(input(f"Enter mark for student: {student['name']}, ID: {student['id']} "))
                        if 0 <= mark <= 20:
                            dict_mark[check_course_id].append((student['id'], mark))  
                            break
                        else:
                            print("Invalid mark. Please enter a mark between 0 and 20.")
        except ValueError:
            print("Please enter mark between 0 and 20")


def list_courses():
    for i in list_course:
        print(f"ID: {i['id']}, Name: {i['name']}")

def list_students():
    for i in list_student:
        print(f"ID: {i['id']}, Name: {i['name']}")

def Show_student_marks_for_course():
    course_id = input("Enter the course ID to show marks: ")
    if course_id in dict_mark:
        for student_id, mark in dict_mark[course_id]:
            student_name = next(student['name'] for student in list_student if student['id'] == student_id)
            print(f"Student: {student_name}, Mark: {mark}")
    else:
        print("No marks recorded for this course.")
            
def main(): 
    while True:
        print("\n1. Input information of student")
        print("2. Input information of course")
        print("3. Select course and input mark for student")
        print("4. List course")
        print("5. List student")
        print("6. Show student matks for a given course")
        print("Other. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            info_students()
        elif choice =='2':
            info_courses()
        elif choice == '3':
            select_and_input_marks_in_course()
        elif choice == '4':
            list_courses()
        elif choice == '5':
            list_students()
        elif choice == '6':
            Show_student_marks_for_course()
        else:
            break
if __name__ == "__main__":
    main()