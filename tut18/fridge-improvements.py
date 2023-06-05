# Fridge
# Use triple pair of strings for multi-line strings or comments

temperature_c = input("Enter temperature in Celsius:")

temperature_c = float(temperature_c)

# Using Constants to group all the strings to one place
STATUS_BROKEN = "Fridge is broken"
STATUS_OK = "Fridge OK"
STATUS_COLD = "Fridge too cold" 
STATUS_WARM = "Fridge too warm"

status = STATUS_BROKEN

if temperature_c < 0.0:
    status = STATUS_COLD
elif temperature_c <= 4.0:
    status = STATUS_OK
elif temperature_c < 6.0:
    status = STATUS_WARM

print(status)
