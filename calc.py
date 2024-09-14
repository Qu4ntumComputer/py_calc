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
    euler = sp.E 
    pi = sp.pi 

    console.print(f"\nInput example:  f(x) = 3x² + 4x", style="yellow1")
    console.print("You can also use a ^ sign to symbolize exponents.\n", style="yellow1")

    console.print("f(x) = ", style="magenta3", end="")
    original_function = input()


    function = original_function.replace('^', '**')
    function = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', function)  


    function = function.replace('pi', f'{pi}')
    function = function.replace('e', f'{euler}')

    try:
        math_expr = sp.sympify(function)
        integral = sp.integrate(math_expr, x)


        integral_syntax = str(integral)
        integral_syntax = format_with_superscript(integral_syntax)
        integral_syntax = replace_multiplication_symbol(integral_syntax)


        formatted_original = format_exponents(original_function).replace('pi', 'π')
        integral_syntax = integral_syntax.replace('pi', 'π')

        console.print(f"\nThe undefined integral of f(x) = {formatted_original} is:\n", style="yellow1")
        console.print(f"f(x) = {integral_syntax} + c\n\n", style="yellow1")
    except Exception as e:
        console.print(f"Error while calculating: {e}", style="red1")
    
    return main()

def addition():
    try:

        console.print("\n> First Summand: ", style="magenta3", end="")
        num1_input = input()

        if num1_input == "pi":
            num1 = math.pi
        elif num1_input == "e":
            num1 = math.e
        else:
            num1 = float(num1_input)

 
        console.print("> Second Summand: ", style="magenta3", end="")
        num2_input = input()

 
        if num2_input == "pi":
            num2 = math.pi
        elif num2_input == "e":
            num2 = math.e
        else:
            num2 = float(num1_input)

        sum = num1 + num2
        console.print(f'\n\nThe result is: {sum}\n\n', style="yellow1")

    except ValueError:
        console.print("Invalid input, try again.", style="red1")
    
    return main()

def subtraction():
    try:
        console.print("\n> Minuend: ", style="magenta3", end="")
        num1_input = input()


        if num1_input.lower() == "pi":
            num1 = math.pi
        elif num1_input.lower() == "e":
            num1 = math.e
        else:
            num1 = float(num1_input)

        console.print("> Subtrahend: ", style="magenta3", end="")
        num2_input = input()

        if num2_input.lower() == "pi":
            num2 = math.pi
        elif num2_input.lower() == "e":
            num2 = math.e
        else:
            num2 = float(num1_input)

        Diff = num1 - num2
        console.print(f'\n\nThe result is: {Diff}\n\n', style="yellow1")
    except ValueError:
        console.print("Invalid input, try again.", style="red1")
    
    return main()

def multiply():
    try:
        console.print("\n> First Factor: ", style="magenta3", end="")
        num1_input = input()


        if num1_input.lower() == "pi":
            num1 = math.pi
        elif num1_input.lower() == "e":
            num1 = math.e
        else:
            num1 = float(num1_input)


        console.print("> Second Factor: ", style="magenta3", end="")
        num2_input = input()


        if num2_input.lower() == "pi":
            num2 = math.pi
        elif num2_input.lower() == "e":
            num2 = math.e
        else:
            num2 = float(num1_input)

        product = num1 * num2
        formatted_result = replace_multiplication_symbol(f"{product}")
        console.print(f'\n\nThe result is: {formatted_result}\n\n', style="yellow1")
    except ValueError:
        console.print("Invalid input, try again.", style="red1")
    
    return main()

def division():
    try:
        console.print("\n> Dividend: ", style="magenta3", end="")
        num1_input = input()

        if num1_input.lower() == "pi":
            num1 = math.pi
        elif num1_input.lower() == "e":
            num1 = math.e
        else:
            num1 = float(num1_input)

        console.print("> Divisor: ", style="magenta3", end="")
        num2_input = input()

        if num2_input.lower() == "pi":
            num2 = math.pi
        elif num2_input.lower() == "e":
            num2 = math.e
        else:
            num2 = float(num2_input)

        if num2_input == 0:
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
        num1_input = input()

        if num1_input.lower() == "pi":
            num1 = math.pi
        elif num1_input.lower() == "e":
            num1 = math.e
        else:
            num1 = float(num1_input)


        squareroot = math.sqrt(num1)
        console.print(f'\n\nThe result is: {squareroot}\n\n', style="yellow1")
    except ValueError:
        console.print("Invalid input, try again.", style="red1")
    
    return main()

def exponent():
    try:

        console.print("\n> Base: ", style="magenta3", end="")
        base_input = input()


        if base_input.lower() == "pi":
            base = math.pi
        elif base_input.lower() == "e":
            base = math.e
        else:
            base = float(base_input)

        console.print("> Exponent: ", style="magenta3", end="")
        expo_input = input() 


        if expo_input.lower() == "pi":
            expo = math.pi
        elif expo_input.lower() == "e":
            expo = math.e
        else:
            expo = float(expo_input)


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
        value_input = input()


        if value_input.lower() == "pi":
            value = math.pi
        elif value_input.lower() == "e":
            value = math.e
        else:
            value = float(value_input)


        console.print("> Base: ", style="magenta3", end="")
        base_input = input()


        if base_input.lower() == "pi":
            base = math.pi
        elif base_input.lower() == "e":
            base = math.e
        else:
            base = float(base_input)


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


