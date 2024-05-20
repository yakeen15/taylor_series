from sympy import symbols, sympify

# Define the symbols
x = symbols('x')

# Get input from the user
user_input = input("Enter a function of x: ")

# Convert the input string to a SymPy expression
function = sympify(user_input)

# Print the resulting function
print(f"The function you entered is: {function}")

# Compute the derivative
derivative = function.diff(x)
print(f"The derivative of the function is: {derivative}")

# Get the order of the Taylor series from the user
n = int(input("Enter the order n for the Taylor series expansion: "))

# Compute the Taylor series expansion about x = 0 up to x^n
taylor_series = function.series(x, 0, n+1).removeO()
print(f"The Taylor series expansion of the function about x=0 up to x^{n} is: {taylor_series}")
