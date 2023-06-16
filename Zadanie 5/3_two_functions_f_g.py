def complex(f, g):
    def comp_func(x):
        return f(g(x))
    
    return comp_func

def f(x):
    return x ** 2

def g(x):
    return x + 1

# Comp. a functions f and g
h = complex(f, g)

# Calling a comp. function
x = 2
wynik = h(x)

print(f"Wynik złożonej funkcji dla h={x} wynosi: {wynik}")