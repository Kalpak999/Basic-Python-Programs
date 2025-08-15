# Combined Program: Temperature Converter + Calculator

def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit:.2f}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius:.2f}°C")
    else:
        print("Invalid choice!")


def calculator():
    print("\nSimple Calculator")
    print("Operations: +, -, *, /")

    num1 = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operation."

    print("Result:", result)


# Main menu
while True:
    print("\n--- Main Menu ---")
    print("1. Temperature Converter")
    print("2. Calculator")
    print("3. Exit")

    main_choice = input("Enter your choice (1-3): ")

    if main_choice == "1":
        temperature_converter()
    elif main_choice == "2":
        calculator()
    elif main_choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
