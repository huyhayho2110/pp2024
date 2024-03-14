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

    def add_marks(self, course_id, student_id, mark):
        if course_id not in self.marks:
            self.marks[course_id] = []
        self.marks[course_id].append((student_id, mark))

    def show_marks_for_course(self, course_id):
        if course_id in self.marks:
            for student_id, mark in self.marks[course_id]:
                student_name = next(student.name for student in self.students if student.id == student_id)
                print(f"Student: {student_name}, Mark: {mark}")
        else:
            print("No marks recorded for this course.")

    def input_students_info(self):
        number_students = self._input_number("students")
        for i in range(1, number_students + 1):
            id_student = input(f"Enter student {i} id: ")
            name_student = input(f"Enter student {i} name: ")
            dob_student = self._input_dob()
            self.add_student(Student(id_student, name_student, dob_student))

    def input_courses_info(self):
        number_courses = self._input_number("courses")
        for i in range(1, number_courses + 1):
            id_course = input(f"Enter the id of course {i}: ")
            name_course = input(f"Enter the name of course {i}: ")
            self.add_course(Course(id_course, name_course))

    def input_marks(self):
        while True:
            check_course_id = input("Enter the course id of course to input marks or 'q' to quit: ")
            if check_course_id == 'q':
                break
            elif check_course_id not in [course.id for course in self.courses]:
                print(f"The course with id {check_course_id} does not exist")
            else:
                for student in self.students:
                    while True:
                        try:
                            mark = float(input(f"Enter mark for student: {student.name}, ID: {student.id} "))
                            if 0 <= mark <= 20:
                                self.add_marks(check_course_id, student.id, mark)
                                break
                            else:
                                print("Invalid mark. Please enter a mark between 0 and 20.")
                        except ValueError:
                            print("Please enter a valid mark.")

    def list_courses(self):
        for course in self.courses:
            print(f"ID: {course.id}, Name: {course.name}")

    def list_students(self):
        for student in self.students:
            print(f"ID: {student.id}, Name: {student.name}")

    def _input_number(self, item):
        while True:
            try:
                number = int(input(f"Enter the number of {item}: "))
                if number <= 0:
                    print(f"Number of {item} must be positive.")
                else:
                    return number
            except ValueError:
                print("Please enter a valid integer.")

    def _input_dob(self):
        while True:
            dob = input("Enter DoB, follow format: MM/DD/YYYY: ")
            if re.match(r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$", dob):
                return dob
            else:
                print("Please enter in the format: MM/DD/YYYY")

    def menu(self):
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
                self.input_students_info()
            elif choice == '2':
                self.input_courses_info()
            elif choice == '3':
                self.input_marks()
            elif choice == '4':
                self.list_courses()
            elif choice == '5':
                self.list_students()
            elif choice == '6':
                course_id = input("Enter the course ID to show marks: ")
                self.show_marks_for_course(course_id)
            else:
                break

if __name__ == "__main__":
    mark_sheet = MarkSheet()
    mark_sheet.menu()
