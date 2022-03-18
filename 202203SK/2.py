'''
자연수 n과 시계/반시계 방향을 결정하는 boolean 값 clockwise가 주어집니다. 
입출력 예 설명의 그림과 같이 소용돌이 모양(clockwise가 참이면 시계방향, 거짓이면 반시계방향)으로 
n x n 정수 배열을 채워 return 하도록 solution 함수를 완성해주세요.
'''
    


def solution(n, clockwise):
    positions = [(0,0),(n-1,0),(n-1,n-1),(0,n-1)]
    answer = [[1 if (i,j) in positions else 0 for j in range(n)] for i in range(n)]
    direction_change=0
    while len([i for i in answer for j in i if j==0]) !=0:
        if clockwise: 
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
        else: 
            directions = [[0,1],[-1,0],[0,-1],[1,0]]
        for i in range(direction_change):
            directions.append(directions.pop(0))
        for i,(x,y) in enumerate(positions):
            movex, movey = directions.pop(0)
            if answer[y+movey][x+movex] != 0:
                direction_change +=1
                break
            answer[y+movey][x+movex] = answer[y][x] + 1
            positions.pop(i)
            positions.insert(i, (x+movex, y+movey))         
    return answer
ans = solution(6,True)#
print(ans)
ans = solution(6,False)#
print(ans)