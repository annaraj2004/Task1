def add(x, y):
    return int(x + y)

def subtract(x, y):
    return int(x - y)

def multiply(x, y):
    return int(x * y)

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"


def calculator():
    print("BASIC CALCULATOR")
    print("OPERATIONS:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    memory = 0

    while True:
        operation = input("Enter the operation (1/2/3/4/5): ")

        if operation in ["1", "2", "3", "4"]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

        if operation == "1":
            result = add(num1, num2)
        elif operation == "2":
            result = subtract(num1, num2)
        elif operation == "3":
            result = multiply(num1, num2)
        elif operation == "4":
            result = divide(num1, num2)
        elif operation == "5":
            print("Thank you for using the calculator")
            break
        else:
            print("Invalid operation. Please enter a valid option.")
            continue

        print(f"Result: {result}")
        memory = result

if __name__ == "__main__":
    calculator()
