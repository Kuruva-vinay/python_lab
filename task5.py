# Convert temperature between Celsius and Fahrenheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Input temperature and conversion choice
temp = float(input("Enter the temperature: "))
choice = input("Convert to (F)ahrenheit or (C)elsius? ").strip().upper()

if choice == 'F':
    converted_temp = celsius_to_fahrenheit(temp)
    print(f"{temp}°C is equal to {converted_temp}°F")
elif choice == 'C':
    converted_temp = fahrenheit_to_celsius(temp)
    print(f"{temp}°F is equal to {converted_temp}°C")
else:
    print("Invalid choice. Please enter 'F' or 'C'.")
