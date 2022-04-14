
class Solution:
    def test(self, nums: list, target: int) -> int:
        for i,v in enumerate(nums):
            if v==target:
                return i
        return -1    
    def search(self, nums: list, target: int) -> int:
        cache = set()
        def sol(idx, dist):
            cache.add(nums[idx+int(dist)])
            if nums[idx+int(dist)]==target:
                return idx+int(dist)
            else:
                newDist = 1 if int(dist/2) ==0 else abs(dist)/2
                if nums[idx+int(dist)]>target:
                    newDist = newDist*-1
                if -1< idx+int(dist)+int(newDist) < len(nums):
                    if nums[idx+int(dist)+int(newDist)] not in cache:
                        return sol(idx+int(dist), newDist)
                    else:
                        return -1
                else:
                    return -1
        return sol(0, len(nums)/2)
sol = Solution()
params = [
    [[-1,0,3,5,9,12], 9, 4],
    [[-1,0,3,5,9,12], 2, -1],
]

for param in params:
    print('param : ',param[:-1])
    print('Ans : ', param[-1])
    pred = sol.test(*param[:-1])
    print('Pred : ', pred)
    if param[-1]!=pred:
        sol.test(*param[:-1])

'''
1 <= nums.length <= 10^4
-10^4 < nums[i], target < 10^4
All the integers in nums are unique.
nums is sorted in ascending order.
'''

import numpy as np
import random
idx = 0
while True:
    idx+=1
    target = random.randint(-20,20)
    nums = sorted(random.sample(range(-20,20), 10))
    print('{}번째 '.format(str(idx)))
    print('param : ',(nums, target))
    try:
        ans = sol.test(nums, target)
        print('ans : ',ans)
        pred = sol.search(nums, target)
        print('pred : ',pred)
        if pred !=ans:
            sol.search(nums, target)
    except Exception as e:
        sol.search(nums, target)
