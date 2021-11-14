def solution(routes):
    sortedroutes = sorted(routes, reverse=True)
    cameraRange = [sortedroutes.pop()]
    while len(sortedroutes) !=0:
        route = sortedroutes.pop()
        isDetected = False
        for camera in cameraRange:
            for i in range(len(route)):
                if camera[0] <= route[i] <= camera[-1]:
                    camera[i] = route[i]
                    isDetected = True
        if not isDetected:
            cameraRange.append(route)
    return len(cameraRange)
    
sol = solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])# 2
sol = solution([[-20,-15], [-14,-6], [-18,-13], [-5,-3]])# 3
sol = solution([[-1,-1], [-1,0], [-1,1], [0,0],[0,1],[1,1]])# 3 -1,0,1
sol = solution([[-1,-1], [-1,0], [0,1], [0,2], [-1,3], [0,0], [0,1], [1,1]])# 3 -1,0,1 
# print(sol)