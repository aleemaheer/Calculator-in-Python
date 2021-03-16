# making a calculator in python
# this is very simple

num1 = int(input("Enter the first number: "))
operator = input("Enter the operator: ")
num2 = int(input("Enter the second number: "))

# making results

addition = num1 + num2
subtraction = num1 - num2
division = num1 / num2
multiplication = num1 * num2

# printing results with if statements

if operator == '+':
    print(addition)
elif operator == '-':
    print(subtraction)
elif operator == '/':
    print(division)
elif operator == '*':
    print(multiplication)
else:
    print("Invalid operator!")
