from database.Course import Course
from database.Student import Student
from database.StudentsCourses import StudentsCourses
from database.database import Database

db = Database('school.db')

student_manager = Student(db)
course_manager = Course(db)
students_courses_manager = StudentsCourses(db)

while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Оновити інформацію про студента")
    print("8. Оновити інформацію про курс")
    print("9. Вийти")

    choice = input("Оберіть опцію (1-9): ")

    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))
        major = input("Major: ")
        student_manager.add_student(name, age, major)
        # Додавання нового студента

    elif choice == "2":
        name = input("Course name: ")
        instructor = input("Instructor: ")
        course_manager.add_course(name, instructor)
        # Додавання нового курсу

    elif choice == "3":
        # Показати список студентів
        students = student_manager.get_students()
        for student in students:
            print(student)

    elif choice == "4":
        # Показати список курсів
        courses = course_manager.get_courses()
        for course in courses:
            print(course)

    elif choice == "5":
        # Зареєструвати студента на курс
        course_id = int(input("Course_id: "))
        student_id = int(input("Student_id: "))
        students_courses_manager.add_students_courses(course_id, student_id)

    elif choice == "6":
        # Показати студентів на конкретному курсі
        course_id = int(input("Course_id: "))
        students_by_course_id = students_courses_manager.get_students_by_course_id(course_id)
        for student_course in students_by_course_id:
            student = student_manager.get_student(student_course[2])  # Заміна student_course['student_id'] на student_course[2]
            print(student)

    elif choice == "7":
        # Оновити інформацію про студента
        student_id = int(input("Student ID: "))
        name = input("New Name (leave empty to skip): ")
        age = input("New Age (leave empty to skip): ")
        major = input("New Major (leave empty to skip): ")
        student_manager.update_student(student_id, name=name if name else None, age=int(age) if age else None, major=major if major else None)

    elif choice == "8":
        # Оновити інформацію про курс
        course_id = int(input("Course ID: "))
        course_name = input("New Course Name (leave empty to skip): ")
        instructor = input("New Instructor (leave empty to skip): ")
        course_manager.update_course(course_id, course_name=course_name if course_name else None, instructor=instructor if instructor else None)

    elif choice == "9":
        break

    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 9.")