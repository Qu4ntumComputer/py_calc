import sys
import sympy as sp
import re
import math
from rich.console import Console
from rich.text import Text


console = Console()
console.clear()

superscript_map = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

def to_superscript(exp):
    return str(exp).translate(superscript_map)

def format_with_superscript(expression):
    expression = re.sub(r'\*\*(\d+)', lambda match: to_superscript(match.group(1)), expression)
    return expression

def replace_multiplication_symbol(expression):
    return expression.replace('*', '⋅')

def format_exponents(expression):
    return re.sub(r'\^(\d+)', lambda match: to_superscript(match.group(1)), expression)

def integral_calc():
    x = sp.symbols('x')

    print("Input example:   f(x) = 3x^2 + 4x\n\n")

    original_function = input("f(x) = ")

    function = original_function.replace('^', '**')
    function = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', function)

    try:
        math_expr = sp.sympify(function)
        integral = sp.integrate(math_expr, x)

        integral_syntax = str(integral)
        integral_syntax = format_with_superscript(integral_syntax)
        integral_syntax = replace_multiplication_symbol(integral_syntax)

        formatted_original = format_exponents(original_function)

        print(f"\nThe undefined integral of f(x) = {formatted_original} is:\n")
        print(f"f(x) = {integral_syntax} + c\n\n")
    except Exception as e:
        print(f"Error while calculating: {e}")
    
    return main()

def addition():
    try:
        num1 = float(input("\nFirst Summand: "))
        num2 = float(input("Second Summand: "))
        Sum = num1 + num2
        console.print(f'\n\nThe result is: {Sum}\n\n', style="underline yellow")
    except ValueError:
        print("Invalid input, try again.")
    
    return main()

def subtraktion():
    try:
        num1 = float(input("\nMinuend: "))
        num2 = float(input("Subtrahend: "))
        Diff = num1 - num2
        console.print(f'\n\nThe result is: {Diff}\n\n', style="underline yellow")
    except ValueError:
        print("Invalid input, try again.")
    
    return main()

def multiply():
    try:
        num1 = float(input("\nFirst Factor: "))
        num2 = float(input("Second Factor: "))
        produkt = num1 * num2
        formatted_result = replace_multiplication_symbol(f"{produkt}")
        console.print(f'\n\nThe result is: {formatted_result}\n\n', style="underline yellow")
    except ValueError:
        print("Invalid input, try again.")
    
    return main()

def division():
    try:
        num1 = float(input("\nDividend: "))
        num2 = float(input("Divisor: "))
        if num2 == 0:
            print("\nUndefined (Error 0 division)\n")
        else:
            quotient = num1 / num2
            console.print(f'\n\nThe result is: {quotient}\n\n', style="underline yellow")
    except ValueError:
        print("Invalid input, try again.")
    
    return main()

def sqrt():
    try:
        num1 = float(input("\nEnter a number: "))
        squareroot = math.sqrt(num1)
        console.print(f'\n\nThe result is: {squareroot}\n\n', style="underline yellow")
    except ValueError:
        print("Invalid input, try again.")
    
    return main()

def exponent():
    try:
        base = float(input("\nBase: "))
        expo = float(input("Exponent: "))
        result = base ** expo
        
        if expo.is_integer():
            formatted_result = f"{base}{to_superscript(int(expo))} = {result}"
        else:
            formatted_result = f"{base}^{expo} = {result}"
        console.print(f'\n\nThe result is: {formatted_result}\n\n', style="underline yellow")
    except ValueError:
        print("Invalid input. Use numerical values.")
    
    return main()

def exit():
    print("\nProcess ended.\n\n")
    sys.exit()

def main():
    text = Text()
    
    t1 = text.append("\n\n----------------------------------------------------\n", style="bold red")
    t_space = text.append("                   ")
    t2 = text.append("0. Exit\n\n", style="bold underline2 red")

    t3 = text.append("[1.]", style="blue")
    text.append(" Addition               ", style="green")
    text.append("[8.]", style="blue")
    text.append(" ??\n", style="green")

    t4 = text.append("[2.]", style="blue")
    text.append(" Subtraction            ", style="green")
    text.append("[9.]", style="blue")
    text.append(" ??\n", style="green")

    t5 = text.append("[3.]", style="blue")
    text.append(" Multiplication        ", style="green")
    text.append("[10.]", style="blue")
    text.append(" ??\n", style="green")

    t6 = text.append("[4.]", style="blue")
    text.append(" Division              ", style="green")
    text.append("[11.]", style="blue")
    text.append(" ??\n", style="green")

    t7 = text.append("[5.]", style="blue")
    text.append(" Exponent              ", style="green")
    text.append("[12.]", style="blue")
    text.append(" ??\n", style="green")

    t8 = text.append("[6.]", style="blue")
    text.append(" Squareroot            ", style="green")
    text.append("[13.]", style="blue")
    text.append(" ??\n", style="green")

    t9 = text.append("[7.]", style="blue")
    text.append(" undefined Integrals", style="green")
    text.append("   [14.]", style="blue")
    text.append(" ??\n", style="green")

    t10 = text.append("\n----------------------------------------------------\n", style="bold red")

    console.print(text)

    try:
        operation = int(input("Select an Operation: "))
    except ValueError:
        print("Invalid input. Choose a number from the listet operations above.")
        return main()

    if operation == 0:
        exit()
    elif operation == 6:
        sqrt()
    elif operation == 7:
        integral_calc()
    elif operation == 1:
        addition()
    elif operation == 2:
        subtraktion()
    elif operation == 3:
        multiply()
    elif operation == 4:
        division()
    elif operation == 5:
        exponent()
    else:
        print("Error: Invalid Operation")
        return main()

main()
