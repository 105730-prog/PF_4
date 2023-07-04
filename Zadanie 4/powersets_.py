
def powerset(collection):
    if len(collection) == 0:
        return [[]]
    
    first_element = collection[0]
    other_elements = collection[1:]
    
    subsets = powerset(other_elements)
    new_subsets = []
    
    for subset in subsets:
        new_subsets.append(subset)
        new_subsets.append([first_element] + subset)
    
    return new_subsets

collection = [1, 2, 3]
wynik = powerset(collection)
print(wynik)

