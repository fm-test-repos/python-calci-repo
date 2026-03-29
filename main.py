from calculator.operations import add, subtract, multiply, divide


def main():
    print("Simple Calculator")
    print("------------------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose operation (1/2/3/4): ")

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            result = add(a, b)

        elif choice == "2":
            result = subtract(a, b)

        elif choice == "3":
            result = multiply(a, b)

        elif choice == "4":
            result = divide(a, b)

        else:
            print("Invalid option selected.")
            return

        print("Result:", result)

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
