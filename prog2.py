def min_of_3():
    a = int(input("First number: "))
    b = int(input("Second number: "))
    c = int(input("Third number: "))
    if a < b and a < c:
       min = a
    elif b < a and b < c:
        min = b
    else:
        min = c
    return min


   
minimum = min_of_3()
print(f"The lowest of the 3 numbers is {minimum}")