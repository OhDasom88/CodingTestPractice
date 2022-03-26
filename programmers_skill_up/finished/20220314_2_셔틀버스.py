'''
카카오에서는 무료 셔틀버스를 운행하기 때문에 판교역에서 편하게 사무실로 올 수 있다. 
카카오의 직원은 서로를 '크루'라고 부르는데, 아침마다 많은 크루들이 이 셔틀을 이용하여 출근한다.

이 문제에서는 편의를 위해 셔틀은 다음과 같은 규칙으로 운행한다고 가정하자.

셔틀은 09:00부터 총 n회 t분 간격으로 역에 도착하며, 하나의 셔틀에는 최대 m명의 승객이 탈 수 있다.
셔틀은 도착했을 때 도착한 순간에 대기열에 선 크루까지 포함해서 대기 순서대로 태우고 바로 출발한다. 
예를 들어 09:00에 도착한 셔틀은 자리가 있다면 09:00에 줄을 선 크루도 탈 수 있다.
일찍 나와서 셔틀을 기다리는 것이 귀찮았던 콘은, 일주일간의 집요한 관찰 끝에 
어떤 크루가 몇 시에 셔틀 대기열에 도착하는지 알아냈다. 
콘이 셔틀을 타고 사무실로 갈 수 있는 도착 시각 중 제일 늦은 시각을 구하여라.

단, 콘은 게으르기 때문에 같은 시각에 도착한 크루 중 대기열에서 제일 뒤에 선다.
 또한, 모든 크루는 잠을 자야 하므로 23:59에 집에 돌아간다. 따라서 어떤 크루도 다음날 셔틀을 타는 일은 없다.
'''

def solution(n, t, m, timetable):
    timetable = sorted(timetable, reverse=True)# 내림차순
    answer = ''
    for i in range(n-1):# 마지막 버스 대기 상황 파악
        bus = 9*60+i*t
        for j in range(m):
            if [int(k) for k in timetable[-1].split(':')] <= [bus//60, bus%60]:
                timetable.pop()# 탑승
                if len(timetable)==0:
                    break
        if len(timetable)==0:
            break

    last_bus = 9*60+(n-1)*t
    timetable = sorted([mt for mt in timetable if [int(k) for k in mt.split(':')] <= [last_bus//60, last_bus%60]])
    if len(timetable) < m:
        answer = f'{str(last_bus//60+100)[1:]}:{str(last_bus%60+100)[1:]}' 
    # elif len(timetable) == m:
    #     crew = [int(i) for i in timetable.pop().split(':')]
    #     crew = crew[0]*60 + crew[-1] - 1
    #     answer = f'{str(crew//60+100)[1:]}:{str(crew%60+100)[1:]}' 
    else:
        # tmp = timetable[:m]# 정원
        # last_crew = tmp.pop()
        # while last_crew == timetable[m] and len(last_crew)>0:
        #     last_crew = tmp.pop()
        crew = [int(i) for i in timetable[m-1].split(':')]
        crew = crew[0]*60 + crew[-1] - 1
        answer = f'{str(crew//60+100)[1:]}:{str(crew%60+100)[1:]}' 
            
    return answer

# from collections import defaultdict
# def solution(n:int, t:int, m:int, timetable:list):
#     answer = None
#     timetable = sorted(timetable, reverse=True)
#     for i in range(n):#셔틀 운행 횟수 n
#         bus = 9*60 + i*t#셔틀 운행 간격 t
#         crew = set()
#         for j in range(m):# 한 셔틀에 탈 수 있는 최대 크루 수 m
#             hours, mins = timetable[-1].split(':')
#             if bus >= int(hours)*60+int(mins):
#                 crew.add(timetable.pop())
#                 if len(timetable)==0:
#                     if j<m-1:# 버스에 여석이 있을때
#                         answer = f'{str(bus//60+100)[1:]}:{str(bus%60+100)[1:]}' 
#                     elif i==n-1:# 버스에 여석이 없을때 + 다음버스가 없을때
#                         if len(crew) > 1:
#                             crew = sorted(crew)
#                             answer = crew.pop(-2)
#                         else:#재일먼저와야 탈수 있음
#                             hours, mins = crew.pop().split(':')
#                             ti = int(hours)*60+int(mins)-1
#                             answer = f'{str(ti//60+100)[1:]}:{str(ti%60+100)[1:]}' 
#                     break
#             else:
#                 break
#         if answer: 
#             break
#     if not answer:
#         answer = f'{str(bus//60+100)[1:]}:{str(bus%60+100)[1:]}'
#     return answer
'''
출력 형식
콘이 무사히 셔틀을 타고 사무실로 갈 수 있는 제일 늦은 도착 시각을 출력한다. 
도착 시각은 HH:MM 형식이며, 00:00에서 23:59 사이의 값이 될 수 있다.

입력 형식
셔틀 운행 횟수 n, 셔틀 운행 간격 t, 한 셔틀에 탈 수 있는 최대 크루 수 m
, 크루가 대기열에 도착하는 시각을 모은 배열 timetable이 입력으로 주어진다.

0 ＜ n ≦ 10
0 ＜ t ≦ 60
0 ＜ m ≦ 45

timetable은 최소 길이 1이고 최대 길이 2000인 배열로
, 하루 동안 크루가 대기열에 도착하는 시각이 HH:MM 형식으로 이루어져 있다.
크루의 도착 시각 HH:MM은 00:01에서 23:59 사이이다.

'''
params = [[1,1,5,["08:00", "08:01", "08:02", "08:03"],"09:00"]
, [2,10,2,["09:10", "09:09", "08:00"],"09:09"]
, [2,1,2,["09:00", "09:00", "09:00", "09:00"],"08:59"]
, [1,1,5,["00:01", "00:01", "00:01", "00:01", "00:01"],"00:00"]
, [1,1,1,["23:59"],"09:00"]
, [10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"],"18:00"]
, [1,10,3,["08:55", "08:55", "08:59"],"08:58"]
, [10, 25, 1, { "09:00", "09:10" ,"09:20" ,"09:30" ,"09:40" ,"09:50", "10:00", "10:10" ,"10:20" ,"10:30" ,"10:40" ,"10:50" }, "10:29"]
]
for i, param in enumerate(params):
    print('param : ',param[:-1])
    print('ans : ',param[-1])
    pred = solution(*param[:-1])
    print('pred : ',pred)
    
    if pred!=param[-1]:
        solution(*param[:-1])

import numpy as np
import random
idx = 0
while True:
    works = list(np.random.randint(1,5, size=random.randint(4,5)))
    n=random.randint(1,100)
    idx+=1
    n = random.randint(1,10)
    t = random.randint(1,60)
    m = random.randint(1,45)
    timetable = ['{0}:{1}'.format(str(random.choice([i for i in range(0,24)])+100)[1:], str(random.choice([i for i in range(0,60)])+100)[1:]) for _ in range(random.randint(1,20))]
    print('{}번째 '.format(str(idx)))
    print('param : ',(n, t, m, timetable))
    try:
        pred = solution(n, t, m, timetable)
        print('pred : ',pred)
    except Exception as e:
        solution(n, t, m, timetable)

    # if solution(n, works.copy()) !=test(n, works.copy()):
    #     print(solution(n, works.copy()))
    #     print(test(n, works.copy()))
    #     solution(n,works.copy())



# ans = solution(4, [4, 3, 3])#12
# print(ans)
# ans = solution(1, [2, 1, 2])#6
# print(ans)
# ans = solution(3, [1,1])#0
# print(ans)