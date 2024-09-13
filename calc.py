import sys
import sympy as sp
import re
import math
from rich.console import Console
from rich.text import Text
import numpy as np
from mpmath import mp
import time


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


    console.print(f"Input example:  f(x) = 3x² + 4x", style="yellow1")
    console.print("You can also use a ^ sign to symbolize exponents.\n", style="yellow1")

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
        console.print(f"Error while calculating: {e}", style="red1")
    
    return main()

def addition():
    try:
        console.print("\n> First Summand: ", style="magenta3", end="")
        num1 = float(input())

        console.print("> Second Summand: ", style="magenta3", end="")
        num2 = float(input())

        sum = num1 + num2
        console.print(f'\n\nThe result is: {sum}\n\n', style="yellow1")
    except ValueError:
        console.print("Invalid input, try again.", style="red1")
    
    return main()

def subtraction():
    try:
        console.print("\n> Minuend: ", style="magenta3", end="")
        num1 = float(input())

        console.print("> Subtrahend: ", style="magenta3", end="")
        num2 = float(input())

        Diff = num1 - num2
        console.print(f'\n\nThe result is: {Diff}\n\n', style="yellow1")
    except ValueError:
        console.print("Invalid input, try again.", style="red1")
    
    return main()

def multiply():
    try:
        console.print("\n> First Factor: ", style="magenta3", end="")
        num1 = float(input())

        console.print("> Second Factor: ", style="magenta3", end="")
        num2 = float(input())

        produkt = num1 * num2
        formatted_result = replace_multiplication_symbol(f"{produkt}")
        console.print(f'\n\nThe result is: {formatted_result}\n\n', style="yellow1")
    except ValueError:
        console.print("Invalid input, try again.", style="red1")
    
    return main()

def division():
    try:
        console.print("\n> Dividend: ", style="magenta3", end="")
        num1 = float(input())

        console.print("> Divisor: ", style="magenta3", end="")
        num2 = float(input())
        if num2 == 0:
            console.print("\nUndefined (Error 0 division)\n", style="red1")
        else:
            quotient = num1 / num2
            console.print(f'\n\nThe result is: {quotient}\n\n', style="yellow1")
    except ValueError:
        console.print("Invalid input, try again.", style="red1")
    
    return main()

def sqrt():
    try:
        console.print("\n> Value: ", style="magenta3", end="")
        num1 = float(input())

        squareroot = math.sqrt(num1)
        console.print(f'\n\nThe result is: {squareroot}\n\n', style="yellow1")
    except ValueError:
        console.print("Invalid input, try again.", style="red1")
    
    return main()

def exponent():
    try:

        console.print("\n> Base: ", style="magenta3", end="")
        base = float(input())

        console.print("\n> Exponent: ", style="magenta3", end="")
        expo = float(input()) 

        result = base ** expo
        
        if expo.is_integer():
            formatted_result = f"{base}{to_superscript(int(expo))} is {result}"
        else:
            formatted_result = f"{base}^{expo} = {result}"
        console.print(f'\n\nThe result of {formatted_result}\n\n', style="yellow1")
    except ValueError:
        console.print("Invalid input, try again.", style="red1")
    
    return main()


def logarithm():
    try:

        console.print("\n> Value: ", style="magenta3", end="")
        value = float(input())

        console.print("\n> Base: ", style="magenta3", end="")
        base = float(input())

        if value <= 0:
            console.print("Error, logarithm of negative numbers or 0 is not defined.", style="red1")
        if base <= 0:
            console.print("Error, the base of a logarithm can't be equal or less than 0.", style="red1")
        if base == 1:
            console.print("Error, the base of a logarithm can't be equal to 1.", style="red1")

        result = math.log(value, base)

        console.print(f'\nThe result is: {result}', style="yellow1")

    except ValueError:
        console.print("Invalid input, try again.", style="red1")

    return main()

def factorial():
    try:
        console.print("\n> Value: ", style="magenta3", end="")
        value = int(input())

        if value < 0:
            console.print("Factorials aren't defined for negatives numbers.", style="red1")
            return factorial()
        result = 1
        for i in range(2, value + 1):
            result *= i
        
        console.print(f'\n\nThe result is: {result}', style="yellow1")


    except ValueError:
        console.print("Error, this function only accepts integer values. Use gamma function for non-integer factorials.", style="red1")

    return main()


