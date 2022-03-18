from collections import defaultdict
def solution(nums) -> int:
    res = []
    for i, n in zip(range(1, len(nums)+1), nums):
        if i!=n:
            res.append(n)
            res.append(i)
    return res
ans = solution([1,2,3,4,3])
ans = solution([1,2,2])
def solution(cards) -> int:
    res = -1
    for card in cards:
        dic = defaultdict(int)
        for c in card:
            dic[c]+=1
        arr = [k for k,v in dic.items() if v==1]
        if len(arr) > 0:
            val = max(arr)
            if val > res:
                res = val
    return res

ans = solution([[5,7,3,9,4,9,8,3,1],[1,2,2,4,4,1],[1,2,3]])
ans = solution([[5,5],[2,2]])