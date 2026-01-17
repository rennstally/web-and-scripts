def calculate(a, b, operation):

    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "invalid operation"
    

op = input("choose operation (add, subtract, multiply, divide):").lower()

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = calculate(num1, num2, op)
print("Result:", result)