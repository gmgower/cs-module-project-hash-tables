# 1 memoized implementation of a recursive approach 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# Recursive function require:
## base case of
## move toward the base case 
## function has to call itself

# 2^n
def slow_fibonacci(n):
    if n <= 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)



# O(n) ?
cache = {}
def fibonacci(n, total = 0):
    if n <= 1:
        return n
    
    if n not in cache:
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
    
    return cache[n]

# Use a cache!
# Memoizing - store you result as you go
# dynamic programming
print(fibonacci(8))
print(fibonacci(9))
print(fibonacci(15))
print(fibonacci(25))
print(fibonacci(45))
print(fibonacci(1000))
print(len(cache))

# clearly, this has linear time complexity
# O(n)
def tiny_recurse(n):
    if n <= 1:
        return n

    return n + tiny_recurse(n - 1)