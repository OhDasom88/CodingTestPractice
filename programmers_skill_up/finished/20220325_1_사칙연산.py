'''
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때
, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

제한사항
N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
최솟값이 8보다 크면 -1을 return 합니다.
'''

from cmath import inf

def solution(N, number):
    def sol(nums):
        if len(nums)==1:
            return [int(nums)]
        if len(nums)==2:
            t1 = int(nums[0])
            t2 = int(nums[1])
            return set([t1+t2,t1-t2,t1*t2,t1//t2, int(nums)])
        ans = {int(nums)}
        for i in range(1,len(nums)):
            for n1 in sol(nums[:i]):
                for n2 in sol(nums[i:]):
                    ans.add(n1+n2)
                    ans.add(n1-n2)
                    ans.add(n1*n2)
                    if n2!=0:
                        ans.add(n1//n2)
        return ans
    for cnt in range(1,9):
        if number in sol(str(N)*cnt):
            return cnt
    return -1


# def solution(N, number):
#     cache = {}
#     def sol(num, cnt):
#         if num == number:
#             return cnt
#         elif cnt > 8:
#             return cnt
#         else:
#             sols = []
#             for numb in [num+N, num-N, num*N]:
#                 key = (numb, cnt)
#                 if key not in cache:
#                     cache.update({key: sol(numb, cnt+1)})
#                 sols.append(cache.get(key))
#             if num!=0:
#                 for numb in [int(str(abs(num))+str(N))*(num//abs(num)), int(str(N)+str(abs(num)))*(num//abs(num))]:
#                     key = (numb, cnt)
#                     if key not in cache:
#                         cache.update({key: sol(numb, cnt+1)})
#                     sols.append(cache.get(key))
#             if num%N==0:
#                 numb = int(num/N)
#                 key = (numb, cnt)
#                 if key not in cache:
#                     cache.update({key: sol(numb, cnt+1)})
#                 sols.append(cache.get(key))
#             return min(sols)
#     answer = sol(0, 0)
#     return -1 if answer >8 else answer

params = [
    (8,53,5),
    (5,12,4),
    (2,11,3),
]
for N, number, ans in params:
    print('param : ',(N, number))
    print('Ans : ', ans)
    pred = solution(N, number)
    print('Pred : ', pred)
    if ans!=pred:
        solution(N, number)
