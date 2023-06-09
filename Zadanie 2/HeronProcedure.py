# Heron's method generates a sequence of numbers that represent 
# better and better approximations for √n. 
# The first number in the sequence is an arbitrary guess; every other number in the sequence is 
# obtained from the previous number prev using the formula:
x = 81
g = 1
results = [g]
if g * g == x:
    print("The square root of", x, "is", g)
else:
    g = (g + (x / g)) / 2
    results.append(g)
    while results[-1] != results[-2]:
        g = (g + (x / g)) / 2
        results.append(g)
    else:
        print(results)

# apppend() - enables us to add an element or an array to the end of another array
       