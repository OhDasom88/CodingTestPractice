'''
오늘의집 스토어에서 마음에 드는 침대들과 책상들을 찾았습니다. 
이 중 침대와 책상을 하나씩 구매하고, 이들을 배치할 수 있는 가장 작은 면적의 직사각형 모양 방을 구하려 합니다.
평면도상에서 방에 가구를 배치할 때 침대와 책상은 w × h 크기의 직사각형으로 표현하며, 
그대로 배치하거나 90도 회전해서 배치할 수 있지만 서로 겹치는 부분이 없어야 합니다.

총예산이 최소가 되도록 침대와 책상, 그리고 방의 면적을 선택하려고 합니다. 
이때 총예산은 침대의 가격 + 책상의 가격 + 방의 면적 × 방의 면적당 가격 으로 계산됩니다.

침대들의 정보가 담긴 2차원 정수 배열 beds, 책상들의 정보가 담긴 2차원 정수 배열 tables, 
방의 면적당 가격을 나타내는 정수 cost가 매개변수로 주어질 때, 
가능한 총예산의 최솟값을 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ beds의 길이 ≤ 1,000
beds의 원소는 [w, h, price] 형태입니다.
w, h는 침대의 가로 길이와 세로 길이를 나타냅니다.
1 ≤ w, h ≤ 1,000
price는 침대의 가격을 나타냅니다.
1 ≤ price ≤ 1,000,000
1 ≤ tables의 길이 ≤ 1,000
tables의 원소는 [w, h, price] 형태입니다.
w, h는 책상의 가로 길이와 세로 길이를 나타냅니다.
1 ≤ w, h ≤ 1,000
price는 책상의 가격을 나타냅니다.
1 ≤ price ≤ 1,000,000
1 ≤ cost ≤ 10,000
'''

params = [
    [[[4, 1, 200000]], [[2, 3, 100000]], 10000, 420000],
    [[[2, 3, 40], [2, 5, 20]], [[1, 1, 30]], 10000, 80070],
    [[[2, 3, 40000], [2, 5, 20000]],[[1, 1, 30000]],	10,	50120]
]
from cmath import inf
def solution(beds, tables, cost):
    answer = inf
    for bed in beds:
        for table in tables:
            minA = inf
            for i, x in enumerate(bed[:-1]):
                for j, y in enumerate(table[:-1]):
                    tmp = (x+y)*max([bed[:-1][i-1], table[:-1][j-1]])
                    if minA > tmp:
                        minA = tmp
            price = bed[-1] + table[-1] + minA*cost
            if price< answer:
                answer = price
    return answer
for param in params:
    print('param : ',param[:-1])
    print('ans : ',param[-1])
    pred = solution(*param[:-1])
    print('pred : ',pred)
    if pred != param[-1]:
        solution(*param[:-1])    