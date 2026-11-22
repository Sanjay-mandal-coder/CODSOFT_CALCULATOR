"""A simple command-line calculator for basic arithmetic."""


def read_number(prompt: str) -> float:
    """Prompt until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    first = read_number("Enter the first number: ")
    second = read_number("Enter the second number: ")

    print("\nChoose an operation:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    operation = input("Operation (+, -, *, /): ").strip()

    if operation == "+":
        result = first + second
    elif operation == "-":
        result = first - second
    elif operation == "*":
        result = first * second
    elif operation == "/":
        if second == 0:
            print("Error: division by zero is not allowed.")
            return
        result = first / second
    else:
        print("Invalid operation. Choose +, -, *, or /.")
        return

    print(f"Result: {first:g} {operation} {second:g} = {result:g}")


if __name__ == "__main__":
    main()
