# Full name: JC Argel Balcarse
# Section: IV-BSIT-A
# Activity: P2 - Using Custom and Built-in Modules
# Date: 2026-11-19
# Note: Taglish comments ang guide para madaling balikan ang logic.


import datetime
import student_utils  # Import module style: tatawagin ang function gamit ang module name.
from student_utils import is_passing  # From-import style: direct function name ang gagamitin.

def main():
    grades = []
    print("P2 STUDENT REPORT")
    print("Name:", "JC Argel Balcarse")
    while True:
        raw = input("Grade (done to finish): ").strip()
        if raw.lower() == "done":
            break
        try:
            value = float(raw)
            if 0 <= value <= 100:
                grades.append(value)
            else:
                print("0 hanggang 100 lang ang valid.")
        except ValueError:
            print("Invalid number. Subukan ulit.")
    if not grades:
        print("Walang grades na na-enter.")
        return
    print("\n--- RESULT ---")
    print(f"Average: {student_utils.calculate_average(grades):.2f}")
    print("Highest:", student_utils.highest_grade(grades))
    print("Lowest:", student_utils.lowest_grade(grades))
    print("Status:", "PASSED" if is_passing(grades) else "FAILED")
    # Built-in datetime module para may report timestamp.
    print("Report generated:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    main()
