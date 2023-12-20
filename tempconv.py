
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Let's convert Celsius to Fahrenheit
celsius = float(input("Enter the temperature in Celsius: "))
converted_temp = celsius_to_fahrenheit(celsius)
print(f"The temperature in Fahrenheit is: {converted_temp}°F")

# Let's convert Fahrenheit to Celsius
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
converted_temp = fahrenheit_to_celsius(fahrenheit)
print(f"The temperature in Celsius is: {converted_temp}°C")
