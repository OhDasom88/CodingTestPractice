from collections import defaultdict
from itertools import combinations
def solution(s):
    answer = 0
    tmp = [
        ['q','w','e','r','t','y','u','i','o']
        , ['p','a','s','d','f','g','h','j','k']
        , ['l','z','x','c','v','b','n','m','']
    ]
    loc = defaultdict(list)
    for i in range(len(tmp)):
        for j in range(len(tmp[0])):
            if i == len(tmp)-1 and j == len(tmp[0])-1:
                continue
            loc[tmp[i][j]] = [i,j]
    dist = defaultdict(int)
    for ik, iv in loc.items():
        for jk, jv in loc.items():
            for i in range(2):
              dist[ik+jk] += abs(iv[i]-jv[i])

    # for size in range(2,len(s)+1):
    #     for start in range(len(s)-size+1):
    #         subStr = s[start:start+size]
    #         for i in range(len(subStr)-1):
    #             keyStr = subStr[i:i+2]
    #             answer+= dist[keyStr]
    temp =[]
    for start in range(len(s)-1):
        subStr = s[start:start+2]
        num = dist[subStr]
        temp.append(num)

    for size in range(1,len(temp)+1):
        for start in range(len(temp)-size+1):
            answer+= sum(temp[start:start+size])
    return answer

print(solution('abcc'))# ,23
print(solution('tooth'))# ,52
print(solution('zzz'))# 0