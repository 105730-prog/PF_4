def newton_cube_root(k, epsilon):
  guess = k
  while(((1/3)*(2*guess + k/guess**2))**3 - k >= epsilon):
    guess = (1/3)*(2*guess + k/guess**2)
    print(f"Cube root of {k} is about {guess}")

newton_cube_root(216, .001)