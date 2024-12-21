def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

start_calculation = True
number1 = -1
number2 = -1
use_existing_result = False

while start_calculation:
    if not use_existing_result:
        number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    operation = input("Enter the operation to perform: +, -, *, /\n")
    result = operation_dict.get(operation).__call__(number1, number2)
    print(result)
    perform_calculation = input("Do you want to continue calculation: True, False ")
    if perform_calculation.lower() == "true":
        start_calculation = True
    else:
        start_calculation = False
    if start_calculation:
        user_response_use_existing_result = input("Do you want to use existing result")
        if user_response_use_existing_result.lower() == "true":
            use_existing_result = True
            number1 = result
        else:
            use_existing_result = False

print("Thanks for computing")
