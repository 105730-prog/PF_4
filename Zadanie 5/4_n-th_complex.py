def comp(f, n):
    def c_func(x):
        wynik = x
        for _ in range(n):
            wynik = f(wynik)
        return wynik
    
    return c_func

def f(x):
    return x ** 2

# function f multiple times
n = 3
a = comp(f, n)

# Calling function
x = 2
wynik = a(x)

print(f"Wynik {n}-krotnego złożenia funkcji dla a={x} wynosi: {wynik}")
