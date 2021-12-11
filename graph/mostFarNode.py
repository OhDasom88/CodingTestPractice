
from collections import defaultdict
def answer(n, edge):
    '''
    n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 
    1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 
    가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

    노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 
    1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.
    '''
    v = defaultdict(set)
    for e in edge:
        v[e[0]].add(e[1])
        v[e[1]].add(e[0])
    parents = [1]
    visited = set([1])
    while True:
        nextParents = set()
        for parent in parents:
            w = v.pop(parent)
            for u in w:
                if u not in visited.union(nextParents):
                    nextParents.add(u)
        if len(nextParents)==0:
            return len(parents)
        else:
            parents = nextParents
            visited = visited.union(nextParents)

def solution(n, edge):
    '''
    n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 
    1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 
    가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

    노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 
    1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.
    '''
    v = defaultdict(set)
    for e in edge:
        v[e[0]].add(e[1])
        v[e[1]].add(e[0])
    parents = [1]
    visited = set([1])
    while True:
        nextParents = set()
        for parent in parents:
            connectedNodes = v.pop(parent)
            temp = visited.copy()
            for node in connectedNodes:
                if node not in temp:
                    nextParents.add(node)
                    temp.add(node)
        if len(nextParents)==0:
            return len(parents)
        else:
            parents = nextParents
            visited = visited.union(nextParents)

'''
노드의 개수 n은 2 이상 20,000 이하입니다.
간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.
'''
import random
# while True:

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))# 3