def matrix():
    try: 
        def matrix_input():
            m, n = map(int, input("\n\nEnter the amount of lines and columns of your matrix with a space between each value: ").split())
            print("")

            if m != n:
                console.print("\nThe inverse of your matrix does not exist. A matrix must be quadratic to have an inverse.", style="red1")
                return None

            matrix = []

            for i in range(m):
                zeile = list(map(float, input(f"Enter the elements of the {i+1}. line of your matrix with a space between each value: ").split()))
                if len(zeile) != n:
                    console.print("\nError, wrong amount of lines. Try again.", style="red1")
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
                console.print("\n\nThe inverse of your matrix is: \n", style="yellow1")
                format_matrix(inverse)

    except ValueError:
        console.print("Error, input values must be of the datatype 'float', try again", style="red1")


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
            float_value = float(input("\n\n> Float value: "))
            precision = int(input("Enter how many decimals points you would like to know: "))
            result = factorial_of_float(float_value, precision)
            console.print(f"\nThe factorial of {float_value} is: {result}", style="yellow")
        except ValueError as e:
            console.print(f"Error: {e}", style="bold red")


    faculty()
    
    return main()

def help_list():

    console.clear()

    def typewriter_effect(text, delay=0.025):
        for char in text:
            console.print(char, style="yellow", end="")
            sys.stdout.flush()
            time.sleep(delay)

    text = """
    » [1.] How to use constants like π or e
    » [2.] bla bla bla
    » [3.] Back

    """

    constants = """
    bla bla bla
    bla bla bla
    """


    console.print("\n----------------------------------------------------", style="purple")
    typewriter_effect(f'\n{text}\n', 0.01)
    console.print("----------------------------------------------------", style="purple")


    console.print("\n>> Enter option: ", style="yellow1", end="")
    choice = int(input())

    if choice == 0:
        main()
    elif choice == 1:
        def typewriter_effect(text, delay=0.025):
            for char in text:
                console.print(char, style="yellow1", end="")
                sys.stdout.flush()
                time.sleep(delay)
        console.clear()
        console.print("\n----------------------------------------------------", style="purple")
        typewriter_effect(f'\n{constants}\n', 0.01)
        console.print("\n----------------------------------------------------", style="purple")
        console.print("Type 'Ok' to go back: ", style="dodger_blue1", end="")
        answer = input()

        if answer == "ok" or answer == "Ok":
            console.clear()
            main()
        else:
            console.print("Sorry, did you mean to type 'ok'? (y/n)", style="dodger_blue1", end=" ")
            answer_typo = str(input())
            if answer_typo == "y":
                console.clear()
                main()
            else:
                console.clear()
                console.print("fuck you", style="yellow1")
                
                main()

    elif choice == 3:
        console.clear()
        main()

    else:
        console.print("\nError: Invalid input. Try again.", style="red1")
        return help_list()
        




def exit():
    console.clear()
    console.print("\nProcess terminated.", style="red1")
    sys.exit()


def main():
    text = Text()
    
    text.append("\n\n----------------------------------------------------\n", style="red1")
    text.append("                   ")
    text.append("0. Exit\n\n", style="red1")

    text.append("[01.]", style="blue1")
    text.append(" Addition              ", style="green1")
    text.append("[08.]", style="blue1")
    text.append(" Logarithm\n", style="green1")

    text.append("[02.]", style="blue1")
    text.append(" Subtraction           ", style="green1")
    text.append("[09.]", style="blue1")
    text.append(" Inverse Matrix\n", style="green1")

    text.append("[03.]", style="blue1")
    text.append(" Multiplication        ", style="green1")
    text.append("[10.]", style="blue1")
    text.append(" Factorial\n", style="green1")

    text.append("[04.]", style="blue1")
    text.append(" Division              ", style="green1")
    text.append("[11.]", style="blue1")
    text.append(" Gamma function\n", style="green1")

    text.append("[05.]", style="blue1")
    text.append(" Exponent              ", style="green1")
    text.append("[12.]", style="blue1")
    text.append(" ??\n", style="green1")

    text.append("[06.]", style="blue1")
    text.append(" Squareroot            ", style="green1")
    text.append("[13.]", style="blue1")
    text.append(" ??\n", style="green1")

    text.append("[07.]", style="blue1")
    text.append(" undefined Integrals", style="green1")
    text.append("   [14.]", style="blue1")
    text.append(" ??\n", style="green1")
    text.append("\n               Type !h for help.", style="yellow1")

    text.append("\n----------------------------------------------------\n", style="red1")

    console.print(text)


    console.print(">> Select an Operation: ", style="yellow1", end="")
    operation = input()


    if operation == "0":
        exit()
    elif operation == "!h":
        help_list()

    elif operation == "1":
        addition()
    elif operation == "2":
        subtraction()
    elif operation == "3":
        multiply()
    elif operation == "4":
        division()
    elif operation == "5":
        exponent()
    elif operation == "6":
        sqrt()
    elif operation == "7":
        integral_calc()
    elif operation == "8":
        logarithm()
    elif operation == "9":
        matrix()
    elif operation == "10":
        factorial()
    elif operation == "11":
        gamma_function()
    else:
        console.print("\nError: Invalid Operation", style="red")
        return main()

main()
