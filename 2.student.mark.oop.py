import re

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class MarkSheet:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def input_marks(self):
        while True:
            try:
                check_course_id = input("Enter the course id of course to input marks or 'q' to quit: ")
                if check_course_id == 'q':
                    break
                elif check_course_id not in [course.id for course in self.courses]:
                    print(f"The course with id {check_course_id} does not exist")
                else:
                    self.marks[check_course_id] = []
                    for student in self.students:
                        while True:
                            mark = float(input(f"Enter mark for student: {student.name}, ID: {student.id} "))
                            if 0 <= mark <= 20:
                                self.marks[check_course_id].append((student.id, mark))
                                break
                            else:
                                print("Invalid mark. Please enter a mark between 0 and 20.")
            except ValueError:
                print("Please enter mark between 0 and 20")

    def list_courses(self):
        for course in self.courses:
            print(f"ID: {course.id}, Name: {course.name}")

    def list_students(self):
        for student in self.students:
            print(f"ID: {student.id}, Name: {student.name}")

    def show_student_marks_for_course(self):
        course_id = input("Enter the course ID to show marks: ")
        if course_id in self.marks:
            for student_id, mark in self.marks[course_id]:
                student_name = next(student.name for student in self.students if student.id == student_id)
                print(f"Student: {student_name}, Mark: {mark}")
        else:
            print("No marks recorded for this course.")

def DoB_format(date):
    date_pattern = r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$"  # MM/DD/YYYY format
    return re.match(date_pattern, date) is not None

def main():
    mark_sheet = MarkSheet()
    
    while True:
        print("\n1. Input information of student")
        print("2. Input information of course")
        print("3. Select course and input mark for student")
        print("4. List course")
        print("5. List student")
        print("6. Show student marks for a given course")
        print("Other. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            id_student = input("Enter student ID: ")
            name_student = input("Enter student name: ")
            dob_student = input("Enter student date of birth (MM/DD/YYYY): ")
            if DoB_format(dob_student):
                student = Student(id_student, name_student, dob_student)
                mark_sheet.add_student(student)
            else:
                print("Please enter the date of birth in MM/DD/YYYY format")
        elif choice == '2':
            id_course = input("Enter course ID: ")
            name_course = input("Enter course name: ")
            course = Course(id_course, name_course)
            mark_sheet.add_course(course)
        elif choice == '3':
            mark_sheet.input_marks()
        elif choice == '4':
            mark_sheet.list_courses()
        elif choice == '5':
            mark_sheet.list_students()
        elif choice == '6':
            mark_sheet.show_student_marks_for_course()
        else:
            break

if __name__ == "__main__":
    main()
