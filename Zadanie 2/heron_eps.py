# Heron's method generates a sequence of numbers that represent 
# better and better approximations for √n. 

number = float(input("type number to root : "))
error = float(input("type error : "))

a = number

while abs(a-number/a)>error:
    a = (a + number/a)/2

print("Square root of" , number , "is" , a)
       