
from math import inf
from collections import deque
import sys
sys.setrecursionlimit(2**30)
class Solution:
    def test(self, nums: list, x: int) -> int:
        cache = {}
        def sol(numbers:deque, num:int, op:int):
            if num == 0:
                return op
            else:
                if num <0 or len(numbers) == 0 or num > sum(numbers): return inf
                if len(cache) > 0 and min(cache.values()) <= op: return inf 
                ans = inf
                for i in range(2):
                    cpNums = numbers.copy()
                    if i==0:
                        cpNum = num - cpNums.popleft() 
                    else:
                        cpNum = num - cpNums.pop()
                    key = (tuple(cpNums), cpNum)
                    if key not in cache:
                        cache.update({key:sol(cpNums, cpNum, op+1)})
                    tmp = cache.get(key)
                    if ans > tmp:
                        ans = tmp
                return ans
        answer = sol(deque(nums),x,0)  
        return -1 if answer > len(nums) else answer
    '''
    We could use dfs+memo or BFS, but they are too slow and will TLE (?)
    If it exists an answer, 
    then it means we have a subarray in the middle of original array whose sum is == totalSum - x
    If we want to minimize our operations, then we should maximize the length of the middle subarray.
    Then the qeustion becomes: Find the Longest Subarray with Sum Equals to TotalSum - X
    We could simply use Map + Prefix Sum to get it!
    '''
    def minOperations(self, nums: list, x: int) -> int:
        answer = -1
        target = sum(nums) - x
        if target == 0: return len(nums)
        cache = {}
        summ = 0
        for i, num in enumerate(nums):
            summ += num
            if cache.get(summ-target):
                answer = max(answer, i+1-cache[summ-target])
            cache[summ] = i+1
        nums.reverse()
        cache = {}
        for i, num in enumerate(nums):
            summ += num
            if cache.get(summ-target):
                answer = max(answer, i+1-cache[summ-target])
            cache[summ] = i+1
        return answer if answer ==-1 else len(nums)-answer
        # cache = {}
        # def sol(numbers:deque):
        #     if sum(numbers)==(sum(nums)-x):
        #         return len(numbers)
        #     elif sum(numbers) > sum(nums)-x:
        #         if len(numbers)==0: return -1
        #         ans = -1
        #         for i in range(2):
        #             cpNums = numbers.copy()
        #             if i==0:
        #                 cpNums.popleft() 
        #             else:
        #                 cpNums.pop()
        #             key = tuple(cpNums)
        #             if key not in cache:
        #                 cache.update({key:sol(cpNums)})
        #             tmp = cache.get(key)
        #             if tmp > ans:
        #                 ans = tmp
        #         return ans
        #     elif sum(numbers) < sum(nums)-x:
        #         return -1
        # answer = sol(deque(nums.copy()))
        # return answer if answer ==-1 else len(nums) - answer

        # cache = [inf]
        # def sol(numbers:deque, num:int, op:int):
        #     if num == 0:
        #         if cache[0] > op:
        #             cache.pop()
        #             cache.append(op)
        #     elif num >0 and cache[0] > op:
        #         for i in range(2):
        #             cpNums = numbers.copy()
        #             if i==0:
        #                 cpNum = cpNums.popleft() 
        #             else:
        #                 cpNum = cpNums.pop()
        #             sol(cpNums, num-cpNum, op+1)
        # if x>sum(nums):
        #     return -1
        # else:
        #     sol(deque(nums),x,0)  
        # ans = cache.pop()
        # return -1 if ans == inf else ans
        

sol = Solution()
params = [
    [[1,1,4,2,3], 5, 2],
    [[5,6,7,8,9], 4, -1],
    [[3,2,20,1,1,3], 10, 5],
]

for param in params:
    print('param : ',param[:-1])
    print('Ans : ', param[-1])
    # pred = sol.test(*param[:-1])
    pred = sol.minOperations(*param[:-1])
    print('Pred : ', pred)
    if param[-1]!=pred:
        # sol.test(*param[:-1])
        sol.minOperations(*param[:-1])

'''
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
1 <= x <= 10^9
'''

import numpy as np
import random
from datetime import datetime as dt


idx = 0
while True:
    idx+=1
    # num = 4
    # target = random.randint(1,10**(num+5))
    # nums = random.choices(range(1,10**num), k=10**(num+1))
    num = 1
    target = random.randint(1,10**(num+2))
    nums = random.choices(range(1,10**num), k=10**(num+1))
    print('{}번째 '.format(str(idx)))
    print('param : ',(nums, target))
    try:
        start = dt.now()
        ans = sol.test(nums, target)
        print('ans : ',ans, dt.now()-start)
        start = dt.now()
        pred = sol.minOperations(nums, target)
        print('pred : ',pred, dt.now()-start)
        if pred !=ans:
            sol.minOperations(nums, target)
    except Exception as e:
        sol.minOperations(nums, target)
