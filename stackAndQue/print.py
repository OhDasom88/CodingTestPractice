from collections import defaultdict, deque

def solution(priorities, location):
    answer = 0
    dq = deque()
    d = defaultdict(int)
    for i, p in enumerate(priorities):
        d[p] += 1
        dq.append((i, p))
    
    while len(dq) >0:
        v = dq.popleft()
        if v[-1] < max(d.keys()):
            dq.append(v)
        else:
            answer+=1
            if v[0] == location:
                break
            d[v[-1]]-=1
            if d[v[-1]] ==0:
                d.pop(v[-1])
    return answer

print(solution([2, 1, 3, 2], 2))#1
print(solution([1, 1, 9, 1, 1, 1], 0))#5