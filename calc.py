import sys
import sympy as sp
import re
import math
from rich.console import Console
from rich.text import Text
import numpy as np
from mpmath import mp


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

    COLOR = "yellow"

    YELLOW = "\033[33m"
    RESET = "\033[0m"

    print(f"{YELLOW}Input example: {RESET} f(x) = 3x² + 4x")
    console.print("You can also use a ^ sign to symbolize exponents.\n", style="yellow")

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
        console.print(f'\n\nThe result is: {Sum}\n\n', style="yellow")
    except ValueError:
        print("Invalid input, try again.")
    
    return main()

def subtraction():
    try:
        num1 = float(input("\nMinuend: "))
        num2 = float(input("Subtrahend: "))
        Diff = num1 - num2
        console.print(f'\n\nThe result is: {Diff}\n\n', style="yellow")
    except ValueError:
        print("Invalid input, try again.")
    
    return main()

def multiply():
    try:
        num1 = float(input("\nFirst Factor: "))
        num2 = float(input("Second Factor: "))
        produkt = num1 * num2
        formatted_result = replace_multiplication_symbol(f"{produkt}")
        console.print(f'\n\nThe result is: {formatted_result}\n\n', style="yellow")
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
            console.print(f'\n\nThe result is: {quotient}\n\n', style="yellow")
    except ValueError:
        print("Invalid input, try again.")
    
    return main()

def sqrt():
    try:
        num1 = float(input("\nEnter a number: "))
        squareroot = math.sqrt(num1)
        console.print(f'\n\nThe result is: {squareroot}\n\n', style="yellow")
    except ValueError:
        print("Invalid input, try again.")
    
    return main()

def exponent():
    try:

        base = float(input("\nBase: "))
        expo = float(input("Exponent: "))
        result = base ** expo
        
        if expo.is_integer():
            formatted_result = f"{base}{to_superscript(int(expo))} is {result}"
        else:
            formatted_result = f"{base}^{expo} = {result}"
        console.print(f'\n\nThe result of {formatted_result}\n\n', style="yellow")
    except ValueError:
        print("Invalid input. Use numerical values.")
    
    return main()


def logarithm():
    try:

        value = float(input("\n\nValue: "))
        base = float(input("Base: "))

        if value <= 0:
            console.print("Error, logarithm of negative numbers or 0 is not defined.", style="red")
        if base <= 0:
            console.print("Error, the base of a logarithm can't be equal or less than 0.", style="red")
        if base == 1:
            console.print("Error, the base of a logarithm can't be equal to 1.")

        result = math.log(value, base)

        console.print(f'\nThe result is: {result}', style="yellow")

    except ValueError:
        print("Invalid input. Use numerical values.")

    return main()

def factorial():
    try:
        value = int(input("\n\nFactorial Value: "))

        if value < 0:
            return "Faktorial ist für negative Zahlen nicht definiert."
        result = 1
        for i in range(2, value + 1):
            result *= i
        
        console.print(f'\n\nThe result is: {result}', style="yellow")


    except ValueError:
        print("Error, this function only accepts integer values. You will have to use the gamma function [11.] for non-integer factorials.")

    return main()


def matrix():
    try: 
        def matrix_input():
            m, n = map(int, input("\n\nEnter the amount of lines and columns of your matrix with a space between each value: ").split())
            print("")

            if m != n:
                print("\nThe inverse of your matrix does not exist. A matrix must be quadratic to have an inverse.")
                return None

            matrix = []

            for i in range(m):
                zeile = list(map(float, input(f"Enter the elements of the {i+1}. line of your matrix with a space between each value: ").split()))
                if len(zeile) != n:
                    print("\nError, wrong amount of lines. Try again.")
                    return None
                matrix.append(zeile)

            return np.array(matrix)

        def calc_matrix(matrix):
            try:
                inverse = np.linalg.inv(matrix)
                return inverse
            except np.linalg.LinAlgError:
                return matrix_input

        def format_matrix(matrix):
            m, n = matrix.shape
            for i, line in enumerate(matrix):
                if i == 0:
                    print("⌈", end="")
                    print(" ".join(f"{val:6.2f}" for val in line), end="")
                    print(" ⌉")
                elif i == m - 1:
                    print("⌊", end="")
                    print(" ".join(f"{val:6.2f}" for val in line), end="")
                    print(" ⌋")
                else:
                    print(" " + " ".join(f"{val:6.2f}" for val in line))

        matrix = matrix_input()

        if matrix is not None:

            inverse = calc_matrix(matrix)
            
            if isinstance(inverse, str):
                print(inverse)
            else:
                console.print("\n\nThe inverse of your matrix is: \n", style="yellow")
                format_matrix(inverse)

    except ValueError:
        print("Error, input values must be of the datatype 'float', try again")


    return main()




def gamma_function():

    def factorial_of_float(value, precision=50):
        if value.is_integer() and value <= 0:
            raise ValueError("Gamma function is not defined for non-positive integers.")
        
        mp.dps = precision 

        gamma_value = mp.gamma(value + 1)
        
        return gamma_value

    def faculty():
        try:
            float_value = float(input("\n\nEnter a float value: "))
            precision = int(input("\nEnter how many decimals points you would like to know: "))
            result = factorial_of_float(float_value, precision)
            console.print(f"\nThe factorial of {float_value} is: {result}", style="yellow")
        except ValueError as e:
            print(f"Error: {e}")


    faculty()
    
    return main()





def exit():
    console.print("\nProcess terminated.\n\n", style="red")
    sys.exit()

def main():
    text = Text()
    
    t1 = text.append("\n\n----------------------------------------------------\n", style="bold red")
    t_space = text.append("                   ")
    t2 = text.append("0. Exit\n\n", style="bold 2 red")

    t3 = text.append("[1.]", style="blue")
    text.append(" Addition               ", style="green")
    text.append("[8.]", style="blue")
    text.append(" Logarithm\n", style="green")

    t4 = text.append("[2.]", style="blue")
    text.append(" Subtraction            ", style="green")
    text.append("[9.]", style="blue")
    text.append(" Matrix\n", style="green")

    t5 = text.append("[3.]", style="blue")
    text.append(" Multiplication        ", style="green")
    text.append("[10.]", style="blue")
    text.append(" Factorial\n", style="green")

    t6 = text.append("[4.]", style="blue")
    text.append(" Division              ", style="green")
    text.append("[11.]", style="blue")
    text.append(" Gamma function\n", style="green")

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
    elif operation == 1:
        addition()
    elif operation == 2:
        subtraction()
    elif operation == 3:
        multiply()
    elif operation == 4:
        division()
    elif operation == 5:
        exponent()
    elif operation == 6:
        sqrt()
    elif operation == 7:
        integral_calc()
    elif operation == 8:
        logarithm()
    elif operation == 9:
        matrix()
    elif operation == 10:
        factorial()
    elif operation == 11:
        gamma_function()
    else:
        console.print("\nError: Invalid Operation", style="red")
        return main()

main()
