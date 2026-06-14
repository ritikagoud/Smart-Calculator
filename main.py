print("=" * 30)
print("     SMART CALCULATOR")
print("=" * 30)

history = []
while True:
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
        print("history  View Calculation History")

        o = input("\nEnter Operation: ")
        if o == "history":
            if len(history) == 0:
                print("No calculations yet.")
            else:
                print("\nCalculation History:")
                for item in history:
                    print(item)

            continue

        match o:
            case "+":
                result = a + b
                print(f"Result: {result}")
                history.append(f"{a} + {b} = {result}")

            case "-":
                result = a - b 
                print(f"Result: {result}")
                history.append(f"{a} - {b} = {result}")

            case "*":
                result = a * b
                print(f"Result: {result}")
                history.append(f"{a} * {b} = {result}")

            case "/":
                if b == 0:
                    print("Cannot divide by zero.")
                else:
                    result = a / b
                    print(f"Result: {result}")
                    history.append(f"{a} / {b} = {result}")

            case "%":
                result = a % b
                print(f"Result: {result}")
                history.append(f"{a} % {b} = {result}")

            case "//":
                result = a // b
                print(f"Result: {result}")
                history.append(f"{a} // {b} = {result}")

            case "**":
                result = a ** b
                print(f"Result: {result}")
                history.append(f"{a} ** {b} = {result}")

            case _:
                print("Invalid operation selected.")

    except ValueError:
        print("Please enter valid numbers.")
    choice = input("\nDo another calculation? (y/n): ")
    if choice.lower() == "n":
        break
