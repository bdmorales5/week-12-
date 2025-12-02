# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

# Ask the user for today's temperature
temperature = float(input("What is the temperature today? "))

# Check for extreme temperatures
if temperature < -10 or temperature > 110:
    print("Extreme temperature warning!")

# Check if it's cold, warm, or hot
if temperature < 50:
    print("It is cold.")
elif temperature < 80:
    print("It is warm.")
else:
    print("It is hot.")