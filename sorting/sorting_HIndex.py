def doBTS(data:list, initial_h=0):
    if len(data)==0:
        return initial_h
    else:
        h_idx = int(len(data)/2)
        baseCitation = data[h_idx]
        numPaper = initial_h + h_idx+1
        if numPaper == baseCitation:# target 인용횟수  data[h] == 논문 수(h+1)
            if (len(data) -1 == h_idx) or (len(data) -1 > h_idx and baseCitation>data[h_idx+1]):
                return initial_h +h_idx+1
            else:
                return doBTS(data[h_idx+1:], numPaper-1)
        elif numPaper < baseCitation:# data[h] 번 이상 인용된 논문이 h+1편 보다 많음
            return doBTS(data[h_idx+1:], numPaper)
        elif numPaper > baseCitation:# data[h] 번 이상 인용된 논문이 h+1편 보다 적음
            return doBTS(data[:h_idx], numPaper - h_idx-1)


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