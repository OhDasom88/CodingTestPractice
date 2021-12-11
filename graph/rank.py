'''
n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 
권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 
심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 
하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.

선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 
정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.
'''
def getOrder(parent, results:list):
    if len(results)==0:
        return
    else:
        for result in results:
            if result[0]==parent:
                getOrder(result[1], results)
import numpy as np
def solution(n, results):
    newResult = [[0 for j in range(n)] for i in range(n)]
    for result in results:
        win = result[0]
        lose = result[1]
        newResult[win-1][lose-1] +=1
        newResult[lose-1][win-1] -=1


    for player, resultOnPlayer in enumerate(newResult):
        for opponent, result in enumerate(resultOnPlayer):
            if player==opponent:
                continue
            resultOnOpponent = newResult[opponent]
            if result ==1:# player win 
                # 상대의 승리기록을 본인의 전적에 반영,
                # 패배기록을 상대의 패배기록에 반영
                for i in range(n):
                    if resultOnOpponent[i] ==1:
                        newResult[player][i] = 1
                    if resultOnPlayer[i]==-1:
                        newResult[opponent][i] = -1
            elif result == -1:# 상대의 패배 기록을 반영
                # 상대의 패배기록을 본인의 전적에 반영,
                # 승리기록을 상대의 승리기록에 반영
                for i in range(n):
                    if resultOnOpponent[i] ==-1:
                        newResult[player][i]= -1
                    if resultOnPlayer[i]==1:
                        newResult[opponent][i]= 1
            else:# 기록이 없는 경우
                pass

    answer = np.sum(np.count_nonzero(newResult, axis=1)==n-1)
    return answer
'''
선수의 수는 1명 이상 100명 이하입니다.
경기 결과는 1개 이상 4,500개 이하입니다.
results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
모든 경기 결과에는 모순이 없습니다.
'''
print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))#2