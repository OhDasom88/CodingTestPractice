'''
트리 tree_a와 트리 tree_b가 주어집니다.
tree_a는 n개의 정점으로 이루어져 있고 각 정점들은 1~n 번호를 겹치지 않게 가지고 있습니다.
tree_b도 n개의 정점으로 이루어져 있고 각 정점들은 1~n 번호를 겹치지 않게 가지고 있습니다.

당신은 tree_b를 tree_a와 똑같이 만들고 싶습니다.

당신은 두 가지 작업을 할 수 있습니다.

tree_b에 존재하는 간선 하나를 삭제하고 새로운 간선 하나를 추가합니다.
tree_b에 존재하는 두 정점의 번호를 바꿉니다.
1번 작업은 무제한으로 할 수 있지만 2번 작업은 최대 m번까지 밖에 할 수 없습니다.

tree_a의 간선 정보를 담고 있는 2차원 정수 배열 a
, tree_b의 간선 정보를 담고 있는 2차원 정수 배열 b
, 2번 작업을 할 수 있는 횟수 m이 매개변수로 주어집니다. 
이때, tree_b를 tree_a와 똑같이 만들기 위해 해야 하는 
1번 작업의 최소 횟수를 return 하도록 solution 함수를 작성해주세요.


'''
params = [[[[1, 2], [2, 3]],[[1, 3], [3, 2]],1,0]
, [[[1, 2], [3, 1], [2, 4], [3, 5]],[[2, 1], [4, 1], [2, 5], [3, 2]],1,1]
, [[[3, 4], [7, 2], [5, 4], [2, 3], [6, 5], [1, 2]],[[2, 1], [3, 6], [1, 4], [1, 5], [7, 1], [3, 2]],2,2]]


import numpy as np
from itertools import combinations, permutations
def solution(a, b, m):
    mat_a = np.zeros((len(a)+1,len(a)+1))
    mat_b = np.zeros((len(b)+1,len(b)+1))

    for ax, ay in a:
        mat_a[ax-1][ay-1] = 1
        mat_a[ay-1][ax-1] = 1
    for bx, by in b:
        mat_b[bx-1][by-1] = 1
        mat_b[by-1][bx-1] = 1

    def sol(mat, m):
        if m==0:
            return (mat!=mat_a).sum()/4
        tmpArr = []
        for pos in combinations(range(len(a)+1),2):
            tmpMat = mat.copy()
            ops = set()
            for i in range(len(a)):
                for j in range(len(a)+1):
                    if i in pos:
                        newi = pos.index(i)-1 if pos.index(i)-1>0 else len(a)
                        key = set([tuple([i,j]),tuple([newi,j])])
                        if key in ops:
                            continue
                        ops.add(key)
                        tmp = tmpMat[i,j]
                        tmpMat[i,j] = tmpMat[newi,j]
                        tmpMat[newi,j] = tmp
                    if j in pos:
                        newj = abs(pos.index(j)-1
                        key = set(tuple([i,j]),tuple([i,newj]))
                        if key in ops:
                            continue
                        ops.add(key)
                        tmp = tmpMat[i,j]
                        tmpMat[i,j] = tmpMat[i,newj]
                        tmpMat[i,newj] = tmp
            if (tmpMat!=mat_a).sum() == 0:
                return 0
            else:
                tmpArr.append(sol(tmpMat.copy(),m-1))
        return min(tmpArr)

    answer = sol(mat_b.copy(),m)

    return answer

for param1, param2, param3, ans in params:
    print('param1 : ',param1)
    print('param2 : ',param2)
    print('param3 : ',param3)
    print('ans : ',ans)
    pred = solution(param1, param2, param3)
    print('pred : ',pred)
    if ans != pred:
        solution(param1, param2, param3)
    