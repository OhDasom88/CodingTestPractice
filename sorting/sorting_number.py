
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

def always(nums):
    pick = None   
    for permuted in permutations(nums):
        number = ''.join([str(num) for num in permuted])
        if not pick or (pick is not None and pick < int(number)):
            pick = int(number)
    return str(pick)

def getBigNumber(resource:dict):
    if len(resource) == 0:
        return ''
    else:
        
        key, numbers = resource.popitem()
        if key=='0':
            return ''.join([str(num) for num in numbers]) + getBigNumber(resource)
        else:
            return always(numbers) + getBigNumber(resource)
            

def solution(numbers):
    answer = []
    numontry=0
    while True:
        numontry += 1
        # tmp1 = always(numbers)
        tmp1 = int(getBigNumber({i:[num for num in numbers if str(num)[0] == i] for i in sorted(sorted([str(num)[0] for num in numbers]), key=len)}))
        maxlen = max([len(str(i)) for i in numbers])
        tmp2 = int(''.join(sorted([str(num) for num in numbers], key=lambda x: x*int((maxlen*2)/gcd(maxlen, len(x))), reverse = True)))
        # tmp3 = always(numbers)
        if tmp2 != tmp1:
            print(tmp2 == tmp1, tmp2, tmp1, )
        print(numontry)
        numbers = list(np.random.choice(1000, 7, replace=True))
    # return tmp2 == tmp3
import numpy as np
from math import gcd

sol = solution([0,0,0,0,0])
# sol = solution([6, 10, 2]) # 6210
# sol = solution([3, 30, 34, 5, 9]) # 9534330
# sol = solution([6, 500, 52, 51, 5, 4]) # 9534330