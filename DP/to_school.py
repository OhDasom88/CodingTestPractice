'''
격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다.
오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 
1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.

제한사항

격자의 크기 m, n은 1 이상 100 이하인 자연수입니다.
m과 n이 모두 1인 경우는 입력으로 주어지지 않습니다.
물에 잠긴 지역은 0개 이상 10개 이하입니다.
집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않습니다.
'''


# from ast import Global
# from functools import lru_cache
# map, m, n = None, None, None
# @lru_cache(maxsize=None)
# def sol(x, y):
#     if Global.m == x:
#         return 0
#     elif Global.n == y:
#         return 0
#     elif Global.map[x][y] == 1:
#         return 0
#     elif Global.m == x+1 and Global.n == y+1:
#         return 1
#     else:
#         return sol(x+1, y) + sol(x, y+1)

# def solution(m, n, puddles):
#     answer = 0
#     Global.m = m
#     Global.n = n
#     map = [[0 for i in range(n)] for j in range(m)]
#     for x, y in puddles:
#         map[x-1][y-1] = 1
#         if x==m:
#             for i in range(y):
#                 map[x-1][i] = 1
#         if y==n:
#             for i in range(x):
#                 map[i][y-1] = 1
#     Global.map = tuple([tuple(i) for i in map])
#     answer = sol(0,0)
#     return answer%1000000007

from functools import lru_cache
def solution(m, n, puddles):
    answer = 0
    map = [[0 for i in range(n)] for j in range(m)]
    for x, y in puddles:
        map[x-1][y-1] = 1
        if x==m:
            for i in range(y):
                map[x-1][i] = 1
        if y==n:
            for i in range(x):
                map[i][y-1] = 1
    map = tuple([tuple(i) for i in map])
    @lru_cache(maxsize=None)
    def sol(x, y):
        if m == x:
            return 0
        elif n == y:
            return 0
        elif map[x][y] == 1:
            return 0
        elif m == x+1 and n == y+1:
            return 1
        else:
            return sol(x+1, y) + sol(x, y+1)
    answer = sol(0,0)

    return answer%1000000007

def solution(m, n, puddles):
    answer = 0
    map = [[0 for i in range(n)] for j in range(m)]
    for x, y in puddles:
        map[x-1][y-1] = 1
    map = tuple([tuple(i) for i in map])
    funcMap = {}
    def sol(x, y):
        if m == x:
            return 0
        elif n == y:
            return 0
        elif map[x][y] == 1:
            return 0
        elif m == x+1 and n == y+1:
            return 1
        else:
            if (x,y) in funcMap:
                return funcMap.get((x,y))
            else:
                funcMap.update({(x,y):sol(x+1, y) + sol(x, y+1)})
                return funcMap.get((x,y))
    answer = sol(0,0)

    return answer%1000000007

ans = solution(4,3,[[2, 2]])#4