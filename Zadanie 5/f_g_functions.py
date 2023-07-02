def composition(f, g):
    return lambda x: f(g(x))

def multiply(x):
    return 2 * x

def power(x):
    return x ** 2

complex_function = composition(multiply, power)

result = complex_function(10)
print(result)  


