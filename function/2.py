def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
