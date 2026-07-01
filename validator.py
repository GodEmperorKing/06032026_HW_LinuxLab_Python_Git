import sys

print("[LOG - PYTHON]: Inside py1/validator.py subsystem context.")

try:
    Name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    ### Operational Logic & Conditionals
    if age >= 18 and age < 40:
        print(f"[LOG - OUTPUT]: {Name}, You are an adult.")
    elif age >= 40:
        print(f"[LOG - OUTPUT]: {Name}, You are middle-aged.")
    else:
        print(f"[LOG - OUTPUT]: {Name}, You are a minor.")

except ValueError:
    print("[ERROR - PYTHON]: Input validation failed. Age must be an integer.")
    sys.exit(1)
