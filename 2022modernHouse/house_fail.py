'''
오늘의집을 통해 집을 인테리어 하기 전에 집을 설계하려고 합니다.

n x m 크기의 비어있는 집이 주어집니다. 당신은 이 집에 방과 화장실을 배치하려고 합니다.
방은 항상 2 x 2의 정사각형 모양이며 화장실은 항상 1 x 2의 직사각형 모양입니다.

당신은 이 집에 방 room개와 화장실 bath개를 배치하려고 합니다.

첫째, 방과 화장실을 배치할 때 방과 화장실은 상하좌우 중 최소 한 방향으로 집의 빈 공간과 인접해 있어야 합니다. 
즉, 집의 어느 빈 공간에서도 이어진 집의 빈 공간을 통해 모든 방과 화장실에 들어갈 수 있어야 합니다.
방과 방, 방과 화장실, 화장실과 화장실 사이의 이동은 불가능합니다. 
방이나 화장실로 이동은 인접한 집의 빈 공간에서만 할 수 있습니다.

둘째, 방과 화장실을 배치하고 남은 집의 빈 공간은 하나로 연결되어 있어야 합니다. 
즉, 방과 화장실을 배치할 때 집에서 버려지는 공간이 있으면 안 됩니다.

셋째, 집의 입구를 설치하기 위해 방과 화장실을 배치하고 남은 집의 빈 공간 중 
최소 한 공간은 집의 테두리와 인접해 있어야 합니다.

집의 세로 길이를 나타내는 정수 n, 집의 가로 길이를 나타내는 정수 m, 
배치해야 할 방의 개수를 나타내는 정수 room, 배치해야 할 화장실의 개수를 나타내는 정수 bath가 매개변수로 주어집니다. 
위 세 가지 조건에 맞게 방과 화장실을 배치하는 방법의 수를 return 하도록 solution 함수를 완성해주세요. 
단, 모든 방과 화장실을 배치할 수 없는 경우 0을 return 해주세요.

제한사항
1 ≤ n, m ≤ 5
1 ≤ room, bath ≤ 3
n x m 크기의 비어있는 집이 주어집니다. 당신은 이 집에 방과 화장실을 배치하려고 합니다.
방은 항상 2 x 2의 정사각형 모양이며 화장실은 항상 1 x 2의 직사각형 모양입니다.
'''
from copy import deepcopy
def solution(n, m, room, bath):

    def sol(room:int, bath:int, status:list):
        def checkConnection(x,y, paddedState):# 미완성
            connected = False
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    if i+j ==0:
                        continue
                    if paddedState[x+i][y+j] == 0:
                        connected = True
                        paddedState[x+i][y+j] = 1
                        checkConnection(x+i, y+j, paddedState)# 연결되어 있는 빈공간 확인 
            # if not connected:
            #     return False
            # else:                

        if room + bath == 0:
            # 모든 0 이 이어져 있는지 + 하나 이상의 0이 외각이 있는지 점검
            paddedState = [[1 for _ in range(m+2)]]
            for s in status:
                paddedState.append([1]+s+[1])
            paddedState.append([1 for _ in range(m+2)])

            conditions = False
            door = False
            zeroloc = False
            for i in range(n):
                for j in range(m):
                    if i==0 or j==0 or i==n-1 or j==m-1:
                        door=True
                    if status[i][j]==0:
                        paddedState[i+1][j+1]=1
                        checkConnection(i+1,j+1, deepcopy(paddedState))# padding 미완성
                        # checkConnection(i,j)# 

                    if door and isinstance(zeroloc, tuple):
                        conditions = True
                        break
            if conditions:
                return 1
            return 0
        else:
            ans = 0
            if room !=0:
                isFit = False
                for i in range(n-1):
                    for j in range(m-1):
                        if 0 == sum([status[i+k][j+l] for k in range(2) for l in range(2)]):
                            isFit = True
                            # 방 배치 가능
                            cpstatus = deepcopy(status)
                            for k in range(2):
                                for l in range(2):
                                    cpstatus[i+k][j+l] =1
                            ans += sol(room-1, bath, cpstatus)
                if not isFit:# 배정되지 않는 방
                    return 0
            if bath !=0:
                isFit = False # 가로 배치
                for i in range(n):
                    for j in range(m-1):
                        if 0 == sum([status[i][j+k] for k in range(2)]):
                            isFit = True # 방 배치 가능
                            cpstatus = deepcopy(status)
                            for k in range(2):
                                cpstatus[i][j+k] = 1
                            ans += sol(room-1, bath, cpstatus)
                for i in range(n-1):# 세로 배치
                    for j in range(m):
                        if 0 == sum([status[i+k][j] for k in range(2)]):
                            isFit = True # 방 배치 가능
                            cpstatus = deepcopy(status)
                            for k in range(2):
                                cpstatus[i+k][j] = 1
                            ans += sol(room-1, bath, cpstatus)
                if not isFit:# 배정되지 않는 방
                    return 0
            return ans
    ans = sol(room, bath, [[0 for _ in range(m)] for _ in range(n)])
    return ans
params = [
    [4,	5,	3,	1,	20],
    [2,	3,	1,	1,	0],
    [3,	4,	2,	1,	0],
    [2,	4,	1,	1,	6],
]
for param in params:
    print('param : ',param[:-1])
    print('ans : ',param[-1])
    pred = solution(*param[:-1])
    print('pred : ',pred)
    if pred != param[-1]:
        solution(*param[:-1]) 