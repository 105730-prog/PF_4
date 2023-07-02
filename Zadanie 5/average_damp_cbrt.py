def average_damp(f):
    return lambda x: (x + f(x)) / 2

def fixed_point(f, guess, tolerance=0.00001, max_iterations=100):
    def close_enough(a, b):
        return abs(a - b) < tolerance

    def try_next(guess, iteration):
        next_guess = f(guess)
        if close_enough(guess, next_guess) or iteration >= max_iterations:
            return next_guess
        return try_next(next_guess, iteration + 1)

    return try_next(guess, 0)

def cube_root(x):
    f = lambda y: x / (y * y)  # function f(y) = x / (y^2)
    average_damped = average_damp(f)
    return fixed_point(average_damped, x / 3)  # przyjmujemy początkowe zgadywanie jako x/3

number = 27
result = cube_root(number)
print(f"Cubic root of {number} equals: {result}")
