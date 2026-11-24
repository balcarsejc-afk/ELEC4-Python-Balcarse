# Full name: JC Argel Balcarse
# Section: IV-BSIT-A
# Activity: P4 - Safe Menu Program with Exceptions
# Date: 2026-11-19
# Note: Taglish comments ang guide para madaling balikan ang logic.


def divide_numbers():
    try:
        first = float(input("First number: "))
        second = float(input("Second number: "))
        answer = first / second
    except ValueError:
        print("Invalid number: digits/decimal number lang ang ilagay.")
    except ZeroDivisionError:
        print("Hindi puwedeng mag-divide sa zero.")
    else:
        # Tatakbo lang ang else kapag walang exception.
        print(f"Result: {answer}")
    finally:
        # Laging tatakbo ang finally, successful man o may error.
        print("Tapos na ang division attempt.")

def read_text_file():
    filename = input("File name: ").strip()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("Hindi makita ang file:", filename)
    except PermissionError:
        print("Walang permission para basahin ang file.")
    else:
        print("\n--- FILE CONTENTS ---")
        print(content if content else "(Empty file)")
    finally:
        print("File operation finished.")

def main():
    while True:
        print("\n=== P4 SAFE MENU ===")
        print("1. Divide two numbers")
        print("2. Open a text file")
        print("3. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            divide_numbers()
        elif choice == "2":
            read_text_file()
        elif choice == "3":
            print("Program closed safely.")
            break
        else:
            print("Invalid menu selection. Piliin ang 1, 2, o 3.")

if __name__ == "__main__":
    main()
