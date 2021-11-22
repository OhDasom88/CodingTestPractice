
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
            

import math

def counting_sort(A, digit, radix):
    # "A" is a list to be sorted, radix is the base of the number system, digit is the digit
    # we want to sort by

    # create a list B which will be the sorted list
    B = [0] * len(A)
    C = [0] * int(radix)
    # counts the number of occurrences of each digit in A 
    for i in range(0, len(A)):
        digit_of_Ai = (radix-1)-(A[i] // radix ** digit) % radix
        C[digit_of_Ai] = C[digit_of_Ai] + 1
        # now C[i] is the value of the number of elements in A equal to i

    # this for loop changes C to show the cumulative # of digits up to that index of C
    for j in range(1, radix):
        C[j] = C[j] + C[j - 1]# base 별 자리를 군별로 입력할수 있도록 수정 2진수 1,3,5 등[1]은 뒤로 2,4 등[0]은 앞으로
        # here C is modifed to have the number of elements <= i
    for m in range(len(A) - 1, -1, -1): # to count down (go through A backwards)
        digit_of_Ai = (radix-1)-(A[m] // radix ** digit) % radix
        C[digit_of_Ai] = C[digit_of_Ai] - 1# base별 자리군의 값을 지움
        B[C[digit_of_Ai]] = A[m]
    
    return B

def radix_sort(A, radix):
    # radix is the base of the number system
    # k is the largest number in the list
    k = max(A)
    # output is the result list we will build
    output = A
    # compute the number of digits needed to represent k
    digits = int(math.floor(math.log(k, radix) + 1))
    for i in range(digits):
        output = counting_sort(output, i, radix)

    return output

# A = [11, 10, 3, 14, 12, 2, 8, 15, 2]
# radix_sort(A, 2)

from collections import deque

def sol2(numbers):
    stack = deque([])
    numbers = deque(sorted([str(num) for num in numbers], key = lambda x: x[0], reverse = True))
    # start1 = time.time()
    # test1 = 0
    # test2 = 0
    # test3 = 0
    # test4 = 0
    # test5 = 0
    # idx = 0
    for i, num in enumerate(numbers):
        # k_list = deque([])
        # idx = 0
        if i == 0:
            stack.append(numbers[0])
        else:
            k_list = deque([])
            # start2 = time.time()
            
            while True:
                # start3 = time.time()
                if len(stack) <= 0: 
                    break
                # test3 += time.time() - start3
                # start3 = time.time()
                if stack[-1]== num: 
                    break
                # test4 += time.time() - start3
                # start3 = time.time()
                if int(stack[-1]+num) >= int(num+stack[-1]): 
                    break
                # idx += 1
                # test5 += time.time() - start3
                k_list.appendleft(stack.pop())
            stack.append(num)
            stack.extend(k_list)
    # end = time.time()
    # print(idx/len(numbers))
    # print('while len(stack) <= 0 : ', test3/(end-start1))
    # print('while stack[-1]== num : ', test4/(end-start1))
    # print('while int(str(stack[-1])+str(num)) >= int(str(num)+str(stack[-1])) : ', test5/(end-start1))
    if len(numbers) == sum([i == 0 for i in stack]):
        return "0"
    else:
        return "".join([str(i) for i in stack])

import time

def solution(numbers):
    answer = []
    numontry=0
    while True:
        numontry += 1
        # tmp1 = always(numbers)
        # tmp1 = int(getBigNumber({i:[num for num in numbers if str(num)[0] == i] for i in sorted(sorted([str(num)[0] for num in numbers]), key=len)}))
        start1 = time.time()
        maxlen = max([len(str(i)) for i in numbers])
        tmp1 = int(''.join(sorted([str(num) for num in numbers], key=lambda x: x*int((maxlen*2)/gcd(maxlen, len(x))), reverse = True)))
        done1 = time.time()
        
        # tmp2 = int(''.join([str(i) for i in radix_sort(numbers, 10)]))
        start2 = time.time()
        tmp2 = sol2(numbers) 
        done2 = time.time()
        # print('A', done2-start2)
        # print('B', done1-start1)
        if tmp2 != str(tmp1):
            print(tmp2 == tmp1, tmp2, tmp1, )
        # print(numontry)
        numbers = list(np.random.choice(1000, 100000, replace=True))
    # return tmp2 == tmp3
import numpy as np
from math import gcd

sol = solution([0,0,0,0,0])
# sol = solution([0,0,0,0,0,1])
# sol = solution([6, 10, 2]) # 6210
# sol = solution([3, 30, 34, 5, 9]) # 9534330
# sol = solution([6, 500, 52, 51, 5, 4]) # 9534330





