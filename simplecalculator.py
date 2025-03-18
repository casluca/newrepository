#step 1 ask user to input first number
num1 = float(input("Enter first number: "))
#step 2 ask user to input second number
num2 =float(input("Enter second Number: "))

#step 3 ask user to input the operation
operation = input("Enter operation (+, -, *, /): ")
#add 2 numbers
#step 4 perform the operation and display result
if operation == "+":
    sum_result = num1 + num2
    print(f"{num1} + {num2}= {sum_result}")
elif operation == "-":
    difference_result = num1 - num2
    print(f"{num1} - {num2}= {difference_result}")

elif operation == "*":
    product_result = num1 * num2
    print(f"{num1} * {num2}= {product_result}")
elif operation == "/":
        if num2 == 0:
            quotient_result = num1 / num2
            print(f"{num1} / {num2}={quotient_result}")
        else:
            print("Error: Division by zero is not allowed.")