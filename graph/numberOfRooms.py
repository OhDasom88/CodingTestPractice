from collections import defaultdict
import numpy as np
from numpy.linalg import matrix_rank
def solution(arrows):
    path = [[0,0]]
    for i, arrow in enumerate(arrows):
        start = path[-1].copy()
        if arrow ==0:
            start[1]+=1
        elif arrow ==1:
            start[0]+=1
            start[1]+=1
        elif arrow ==2:
            start[0]+=1            
        elif arrow ==3:
            start[0]+=1
            start[1]-=1
        elif arrow ==4:
            start[1]-=1
        elif arrow ==5:
            start[0]-=1
            start[1]-=1
        elif arrow ==6:
            start[0]-=1
        elif arrow ==7:
            start[0]-=1
            start[1]+=1
        path.append(start)
    vertices = defaultdict(int)
    edges = defaultdict(int)
    for i, point in enumerate(path):
        vertex = tuple(point)
        if vertices.get(vertex) is None:
            vertices[vertex] = len(vertices)

        edge = (tuple(path[i-1]), tuple(path[i]))
        if i >0 and edges.get(edge) is None:
            edges[edge] = len(edges)

    incidence = np.zeros((len(vertices),len(edges)), dtype=np.int8)
    for i, v in enumerate(path):
        if i==0: continue
        start = tuple(path[i-1])
        end = tuple(path[i])
        edge = (start, end)
        col = edges.get(edge)
        incidence[vertices.get(start)][col] = 1
        incidence[vertices.get(end)][col] = -1
    # rank-nullity-theorem
    rank = matrix_rank(incidence)# SVD 사용
    numOnEdge = incidence.shape[-1]
    # cycle 조건을 충족하는 space의 dimentionality
    # A->B, B->A 순환관계는 있지만 방으로 볼수는 없음
    # A -> B -> C -> B-> A  순환관계는 있지만 방으로 볼수는 없음
    dimensionOfNullSpace = numOnEdge - rank
    return dimensionOfNullSpace
# print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))#3
# print(solution([6, 5, 2, 7, 1, 4, 2, 4, 6]))#3
print(solution([5, 2, 7, 1, 6, 3]))#3 순환관계로는 표현되지 않음
print(solution([6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]))#3 순환관계로는 표현되지 않음