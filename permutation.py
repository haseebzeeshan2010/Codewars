import itertools

def permutations(s):
    combin = list(itertools.permutations(s))
    combin = map("".join, combin)
    return set(combin)
