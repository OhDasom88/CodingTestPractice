def getPath(path:list, edges:list):
    
    adjacentVertices = []
    for i, edge in enumerate(edges):
        if path[-1] == edge[0]:
            adjacentVertices.append((i, edge))

    if len(adjacentVertices) > 0:
        pathes = []
        for vertice in adjacentVertices:
            newPath = path.copy()
            newPath.append(vertice[1][1])
            idx = int(vertice[0])
            newEdges = edges[:idx]+edges[idx+1:] if idx+1<len(edges) else edges[:idx]
            pathInfo = getPath(newPath, newEdges)
            if pathInfo is not None:
                pathes.append(pathInfo)
        if len(pathes) > 0:
            sortedPathes = sorted(pathes, key=lambda x: [-len(set(x)),x], reverse=True)
            selectedPath = sortedPathes.pop()
            return selectedPath
        else:
            return None
    else:# leaf
        return path if len(edges) == 0 else None


def solution(tickets):
    '''
    항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 
    방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
    항상 "ICN" 공항에서 출발합니다.
    '''
    answer = []
    answer = getPath(['ICN'], tickets)
    return answer

'''
제한사항
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

입출력 예
[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	
    >>  ["ICN", "JFK", "HND", "IAD"] # ["ICN", "JFK", "HND", "IAD"] 순으로 방문할 수 있습니다.

[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    >>  ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
    # ["ICN", "SFO", "ATL", "ICN", "ATL", "SFO"] 순으로 방문할 수도 있지만 
    # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] 가 알파벳 순으로 앞섭니다.
'''