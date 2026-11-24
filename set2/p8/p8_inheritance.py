# Full name: JC Argel Balcarse
# Section: IV-BSIT-A
# Activity: P8 - Inheritance and Polymorphism
# Date: 2026-11-19
# Note: Taglish comments ang guide para madaling balikan ang logic.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, ako si {self.name}, {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, course, year_level):
        super().__init__(name, age)  # Kunin ang shared name at age setup ng parent.
        self.course = course
        self.year_level = year_level

    def introduce(self):
        # Override: student-specific ang introduction.
        print(f"Student ako na si {self.name}, {self.course}, Year {self.year_level}.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        # Same method name pero teacher-specific ang output.
        print(f"Teacher ako na si {self.name}; nagtuturo ako ng {self.subject}.")

def main():
    people = [
        Person("Jc Balcarse", 20),
        Student("Mika Santos", 21, "BSIT", 4),
        Teacher("Rina Lopez", 35, "Python")
    ]
    # Polymorphism: iisang method call, pero iba ang output depende sa object.
    for person in people:
        person.introduce()

if __name__ == "__main__":
    main()

# Inheritance ang paggamit ng Student at Teacher sa common attributes at methods ng Person.
# Tinawag nila ang super().__init__() para ma-set ang name at age mula sa parent class.
# Polymorphism naman ang makikita dahil pare-parehong introduce() ang tinatawag sa isang list.
# Iba ang output dahil bawat child class ay may sariling overridden version ng introduce().
