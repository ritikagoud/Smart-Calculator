print("=" * 30)
print("     SMART CALCULATOR")
print("=" * 30)

try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    print("\nAvailable Operations:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("%  Modulus")
    print("// Floor Division")
    print("** Power")

    o = input("\nEnter Operation: ")

    match o:
        case "+":
            print(f"Result: {a + b}")

        case "-":
            print(f"Result: {a - b}")

        case "*":
            print(f"Result: {a * b}")

        case "/":
            if b == 0:
                print("Cannot divide by zero.")
            else:
                print(f"Result: {a / b}")

        case "%":
            print(f"Result: {a % b}")

        case "//":
            print(f"Result: {a // b}")

        case "**":
            print(f"Result: {a ** b}")

        case _:
            print("Invalid operation selected.")

except ValueError:
    print("Please enter valid numbers.")
