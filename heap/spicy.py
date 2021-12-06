from collections import deque


def solution1(scoville, K):
    answer = 0
    sortedScoville = sorted(scoville, reverse=True)# 덜매운게 마지막
    while len(sortedScoville) >2:
        mixed = sortedScoville.pop()# 섞인 음식(반복문이 한번 돈 상태)
        first = sortedScoville.pop()# 기존 음식 덜 매움
        second = sortedScoville.pop()# 기존 음식 더 매움
        moreSpicy, lessSpicy = (first, second) if first > second else (second, first)
        if mixed >= moreSpicy:# 섞은 음식이 나중 두음식보다 매움
            sortedScoville.append(mixed)
        elif mixed >= lessSpicy:# 섞은 음식이 나중 두음식중 매운음식보다는 덜맵지만 덜 매운움식보다는 매움
            sortedScoville.append(moreSpicy)
            moreSpicy = mixed
        elif mixed < lessSpicy:# 섞은 음식이 나중 두음식중 덜 매운음식보다도 덜 매움
            sortedScoville.append(moreSpicy)
            moreSpicy = lessSpicy
            lessSpicy = mixed
        if lessSpicy < K:# 덜매운거 기준 기준치 미만인지 비교
            answer += 1
            scov3 = lessSpicy+moreSpicy*2# 섞기
            sortedScoville.append(scov3)
        else:#  모든 음식의 스코빌 지수가 K 이상
            # K <= s and s <= l => K <= l
            break
    if len(sortedScoville) ==2 and min(sortedScoville) < K :# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
        lastChk = sorted(sortedScoville, reverse=True)
        if (lastChk.pop()+lastChk.pop()*2) > K:
            answer +=1
        else:
            answer = -1
    elif len(sortedScoville) == 1 and sortedScoville[0] < K:
        answer -1
    return answer


        
import bisect 

from collections import deque
def answer(scoville, K):
    answer = 0
    que = deque(sorted(scoville))
    while len(que) > 1 and que[0]<K:
        tmp = que.popleft()+que.popleft()*2
        for i, el in enumerate(que):
            if el >= tmp:
                que.insert(i, tmp)
                tmp = -1
                break
        if tmp!=-1:
            que.append(tmp)
        answer+=1
    if len(que) < 2:
        answer = answer if que.popleft() > K else -1
    return answer


def answer1(scoville, K):
    answer = 0
    que = deque(sorted(scoville))
    while len(que) > 1 and que[0]<K:
        tmp = que.popleft()+que.popleft()*2
        bisect.insort_left(que,tmp)
        answer+=1
    if len(que) < 2:
        answer = answer if que.popleft() > K else -1
    return answer

import heapq
def solution(scoville, K):
    answer = 0
    # tmpList = sorted(scoville, reverse=True)
    tmpList = list(scoville)
    heapq.heapify(tmpList)
    while len(tmpList) > 1 and tmpList[0]<K:
        # tmp = tmpList.pop()+tmpList.pop()*2
        v1 = heapq.heappop(tmpList)
        v2 = heapq.heappop(tmpList)
        tmp = v1+v2*2
        # lo = 0
        # hi = len(tmpList)
        # while lo < hi:
        #     mid = (lo + hi) // 2
        #     if tmpList[mid] > tmp:
        #         lo = mid + 1
        #     else:
        #         hi = mid
        # tmpList.insert(lo, tmp)
        heapq.heappush(tmpList,tmp)
        answer+=1
    if len(tmpList) < 2:
        answer = answer if tmpList.pop() > K else -1
    return answer
'''
scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
'''
import numpy as np
import random

cnt = 0
while True:
    cnt += 1
    k = random.randint(0, 10)
    size = random.randint(2, 5)
    scoville = np.random.randint(0, high=10, size=size)
    if solution(scoville=scoville, K=k) != answer1(scoville=scoville, K=k):
        print(cnt)
        print(answer(scoville=scoville, K=k))
        print(answer1(scoville=scoville, K=k))
        print(solution(scoville=scoville, K=k))
        print(answer1(scoville=scoville, K=k))
# print(answer([1, 2, 3, 9, 10, 12], 7))#2
# print(solution([0,1,0], 7))#2