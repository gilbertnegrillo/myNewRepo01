num1 = float(input("Enter a number: "))
arithmetic_operator = input("Enter an arithmetic  operator: ")
num2 = float(input("Enter a second number: "))

if arithmetic_operator == "+": # addition
    print(num1 + num2)
elif arithmetic_operator == "-": # subtraction
    print(num1 - num2)
elif arithmetic_operator == "/": # division
    print(num1 / num2)
elif arithmetic_operator == "//": # floor division
    print(num1 // num2)
elif arithmetic_operator == "%": # modulus division
    print(num1 % num2)
elif arithmetic_operator == "*": # multiplication
    print(num1 * num2)
elif (arithmetic_operator) == "**": # exponentiation
    print(num1 ** num2)
else:
    print("Invalid operator")