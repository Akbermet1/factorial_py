def factorial(num):
    counter, product = 1, 1
    
    if num < 0:
        print("Can't calculate a factorial of a negative value!")
        return None
    
    while counter <= num:
        product *= counter
        counter += 1
            
    return product

number = input("Enter an integer: ")
number = int(number)
print(factorial(number))

