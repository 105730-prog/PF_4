#Ten program definiuje funkcję zbior_potegowy, która przyjmuje zbiór jako argument i zwraca zbiór potęgowy tego zbioru. 
#Algorytm wykorzystuje rekurencję i wygeneruje wszystkie możliwe podzbiory, 

#zaczynając od pustego zbioru i dodając każdy element na każdym kolejnym poziomie rekurencji.
#W powyższym przykładzie użyłem zbioru [1, 2, 3] jako wejścia, ale możesz zmienić ten zbiór na dowolny inny, 
#aby uzyskać zbiór potęgowy tego zbioru. Wynik zostanie wydrukowany na ekranie.

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

#Nawiasy kwadratowe w "return [[]]'' oznaczają zwracanie listy zawierającej jeden pusty podzbiór. 
#W przypadku tworzenia zbioru potęgowego, pusty zbiór jest częścią tego zbioru, 
#dlatego zwracamy go jako pierwszy element. W zapisie return [[]] puste nawiasy [] oznaczają pusty podzbiór, 
#a zewnętrzne nawiasy kwadratowe [] tworzą listę zawierającą ten pusty podzbiór. 
#Przykładowo, jeśli podamy pusty zbiór jako wejście do funkcji zbior_potegowy, 
#to zostanie zwrócona lista zawierająca pusty podzbiór jako swój jedyny element.
#Możemy to również interpretować jako podstawowy przypadek rekurencji, gdy zbiór wejściowy jest pusty. 
#W takiej sytuacji zbiór potęgowy składa się tylko z pustego zbioru.