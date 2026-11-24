# Full name: JC Argel Balcarse
# Section: IV-BSIT-A
# Activity: P2 - Custom Module student_utils
# Date: 2026-11-19
# Note: Taglish comments ang guide para madaling balikan ang logic.


def calculate_average(grades):
    # Ibalik ang average para magamit ng ibang file.
    return sum(grades) / len(grades) if grades else 0

def is_passing(grades, passing_grade=75):
    return calculate_average(grades) >= passing_grade

def highest_grade(grades):
    return max(grades) if grades else None

def lowest_grade(grades):
    return min(grades) if grades else None

if __name__ == "__main__":
    # Quick test lang kapag direktang ni-run ang module.
    print("student_utils module is ready.")
