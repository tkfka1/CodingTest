# Given problem: Solve the simultaneous equations for integer values of x and y
# Equation 1: ax + by = c
# Equation 2: dx + ey = f

# Let's define a function to solve these equations using the given input parameters

def solve_simultaneous_equations(a, b, c, d, e, f):
    # We will use the method of determinants to solve these equations
    # The determinant (denominator) for x and y
    determinant = a*e - b*d
    
    # To ensure we don't divide by zero
    if determinant == 0:
        return None

    # The numerators for x and y
    x_numerator = c*e - b*f
    y_numerator = a*f - c*d

    # Calculating the values of x and y
    x = x_numerator / determinant
    y = y_numerator / determinant

    # Check if x and y are integers
    if x.is_integer() and y.is_integer():
        return int(x), int(y)
    else:
        return None

# Test with example inputs

# Example 1
x = solve_simultaneous_equations(1, 3, -1, 4, 1, 7)


# Example 2
print(solve_simultaneous_equations(2, 5, 8, 3, -4, -11))
