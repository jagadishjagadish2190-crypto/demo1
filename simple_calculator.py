# calculator.py

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")

    if num2 == 0:
        print("Division by zero is not allowed.")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")

if __name__ == "__main__":
    calculator()
