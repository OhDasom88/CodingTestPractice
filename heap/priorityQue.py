

import heapq
def solution(operations):
    answer = []
    temp = []
    isHeapify = True
    for op in operations:
        cate, value = op.split()
        if cate=='I':#큐에 주어진 숫자를 삽입합니다.
            if not isHeapify: heapq.heapify(temp); isHeapify=True# heap 구조 유지
            heapq.heappush(temp, int(value))
        else:
            if len(temp)>0:
                if value =='1':# 최댓값을 삭제합니다.
                    if isHeapify: heapq._heapify_max(temp); isHeapify=False# heap 구조 유지
                    maxVal = heapq._heappop_max(temp)
                else:# 최솟값을 삭제합니다.
                    if not isHeapify: heapq.heapify(temp); isHeapify=True# heap 구조 유지
                    minVal = heapq.heappop(temp)
#  모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.
    if len(temp)>1:
        if isHeapify: # heap 구조 유지
            minVal = heapq.heappop(temp)
            heapq._heapify_max(temp)
            maxVal = heapq._heappop_max(temp)
        else:# heap 구조 유지
            maxVal = heapq._heappop_max(temp)
            heapq.heapify(temp)
            minVal = heapq.heappop(temp)
        answer = [maxVal, minVal]
    elif len(temp)>0:
        heapq.heapify(temp)
        minVal = heapq.heappop(temp)
        answer = [minVal, minVal]
    else:
        answer = [0,0]
    return answer
'''
operations는 길이가 1 이상 1,000,000 이하인 문자열 배열입니다.
operations의 원소는 큐가 수행할 연산을 나타냅니다.
원소는 “명령어 데이터” 형식으로 주어집니다.- 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.
빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.
'''
# print(solution(["I 16","D 1"]))# [0,0]
# print(solution(["I 7","I 5","I -5","D -1"]))# [7,5]
# print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))# [0,0]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))# 	[333, -45]