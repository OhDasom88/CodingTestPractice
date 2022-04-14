'''
N개의 아파트가 일렬로 쭉 늘어서 있습니다. 
이 중에서 일부 아파트 옥상에는 4g 기지국이 설치되어 있습니다. 
기술이 발전해 5g 수요가 높아져 4g 기지국을 5g 기지국으로 바꾸려 합니다. 
그런데 5g 기지국은 4g 기지국보다 전달 범위가 좁아, 
4g 기지국을 5g 기지국으로 바꾸면 어떤 아파트에는 전파가 도달하지 않습니다.

예를 들어 11개의 아파트가 쭉 늘어서 있고, 
[4, 11] 번째 아파트 옥상에는 4g 기지국이 설치되어 있습니다. 
만약 이 4g 기지국이 전파 도달 거리가 1인 5g 기지국으로 바뀔 경우 모든 아파트에 전파를 전달할 수 없습니다. 
(전파의 도달 거리가 W일 땐, 기지국이 설치된 아파트를 기준으로 전파를 양쪽으로 W만큼 전달할 수 있습니다.)

이때, 우리는 기지국을 최소로 설치하면서 모든 아파트에 전파를 전달하려고 합니다.

아파트의 개수 N, 현재 기지국이 설치된 아파트의 번호가 담긴 1차원 배열 stations, 
전파의 도달 거리 W가 매개변수로 주어질 때, 
모든 아파트에 전파를 전달하기 위해 증설해야 할 기지국 개수의 최솟값을 리턴하는 solution 함수를 완성해주세요
'''
from audioop import reverse
from math import ceil
def solution(n, stations, w):
    new_stations = [s+i for s in stations for i in [-w-1,w+1]]
    if new_stations[0] < 1:
        new_stations.pop(0)
    elif new_stations[0] >= 1:
        new_stations.insert(0,1)   

    if new_stations[-1] > n:
        new_stations.pop()
    elif new_stations[-1] <= n:
        new_stations.append(n)
    answer = 0
    for i in range(len(new_stations)//2):
        dist = new_stations[2*i+1] - new_stations[2*i]+1
        if dist > 0:
            answer += ceil(dist/(2*w+1))        
    return answer

params = [
    [11,	[4, 11],	1,	3],
    [16,	[9],	2,	3],
]


for param in params:
    print('param : ',param[:-1])
    print('Ans : ', param[-1])
    pred = solution(*param[:-1])
    print('Pred : ', pred)
    if param[-1]!=pred:
        solution(*param[:-1])



import numpy as np
import random
idx = 0
'''
제한사항
N: 200,000,000 이하의 자연수
stations의 크기: 10,000 이하의 자연수
stations는 오름차순으로 정렬되어 있고, 배열에 담긴 수는 N보다 같거나 작은 자연수입니다.
W: 10,000 이하의 자연수

'''
import math

def test(n, stations, w):
        
    return 0

while True:
    idx+=1
    N=random.randint(1,30)
    W = random.randint(1,10)
    tmp = [i*W for i in set(list(np.random.randint(1,N//W, size=random.randint(3,4))))]
    stations = sorted(tmp)
    print('{}번째 '.format(str(idx)))
    print('param : ',(N, stations, W))
    try:
        ans = test(N, stations, W)
        print('ans : ',ans)
        pred = solution(N, stations, W)
        print('pred : ',pred)
        if pred !=ans:
            solution(N, stations, W)
    except Exception as e:
        solution(N, stations, W)
