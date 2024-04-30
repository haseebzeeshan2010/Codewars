# In this kata you will have to calculate fib(n) where:

# fib(0) := 0
# fib(1) := 1
# fib(n + 2) := fib(n + 1) + fib(n)
# Write an algorithm that can handle n up to 2000000.

# Your algorithm must output the exact integer answer, to full precision. Also, it must correctly handle negative numbers as input.

# HINT I: Can you rearrange the equation fib(n + 2) = fib(n + 1) + fib(n) to find fib(n) if you already know fib(n + 1) and fib(n + 2)? Use this to reason what value fib has to have for negative values.

# HINT II: See https://web.archive.org/web/20220614001843/https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.4

#Initial version
def fib(n):
    """Calculates the nth Fibonacci number"""
    min_sign = False
    fib = [0,1]
    
    if n < -1:
        min_sign = True
        
    n = abs(n)   
    
    for i in range(0,n):
        fib.append(fib[i]+fib[i+1])
    
    if min_sign == True:
        return -fib[-2]
    return fib[-2]
    pass