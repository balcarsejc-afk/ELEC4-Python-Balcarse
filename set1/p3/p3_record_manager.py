# Full name: JC Argel Balcarse
# Section: IV-BSIT-A
# Activity: P3 - Student Record Manager
# Date: 2026-11-19
# Note: Taglish comments ang guide para madaling balikan ang logic.


def add_student(student_list, name):
    clean_name = name.strip()
    if not clean_name:
        print("Hindi puwedeng blank ang pangalan.")
        return
    # Set comprehension na naka-casefold para Juan Cruz at juan cruz ay duplicate.
    existing_names = {student.casefold() for student in student_list}
    if clean_name.casefold() in existing_names:
        print("Existing na ang student. Hindi dinagdag.")
    else:
        student_list.append(clean_name)
        print(clean_name, "successfully added.")

def remove_student(student_list, name):
    # Hanapin ang original spelling kahit iba ang capitalization.
    for student in student_list:
        if student.casefold() == name.strip().casefold():
            student_list.remove(student)
            print(student, "removed.")
            return
    print("Student not found.")

def search_student(student_list, keyword):
    matches = [student for student in student_list if keyword.casefold() in student.casefold()]
    if matches:
        print("Search results:")
        for student in matches:
            print("-", student)
    else:
        print("Walang match.")

def display_students(student_list):
    if not student_list:
        print("Wala pang student records.")
        return
    # sorted() ay nagpapakita ng alphabetical order nang hindi binabago ang original list.
    ordered = sorted(student_list, key=str.casefold)
    print(f"\nTotal students: {len(ordered)}")
    for number, student in enumerate(ordered, start=1):
        print(f"{number}. {student}")

def main():
    # List ang pangunahing storage; puwedeng magdagdag at magtanggal.
    students = ["Mika Santos", "Paolo Reyes", "Aira Mendoza"]
    while True:
        print("\n=== P3 STUDENT RECORD MANAGER ===")
        print("1 Add | 2 Remove | 3 Search | 4 Display | 5 Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            add_student(students, input("Student name: "))
        elif choice == "2":
            remove_student(students, input("Name to remove: "))
        elif choice == "3":
            search_student(students, input("Partial/full name: "))
        elif choice == "4":
            display_students(students)
        elif choice == "5":
            break
        else:
            print("Invalid menu choice.")

if __name__ == "__main__":
    main()

# Ang list ay ordered at puwedeng magkaroon ng duplicate, kaya dito ko ini-store ang student records.
# Ang set naman ay collection ng unique values, kaya ginamit ko ito sa duplicate checking.
# Casefold() ang tumutulong para hindi maging magkaiba ang Juan Cruz at juan cruz.
# List pa rin ang ginagamit sa display dahil kailangan nating mapanatili ang mismong student names.
