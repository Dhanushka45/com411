# Counting odd and even numbers

print("Please enter first whole number")

first_number = int(input())

print("Please enter first whole number")

second_number = int(input())

print("Please enter third whole number")

third_number = int(input())

odd = 0
even = 0

if first_number % 2 == 0 :
    odd += 1
else:
    even += 1

if second_number % 2 == 0 :
    odd += 1
else:
    even += 1

if third_number % 2 == 0 :
    odd += 1
else:
    even += 1

print(f"There were {even} even numbers and {odd} odd numbers")




