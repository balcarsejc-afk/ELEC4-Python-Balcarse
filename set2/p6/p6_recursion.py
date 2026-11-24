# Full name: JC Argel Balcarse
# Section: IV-BSIT-A
# Activity: P6 - Recursion Toolkit
# Date: 2026-11-19
# Note: Taglish comments ang guide para madaling balikan ang logic.


def factorial(n):
    # Base case: 0! at 1! ay 1. Recursive call: n * factorial(n-1).
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    # Base cases: F(0)=0 at F(1)=1. Recursive call: F(n-1)+F(n-2).
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def sum_numbers(n):
    # Base case: kapag 0, zero ang sum. Recursive call: n + sum_numbers(n-1).
    if n <= 0:
        return 0
    return n + sum_numbers(n - 1)

def search(items, target, index=0):
    # Base case: lampas na sa list, ibig sabihin walang nahanap.
    if index >= len(items):
        return False
    # Recursive call: check ang next index kung hindi match ang current item.
    if items[index] == target:
        return True
    return search(items, target, index + 1)

def main():
    while True:
        print("\n=== P6 RECURSION TOOLKIT ===")
        print("1 Factorial | 2 Fibonacci | 3 Sum 1..n | 4 Search list | 5 Exit")
        choice = input("Choice: ").strip()
        try:
            if choice == "1":
                n = int(input("Non-negative integer: "))
                if n < 0: raise ValueError
                print("Factorial:", factorial(n))
            elif choice == "2":
                n = int(input("How many terms (1-12): "))
                if not 1 <= n <= 12: raise ValueError
                print("First terms:", [fibonacci(i) for i in range(n)])
            elif choice == "3":
                n = int(input("Positive integer: "))
                if n < 0: raise ValueError
                print("Sum:", sum_numbers(n))
            elif choice == "4":
                items = input("Enter words separated by comma: ").split(",")
                target = input("Target word: ").strip()
                print("Found:", search([item.strip() for item in items], target))
            elif choice == "5":
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Sundin ang hinihinging integer/range.")

if __name__ == "__main__":
    main()
