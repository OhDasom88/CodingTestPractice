'''
삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 
아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 

삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

제한사항
삼각형의 높이는 1 이상 500 이하입니다.
삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.
[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]] 30
'''

def sol(point:int, idx:int, targets:list):
    if len(targets)==0:
        return point
    else:
        target = targets.pop()
        values = []
        for i in [idx, idx+1]:
            values.append(sol(target[i], i,targets.copy()))
        return max(values)+point

def solution(triangle:list):
    answer = 0
    triangle.reverse()
    points = triangle.pop()
    answer = sol(points[0], 0, triangle)
    return answer
def sol(processed:list, triangle:list):
        target = triangle.pop()
        temp = [sum(el) for el in zip(target, processed)]
        if len(temp) ==1:
            return temp[0]
        else:
            processed = [max([temp[i], temp[i+1]]) for i in range(len(temp)-1)]
            return sol(processed, triangle)

def solution(triangle:list):
    answer = 0
    target = triangle.pop()
    processed = [max([target[i], target[i+1]]) for i in range(len(target)-1)]
    answer = sol(processed, triangle)
    return answer

ans = solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])#30
print(ans)