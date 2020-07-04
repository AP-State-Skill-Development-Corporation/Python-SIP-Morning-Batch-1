def even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
def factorial(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact

pi = 3.14
x = 5