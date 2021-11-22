def doBTS(data:list, initial_h=0):
    if len(data)==0:
        return initial_h
    else:
        h_idx = int(len(data)/2)
        baseCitation = data[h_idx]
        numPaper = initial_h + h_idx+1# 논문건수
        if numPaper == baseCitation:# 논문건수와 인용횟수가 같은 경우
            # 마지막이거나 다음번 논문의 인용횟수가 현재 논문의 인용횟수보다 작은경우
            if (len(data) -1 == h_idx) or (len(data) -1 > h_idx and baseCitation>data[h_idx+1]):
                return initial_h +h_idx+1
            else:
                return doBTS(data[h_idx+1:], numPaper-1)
        elif numPaper < baseCitation:# 논문건수 보다 인용횟수가 큰 경우
            return doBTS(data[h_idx+1:], numPaper) # 현재 인용횟수보다 인용횟수가 작은 논문들과 현재까지 누적된 논문 전달
        elif numPaper > baseCitation:#논문건수 보다 인용횟수가 작은 경우
            return doBTS(data[:h_idx], numPaper - h_idx-1)# 현재 인용횟수보다 인용횟수가 큰 논문들과 현재까지 누적된 논문 전달


def solution(citations):
    numontry =0
    while True:
        numontry += 1
        data = sorted(citations, reverse=True)
        answer = doBTS(data)
        print(numontry,' : ', data,f'#{answer}#' ,citations[answer-1])
        citations = list(np.random.choice(9, 5, replace=True))
    # return answer
import numpy as np
sol = solution([3, 0, 6, 1, 5])# 3