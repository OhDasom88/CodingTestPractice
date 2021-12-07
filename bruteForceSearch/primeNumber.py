def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield int(''.join(tuple(pool[i] for i in indices[:r])))
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield int(''.join(tuple(pool[i] for i in indices[:r])))
                break
        else:
            return
def solution(numbers):
    answer = 0
    temp = set()
    for size in range(1, len(numbers)+1):
        for target in permutations(numbers, size):
            isPrime = True
            if target in [0,1] or target in temp: continue
            for i in range(2, target):
                if target % i ==0: isPrime = False; break
            if isPrime: 
                temp.add(target) 
    return len(temp)

print(solution("17"))# 3
print(solution("011"))# 2