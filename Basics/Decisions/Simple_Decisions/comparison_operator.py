# Comparing numbers

print("Please enter the first number")

first_number = int(input())

print("Please enter the second number")

second_number = int(input())

if first_number>second_number:
    print(f"{first_number} is greater than {second_number}")
elif first_number<second_number:
    print(f"{first_number} is less than {second_number}")
else:
    print("Numbers are equal")
