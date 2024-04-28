# A Hamming number is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k.

# Write a function that computes the nth smallest Hamming number.

# Specifically:

# The first smallest Hamming number is 1 = 203050
# The second smallest Hamming number is 2 = 213050
# The third smallest Hamming number is 3 = 203150
# The fourth smallest Hamming number is 4 = 223050
# The fifth smallest Hamming number is 5 = 203051
# The 20 smallest Hamming numbers are given in the Example test fixture.

# Your code should be able to compute the first 5 000 ( LC: 400, Clojure: 2 000, Haskell: 12 691, NASM, C, D, C++, Go and Rust: 13 282 ) Hamming numbers without timing out.

#MY CODE
import itertools
def hamming(n):
    
    
    numbers = [i for i in range(0,35)]
    comb = set(itertools.product(*[numbers,numbers,numbers]))
    hamming = []
    for i in comb:
        hamming.append(2 ** i[0] * 3 ** i[1] * 5 ** i[2])
    hamming.sort()
    print(len(hamming))
    return hamming[n-1]

#OPTIMISED CODE
import heapq

def hamming(n):
    if n == 1:
        return 1
    
    seen = set()
    heap = [1]
    heapq.heapify(heap)
    
    for _ in range(n):
        ham = heapq.heappop(heap)
        for factor in [2, 3, 5]:
            next_ham = ham * factor
            if next_ham not in seen:
                seen.add(next_ham)
                heapq.heappush(heap, next_ham)
    
    return ham

#BEST CODE
def hamming(n):
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hamms = [1]
    for _ in range(1, n):
        next_hamms = [bases[i] * hamms[expos[i]] for i in range(3)]
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            expos[i] += int(next_hamms[i] == next_hamm)
    return hamms[-1]
