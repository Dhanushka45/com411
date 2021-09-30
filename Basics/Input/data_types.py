# Adding age, mass and height.
# Calculating BMI

user_name = str(input())

user_age = int(input())

user_height = float(input())

user_mass = float(input())

user_bmi = user_mass/user_height**2

print(f"Your name is {user_name}")

print(f"Your age is {user_age}")

print(f"Your height (in meters) is {user_height}")

print(f"Your mass (in kilograms) is {user_mass}")

print(f"{user_name} you are {user_age} years old and your BMI is {user_bmi}")