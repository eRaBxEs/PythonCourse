# Fridge
# Use triple pair of strings for multi-line strings or comments


"""

Get the user to enter a temperature in celsius.

< 0: Print "Fridge too cold"
0 - 4: Print "Fridge OK"
4 - 6: Print "Fridge too warm"
> 6: Print "Fridge broken"


"""

temperature_c = float(input("Enter temperature in Celsius:"))

if temperature_c < 0.0:
    print("Fridge too cold")
elif temperature_c <= 4.0:
    print("Fridge OK")
elif temperature_c < 6.0:
    print("Fridge too warm")
else:
    print("Fridge broken")
