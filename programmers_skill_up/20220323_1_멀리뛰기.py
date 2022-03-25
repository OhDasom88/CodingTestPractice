'''
효진이는 멀리 뛰기를 연습하고 있습니다. 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다. 칸이 총 4개 있을 때, 효진이는
(1칸, 1칸, 1칸, 1칸)
(1칸, 2칸, 1칸)
(1칸, 1칸, 2칸)
(2칸, 1칸, 1칸)
(2칸, 2칸)
의 5가지 방법으로 맨 끝 칸에 도달할 수 있습니다. 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내, 여기에 1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요. 예를 들어 4가 입력된다면, 5를 return하면 됩니다.

제한 사항
n은 1 이상, 2000 이하인 정수입니다.
입출력 예
'''

import sys
sys.setrecursionlimit(2**30)
def solution(n):
    cache = {}
    def sol(n):
        if n==0:
            return 1
        elif n<0:
            return 0
        else:
            answer =0
            if n-1 not in cache:
                cache.update({n-1:sol(n-1)})
            answer += cache.get(n-1)
            if n-2 not in cache:
                cache.update({n-2:sol(n-2)})
            answer += cache.get(n-2)
            return answer
    return sol(n)
params = [(4,5),(3,3)]
for param, ans in params:
    print('param : ',param)
    print('ans : ',ans)
    pred = solution(param)
    if ans != pred:
        solution(param)