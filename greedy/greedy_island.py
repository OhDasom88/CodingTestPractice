def solution(n, costs):
    answer = 0
    parents = list(i for i in range(n))# index가 node, value가 root
    sortedArr = sorted(costs, key=lambda el : el[-1], reverse=True)
    while not len(set(parents)) == 1:
        edge = sortedArr.pop()
        if parents[edge[0]] != parents[edge[1]]:
            root = min([parents[node] for node in edge[:-1]])
            subroot = max([parents[node] for node in edge[:-1]])
            for i, parent in enumerate(parents):
                if parent == subroot:
                    parents[i] = root
            answer += edge[-1]
    return answer

# sol = solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]] )# 4
# sol = solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]] )#9
sol = solution(5,  [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]] )# 15
sol = solution(5,  [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]] )# 104
sol = solution(6,  [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]] )# 11
sol = solution(5,  [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]] )# 6
sol = solution(5,   [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]])# 8
sol = solution(5, [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]])# 8
sol = solution(5, [[0,1,1],[3,4,1],[1,2,2],[2,3,4]])# 8

print(sol)