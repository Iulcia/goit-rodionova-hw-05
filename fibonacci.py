""""This fnc calculates new one and stores calculated previously Fibonacci numbers"""

def caching_fibonacci():
    cache = {}

    def fibonacci(n:int):
        if n <= 0:  # check for invalid input parameter
            return 0
        elif n == 1: # exit point for recursion
            return 1
        elif n in cache.keys(): # check if value was already stored in cache
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # calculate new value and store in dict {"n":fibonacci(n)}
            return cache[n]
    
    return fibonacci