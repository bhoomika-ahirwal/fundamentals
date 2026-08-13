num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
num_3 = float(input("Enter third number: "))

if num_1 >= num_2 and num_1 >= num_3:
    largest = num_1
elif num_2 >= num_1 and num_2 >= num_3:
    largest = num_2
else:
    largest = num_3

print("Largest number =", largest)