import numpy as np
from rich.console import Console

console = Console()

def matrix():
    try: 
        def matrix_input():
            console.print("\n\nEnter the amount of lines and columns of your matrix with a space between each value: ", style="magenta3", end="")
            m, n = map(int, input().split())
            print("")

            if m != n:
                console.print("\nThe inverse of your matrix does not exist. A matrix must be quadratic to have an inverse.", style="red1")
                return None

            matrix = []

            for i in range(m):
                console.print(f"Enter the elements of the {i+1}. line of your matrix with a space between each value: ", style="magenta3", end="")
                zeile = list(map(float, input().split()))
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
        console.print("Invalid input, try again.", style="red1")

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

            console.print("\n\n> Float value: ", style="magenta3", end="")
            float_input = input()

            if float_input.lower() == "pi":
                float_value = math.pi
            elif float_input.lower() == "e":
                float_value = math.e
            else:
                float_value = float(float_input)

            console.print("> Enter how many decimal points you would like to know: ", style="magenta3", end="")
            precision = int(input())

            result = factorial_of_float(float_value, precision)
            console.print(f"\nThe factorial of {float_value} is: \n{result}", style="yellow")
        
        except ValueError as e:

            console.print(f"Error: {e}", style="red1")

    faculty()

    return main()

def help_list():

    console.clear()

    def typewriter_effect(text, delay=0.025):
        for char in text:
            console.print(char, style="yellow1", end="")
            sys.stdout.flush()
            time.sleep(delay)

    text = """
    » [1.] How to use constants like π or e
    » [2.] Not available yet (ran out of ideas...)
    » [3.] Back 

    """

    constants = """
    Mathematical constants are defined. You can use them just
    by typing the name of the constant. For example:

    [1. Addition]

    First Summand: pi
    Second Summand: 5

    The result is: 8.141592653589793


    As of now only "pi" and "e" are available for the usage
    of this calculator.
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
        


def trigonometry():
    banner = """
    [1.] Sin
    [2.] Cos
    [3.] Tan
    """

    console.print(banner, style="green1")

    console.print(">> Select an Operation: ", style="yellow1", end="")
    operation = int(input())

    if operation == 1:
        # Sinus Funktion
        console.print("\n>> sin(x)", style="yellow1")
        console.print("\n> x = ", style="magenta3", end="")
        angle_input = input()

        try:
            # Ersetze 'pi' und 'e' durch sympy Konstanten
            angle_input = angle_input.replace('pi', '*sp.pi').replace('e', '*sp.E')
            angle = sp.sympify(angle_input, locals={'sp': sp})  # Verwende Sympy zum Parsen des Ausdrucks
            result = sp.sin(angle)  # Berechnet den Sinus des eingegebenen Winkels
            console.print(f"sin({angle}) = {result}\n", style="green1")
        except Exception as e:
            console.print(f"Error: {e}", style="red1")

    elif operation == 2:
        # Cosinus Funktion
        console.print("\n>> cos(x)", style="yellow1")
        console.print("\n> x = ", style="magenta3", end="")
        angle_input = input()

        try:
            # Ersetze 'pi' und 'e' durch sympy Konstanten
            angle_input = angle_input.replace('pi', '*sp.pi').replace('e', '*sp.E')
            angle = sp.sympify(angle_input, locals={'sp': sp})  # Verwende Sympy zum Parsen des Ausdrucks
            result = sp.cos(angle)  # Berechnet den Cosinus des eingegebenen Winkels
            console.print(f"cos({angle}) = {result}\n", style="green1")
        except Exception as e:
            console.print(f"Error: {e}", style="red1")

    elif operation == 3:
        # Tangens Funktion
        console.print("\n>> tan(x)", style="yellow1")
        console.print("\n> x = ", style="magenta3", end="")
        angle_input = input()

        try:
            # Ersetze 'pi' und 'e' durch sympy Konstanten
            angle_input = angle_input.replace('pi', '*sp.pi').replace('e', '*sp.E')
            angle = sp.sympify(angle_input, locals={'sp': sp})  # Verwende Sympy zum Parsen des Ausdrucks
            result = sp.tan(angle)  # Berechnet den Tangens des eingegebenen Winkels
            console.print(f"tan({angle}) = {result}\n", style="green1")
        except Exception as e:
            console.print(f"Error: {e}", style="red1")

    else:
        console.print("Invalid operation, try again.", style="red1")

    return main()




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
    text.append(" Trigonometry\n", style="green1")

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
    elif operation== "12":
        trigonometry()
    else:
        console.print("\nError: Invalid Operation", style="red")
        return main()

main()
