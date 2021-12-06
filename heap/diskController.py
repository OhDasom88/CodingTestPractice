from collections import deque
from itertools import permutations
import heapq
from queue import PriorityQueue
def solution(jobs):
    answer = len(jobs)
    jobs = [tuple(el) for el in jobs]# 원소를 tuple로 바꿔야 heap 형태로 정렬됨
    heapq.heapify(jobs)# jobs 는 insert 부분이 없어서 굳이 heap을 사용하지 않아도 됨
    total = 0
    start = jobs[0][0]# 작업 시작시간 초기화
    while len(jobs) > 0:
        # 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.
        job = heapq.heappop(jobs)# 가장 먼저 요청이 들어온것을 출력
        total += job[1]# 처리시간 << 작업이 없을때 요청은 바로 진행이 됨(대기시간 = 0)
        start = sum(job)# 요청시점 + 요청처리시간
        if len(jobs)==0: break# 요청이 하나만 왔을때 오류 발생
        toProcess = PriorityQueue()
        while jobs[0][0] < start:  #요청시점에 하드디스크가 작업을 수행중
            seq = heapq.heappop(jobs)# 작업중에 들어온 요청
            toProcess.put((seq[1], seq[0]))# 소요시간+요청시점, 대기목록 업데이트
            if len(jobs) >0 :# 다음 요청목록이 있는경우
                if jobs[0][0] >= start: # 다음 요청시점에 진행작업이 없는경우(진행작업목록 업데이트 전)
                    while jobs[0][0] >= start and toProcess.qsize() > 0: # 대기목록으로 진행상황 업데이트
                        # 요청시점에 진행중인 목록이 있는지 확인
                        delayedSeq = toProcess.get()# 작업시간이 가장 작은 값이 반환됨
                        total += start + delayedSeq[0] - delayedSeq[1]# 종료시간(시작시간 + 소요시간) - 요청시간 = 대기시간 + 작업시간
                        start += delayedSeq[0]# 현재시작시간 + 소요시간 = 다음 시작시간
                    if toProcess.qsize() ==0 and jobs[0][0] >= start:
                        # 진행작업목록이 업데이트 후 요청시점에 진행작업 없음 확인
                        break # 2,3번째 반복문 중지
                else: # 대기목록 추가
                    pass# 2번째 반복문 재수행
            elif len(jobs)==0:# 모든 작업 대기목록으로 이동
                while toProcess.qsize()>0: # 대기목록으로 진행상황 업데이트
                    delayedSeq = toProcess.get()# 작업시간이 가장 작은 값이 반환됨
                    total += start + delayedSeq[0] - delayedSeq[1]# 종료시간(시작시간 + 소요시간) - 요청시간 = 대기시간 + 작업시간
                    start += delayedSeq[0]# 현재시작시간 + 소요시간 = 다음 시작시간
                break

    '''
    작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 
    (단, 소수점 이하의 수는 버립니다)
    '''
    return int(total/answer)
'''
jobs의 길이는 1 이상 500 이하입니다.
jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.

하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다. 
 >> 이조건을 지키지 않을경우 더빨리 작업이 처리되게끔 할수 있는것 같음
'''

def withPermute(jobs):
    answer = None
    for els in permutations(jobs,len(jobs)):
        # 처리작업이 없을때 들어온 요청을 바로 처리하지 않음
        # 모든 요청이 다들어왔을때 최소 처리시간을 반환
        total = 0
        ended = 0
        els = list(els)
        while len(els)>0:
            el = els.pop()
            if el[0] < ended:# 요청이 온 시점에 처리중인 작업이 있는 경우
                total += ended-el[0]+el[-1]# 대기시간(시작시 - 요청시) + 처리시간
                ended += el[-1]# 시작시 + 처리시간 = 끝나는 시간
            else:# 요청시점에 처리작업이 없는 경우
                total += el[-1]# 처리시간 << 요청시 바로 처리 시작
                ended = el[0] + el[-1]# 요청시 + 처리시간
            if answer is not None and answer < total:
                break
        if len(els)==0 and (answer is None or total < answer):
            answer = total
    return int(answer/len(jobs))

import numpy as np
import random

cnt = 0
# while True:
#     cnt += 1
#     size = random.randint(1, 3)# jobs의 길이는 1 이상 500 이하입니다.
#     '''
#     jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
#     각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
#     각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
#     '''
#     reqTimes = np.random.randint(0, high=10, size=size)
#     processTimes = np.random.randint(1, high=10, size=size)
#     jobs1 = [tupl for tupl in zip(reqTimes, processTimes)]
#     jobs2 = [list(tupl) for tupl in zip(reqTimes, processTimes)]
#     if solution(list(jobs1)) != withPermute(list(jobs2)):
#         print('# CNT: ',cnt)
#         print(withPermute(list(jobs2)))
#         print(solution(list(jobs1)))
#         print(withPermute(list(jobs2)))
#         print(solution(list(jobs1)))
#     # else:
#     #     print(jobs)
#     #     print(withPermute(list(jobs)))
#     #     print(solution(list(jobs)))

# print(withPermute([[0, 3], [1, 9], [2, 6]]))#9
print(solution([[0, 3], [1, 9], [2, 6]]))#9