'''
회사원 Demi는 가끔은 야근을 하는데요, 야근을 하면 야근 피로도가 쌓입니다. 
야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값입니다. 
Demi는 N시간 동안 야근 피로도를 최소화하도록 일할 겁니다.
Demi가 1시간 동안 작업량 1만큼을 처리할 수 있다고 할 때, 
퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값을 리턴하는 함수 solution을 완성해주세요.

제한 사항
works는 길이 1 이상, 20,000 이하인 배열입니다.
works의 원소는 50000 이하인 자연수입니다.
n은 1,000,000 이하인 자연수입니다.
'''

import heapq
def test(n, works):
    while n>0:
        n-=1
        heapq._heapify_max(works)
        works[0]-=1            
    if sum(works)>0:
        return sum([w**2 for w in works])
    else:
        return 0
import heapq
def solution(n:int, works:list):
    works = [-1*w for w in works]
    while n>0:
        heapq.heapify(works)
        temp = []
        temp.append(heapq.heappop(works))
        if temp[0]==0:break
        while len(works)!=0 and len(temp)<n  and temp[0] == works[0] :
            temp.append(heapq.heappop(works))
        n -= len(temp)
        for t in temp:
            heapq.heappush(works, t+1)
    if sum(works)<=0:
        return sum([w**2 for w in works])
    else:
        return 0
# works는 길이 1 이상, 20,000 이하인 배열입니다.
# works의 원소는 50000 이하인 자연수입니다.
# n은 1,000,000 이하인 자연수입니다.
import numpy as np
import random
idx = 0
while True:
    works = list(np.random.randint(1,5, size=random.randint(4,5)))
    n=random.randint(1,100)
    idx+=1
    print('{}번째 '.format(str(idx)))
    if solution(n, works.copy()) !=test(n, works.copy()):
        print(solution(n, works.copy()))
        print(test(n, works.copy()))
        solution(n,works.copy())



# ans = solution(4, [4, 3, 3])#12
# print(ans)
# ans = solution(1, [2, 1, 2])#6
# print(ans)
# ans = solution(3, [1,1])#0
# print(ans)