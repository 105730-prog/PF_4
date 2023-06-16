def newtons_method(number, epsilon=1e-2, max_iterations=10000):
    
    x = 1.0 # typing arbitral start value
  
    for _ in range(max_iterations):
        
        x_new = (2 * x + number / (x ** 5)) / 3
      
        if abs(x_new - x) < epsilon:
            return x_new
        
        x = x_new
    
    return None # If we fail to achieve the specified iteration quality, we get None

number = 10  
root = newtons_method(number)

if root is not None:
    print(f"Cubic root of {number} is: {root}")
else:
    print("Cannot find cubic root")
