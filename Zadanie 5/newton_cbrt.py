def newtons_method(f, f_prim, guess, tolerance=0.00001, max_iterations=100):
    def close_enough(a, b):
        return abs(a - b) < tolerance

    def try_next(guess, iteration):
        next_guess = guess - (f(guess) / f_prim(guess))
        if close_enough(guess, next_guess) or iteration >= max_iterations:
            return next_guess
        return try_next(next_guess, iteration + 1)

    return try_next(guess, 0)

def cube_root(x):
    f = lambda y: y**3 - x 
    f_prim = lambda y: 3 * y**2 
    return newtons_method(f, f_prim, 1.0)  

number = 27
result = cube_root(number)
print(f"Cubic root of {number} is: {result}")

