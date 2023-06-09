a = 0
b = 1
nn = 1000
print(a, end=", ")
for i in range(0, nn):
    print(b, end=", ")
    b = b+a
    a = b-a