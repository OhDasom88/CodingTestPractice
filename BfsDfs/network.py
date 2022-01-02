import numpy as np
from numpy.linalg import matrix_rank
'''
컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
computer[i][i]는 항상 1입니다.
'''

def solution(n, computers):
    '''
    컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 
    네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
    '''
    incidence = np.zeros((n, n*n))
    for i, net in enumerate(computers):
        for j, conn in enumerate(net):
            if i == j : continue
            incidence[i][i*n+j] = conn# i vertex, i*n+j edge >> 00 > 0번 edge 01 > 1번 edge
            incidence[i][j*n+i] = conn*-1
    # the number of vertices minus the number of connected components equals the rank of I(G)    
    return int(n- matrix_rank(incidence))

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))#2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))#1