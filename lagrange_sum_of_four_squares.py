from typing import Tuple
import random

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True



def four_squares(n: int) -> Tuple[int, int, int, int]:
#     2n
#     p1+p2 = 2n
    
#     p1 % 4 == 1 # Same applies for p2
    
    if n == 0: return 0, 0, 0, 0
    
    
    #STEP 1: Reduce to 2n case or keep as n?
    if n % 2 == 0:
        s = random.randint(1,n) #s is the starting integer value
        
        while True:
            
            if is_prime(s) and is_prime((2*n)-s) and s % 4 == 1:
                break
            s += 1
        print(s)
    
    return 0, 0, 0, 0
