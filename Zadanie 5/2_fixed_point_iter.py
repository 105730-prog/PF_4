def fixed_point_iteration(number, epsilon=1e-6, max_iterations=100):
    # typing arbitral start value
    x = 1.0
    
    # Iterate till to get max. aproximation
    for _ in range(max_iterations):
        
        x_new = (2 * x + number / (x * x)) / 3
        
        # checking epsilon
        if abs(x_new - x) < epsilon:
            return x_new
        
        # updating x value and cont. iteration
        x = x_new
    
    # If we fail to achieve the specified iteration quality, we get None
    return None

# For example
number = 6544
root = fixed_point_iteration(number)

if root is not None:
    print(f"Pierwiastek sześcienny z {number} wynosi: {root}")
else:
    print("Nie udało się obliczyć pierwiastka sześciennego.")
