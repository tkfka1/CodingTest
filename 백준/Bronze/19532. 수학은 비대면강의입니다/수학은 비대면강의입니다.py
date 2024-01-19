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

temp1,temp2,temp3,temp4,temp5,temp6 = map(int,input().split())
    
x = solve_simultaneous_equations(temp1,temp2,temp3,temp4,temp5,temp6)

print(f"{x[0]} {x[1]}")
