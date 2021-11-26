

# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             if prices[i]>prices[j] or j == len(prices)-1:
#                 answer.append(j-i)
#                 break
#     return answer.append(0)
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while len(prices)>0:
        price = prices.popleft()
        cnt = 0
        for i, p in enumerate(prices):
            if price>p or i == len(prices)-1:
                answer.append(cnt+1)
                break
            else:
                cnt += 1
    answer.append(0)
    return answer


print(solution([1, 2, 3, 2, 3]))#[4, 3, 1, 1, 0]