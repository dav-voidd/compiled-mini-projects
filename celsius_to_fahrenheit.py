# Celsius and Fahrenheit Calculator
print("Celsius and Fahrenheit Calculator")
user_input = input("Type 'C' for Celsius or 'F' for Fahrenheit: ").upper().strip()

if user_input == 'C':
    amount = float(input("Amount of Celsius: "))
    fahrenheit = amount * 1.8 + 32
    print(f"Celsius is now converted. {fahrenheit}°F")
elif user_input == 'F':
    amount1 = float(input("Amount of Fahrenheit: "))
    celsius = (amount1 - 30) / 2
    print(f"Fahrenheit is now converted. {celsius}°C")
else:
    print("Invalid")

