# Full name: JC Argel Balcarse
# Section: IV-BSIT-A
# Activity: P5 - Student Information File System
# Date: 2026-11-19
# Note: Taglish comments ang guide para madaling balikan ang logic.


from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.txt")

def load_records():
    records = []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.rstrip("\n").split("|")
                if len(parts) == 4:
                    records.append({"id": parts[0], "name": parts[1], "section": parts[2], "average": parts[3]})
    except FileNotFoundError:
        # Normal lang sa first run kung wala pang data file.
        pass
    return records

def save_records(records):
    # 'w' para i-save ang latest complete list ng records.
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        for item in records:
            file.write(f"{item['id']}|{item['name']}|{item['section']}|{item['average']}\n")

def add_record(records):
    student_id = input("Student ID: ").strip()
    if any(item["id"] == student_id for item in records):
        print("May kaparehong ID na.")
        return
    full_name = input("Full name: ").strip()
    course_section = input("Course/Section: ").strip()
    try:
        average = float(input("General average: "))
        if not 0 <= average <= 100:
            raise ValueError("Average must be from 0 to 100.")
    except ValueError:
        print("Invalid average. Walang record na na-save.")
        return
    records.append({"id": student_id, "name": full_name, "section": course_section, "average": f"{average:.2f}"})
    save_records(records)
    print("Record added and saved.")

def display_records(records):
    if not records:
        print("No student records yet.")
        return
    for item in records:
        print(f"{item['id']} | {item['name']} | {item['section']} | {item['average']}")

def search_record(records):
    wanted = input("Student ID to search: ").strip()
    for item in records:
        if item["id"] == wanted:
            print(item)
            return
    print("Student ID not found.")

def update_record(records):
    wanted = input("Student ID to update: ").strip()
    for item in records:
        if item["id"] == wanted:
            new_name = input(f"New name [{item['name']}]: ").strip()
            new_section = input(f"New course/section [{item['section']}]: ").strip()
            new_average = input(f"New average [{item['average']}]: ").strip()
            try:
                if new_average:
                    value = float(new_average)
                    if not 0 <= value <= 100:
                        raise ValueError
                    item["average"] = f"{value:.2f}"
            except ValueError:
                print("Invalid average; walang binagong record.")
                return
            if new_name:
                item["name"] = new_name
            if new_section:
                item["section"] = new_section
            save_records(records)
            print("Record updated and saved.")
            return
    print("Student ID not found.")

def main():
    records = load_records()
    while True:
        print("\n=== P5 STUDENT FILE SYSTEM ===")
        print("1 Add | 2 Display all | 3 Search by ID | 4 Update | 5 Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            add_record(records)
        elif choice == "2":
            display_records(records)
        elif choice == "3":
            search_record(records)
        elif choice == "4":
            update_record(records)
        elif choice == "5":
            print("Records are stored in", DATA_FILE.name)
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
