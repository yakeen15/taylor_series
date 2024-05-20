from sympy import symbols, Function, dsolve, series

# Define the symbols and the function
x = symbols('x')
y = Function('y')(x)

# Define the differential equation
differential_eq = y.diff(x, x) - y

# Solve the differential equation
general_solution = dsolve(differential_eq, y)
print(f"General solution: {general_solution}")

# Define the order for the Taylor series
n = 5

# Expand the solution into a power series
power_series = general_solution.rhs.series(x, 0, n+1).removeO()
print(f"Power series expansion up to x^{n}: {power_series}")
