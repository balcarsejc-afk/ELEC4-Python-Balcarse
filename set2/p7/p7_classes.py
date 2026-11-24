# Full name: JC Argel Balcarse
# Section: IV-BSIT-A
# Activity: P7 - Student Management System with Classes
# Date: 2026-11-19
# Note: Taglish comments ang guide para madaling balikan ang logic.


class Subject:
    def __init__(self, code, title):
        self.code = code
        self.title = title

    def describe(self):
        return f"{self.code} - {self.title}"

class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.__grade = 0.0  # Private attribute; method ang kontrol sa pagbabago.
        self.set_grade(grade)

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        # Validation para hindi makapaglagay ng grade outside 0-100.
        if not isinstance(new_grade, (int, float)) or not 0 <= new_grade <= 100:
            print("Invalid grade. Dapat 0 hanggang 100.")
            return False
        self.__grade = float(new_grade)
        return True

    def update_name(self, new_name):
        if new_name.strip():
            self.name = new_name.strip()

    def display(self):
        print(f"{self.student_id} | {self.name} | Grade: {self.get_grade():.2f}")

class Section:
    def __init__(self, section_name, subject):
        self.section_name = section_name
        self.subject = subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        print(f"\nSection {self.section_name} — {self.subject.describe()}")
        for student in self.students:
            student.display()

def main():
    programming = Subject("IT401", "Application Development")
    class_section = Section("IV-BSIT-A", programming)

    first = Student("26-101", "Mika Santos", 89)
    second = Student("26-102", "Paolo Reyes", 92)
    third = Student("26-103", "Aira Mendoza", 86)

    class_section.add_student(first)
    class_section.add_student(second)
    class_section.add_student(third)

    print("Before update:")
    class_section.list_students()

    print("\nUpdating records...")
    second.update_name("Paolo R. Reyes")
    third.set_grade(90)

    print("\nAfter update:")
    class_section.list_students()


if __name__ == "__main__":
    main()
