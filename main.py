import art
import replit


def add(num1, num2):
    return num1 + num2


def substraction(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divition(num1, num2):
    return num1 / num2


operations = {"+": add, "-": substraction, "*": multiply, "/": divition}


def calculator():
    print(art.logo)

    first_num = int(input("What's the first number: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("pick an operation : ")
        next_num = int(input("What's the next number: "))

        final_function = operations[operation_symbol]
        answer = final_function(first_num, next_num)
        print(f"{first_num} {operation_symbol} {next_num} = {answer}")

        if input(f"Do you want to continue another operation with {answer}: "
                 ) == "y":
            first_num = answer
        else:
            replit.clear()
            calculator()


calculator()
