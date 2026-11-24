# Full name: JC Argel Balcarse
# Section: IV-BSIT-A
# Activity: P1 - Student Grade Calculator
# Date: 2026-11-19
# Note: Taglish comments ang guide para madaling balikan ang logic.


def get_grades():
    """Kumuha ng grades at siguraduhing 0 hanggang 100 lang."""
    grades = []
    while True:
        raw = input("Ilagay ang grade (type done kapag tapos): ").strip()
        if raw.lower() == "done":
            if grades:
                return grades
            print("Maglagay muna ng kahit isang grade.")
            continue
        try:
            grade = float(raw)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Grade dapat mula 0 hanggang 100.")
        except ValueError:
            print("Number lang o 'done' ang puwede.")

def calculate_average(grades):
    # Average ang total ng grades hati sa dami.
    return sum(grades) / len(grades)

def get_highest(grades):
    return max(grades)

def get_lowest(grades):
    return min(grades)

def get_status(grades, passing_grade=75):
    # Gumagamit ng average para malaman kung pasado.
    return "PASSED" if calculate_average(grades) >= passing_grade else "FAILED"

def show_results(grades):
    # Dito lang nagpi-print; ang computing functions ay return lang.
    print("\n--- GRADE REPORT ---")
    print(f"Average: {calculate_average(grades):.2f}")
    print(f"Highest: {get_highest(grades):.2f}")
    print(f"Lowest: {get_lowest(grades):.2f}")
    print(f"Status: {get_status(grades)}")

def main():
    # Local variable ang grades dahil nasa loob lang ito ng main().
    grades = []
    while True:
        print("\n=== P1 GRADE CALCULATOR ===")
        print("1. Enter grades")
        print("2. View results")
        print("3. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            grades = get_grades()
        elif choice == "2":
            if grades:
                show_results(grades)
            else:
                print("Wala pang grades. Piliin muna ang option 1.")
        elif choice == "3":
            print("Salamat! Bye.")
            break
        else:
            print("Invalid choice. Piliin ang 1, 2, o 3.")

if __name__ == "__main__":
    main()

# Local variable ang grades sa loob ng main() dahil doon lang ito direktang ginagamit.
# Hindi ito awtomatikong nakikita sa ibang function; ipinapasa natin ito bilang parameter.
# Ang global variable naman ay nasa labas ng functions at maaaring basahin sa iba't ibang function.
# Sa program na ito, hindi kailangan ng global variable dahil mas malinaw ang parameter passing.
