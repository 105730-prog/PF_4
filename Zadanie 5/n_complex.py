def n_fold_composition(f, n):
    if n == 0:
        return lambda x: x
    elif n == 1:
        return f
    else:
        return lambda x: f(n_fold_composition(f, n-1)(x))

def doubling(x):
    return 2 * x

n = 17

n_fold_function = n_fold_composition(doubling, n)
result = n_fold_function(5)
print(result) 


