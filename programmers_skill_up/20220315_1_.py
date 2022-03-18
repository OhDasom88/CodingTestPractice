'''
다음과 같은 것들을 정의합니다.

어떤 수열 x의 부분 수열(Subsequence)이란
, x의 몇몇 원소들을 제거하거나 그러지 않고 남은 원소들이 원래 순서를 유지하여 얻을 수 있는 새로운 수열을 말합니다.

예를 들어, [1,3]은 [1,2,3,4,5]의 부분수열입니다. 원래 수열에서 2, 4, 5를 제거해서 얻을 수 있기 때문입니다.

다음과 같은 조건을 모두 만족하는 수열 x를 스타 수열이라고 정의합니다.

x의 길이가 2 이상의 짝수입니다. (빈 수열은 허용되지 않습니다.)
x의 길이를 2n이라 할 때, 다음과 같은 n개의 집합 {x[0], x[1]}, {x[2], x[3]}, ..., {x[2n-2], x[2n-1]} 의
 교집합의 원소의 개수가 1 이상입니다.
x[0] != x[1], x[2] != x[3], ..., x[2n-2] != x[2n-1] 입니다.
예를 들어, [1,2,1,3,4,1,1,3]은 스타 수열입니다.
 {1,2}, {1,3}, {4,1}, {1,3} 의 교집합은 {1} 이고, 각 집합 내의 숫자들이 서로 다르기 때문입니다.

1차원 정수 배열 a가 매개변수로 주어집니다. 
a의 모든 부분 수열 중에서 가장 길이가 긴 스타 수열의 길이를 return 하도록 solution 함수를 완성해주세요. 
이때, a의 모든 부분 수열 중에서 스타 수열이 없다면, 0을 return 해주세요.
'''
from itertools import combinations
def test(a):
    answer = 0
    if len(a)>=2:
        for starsize in range(len(a)//2*2,1,-2):
            for star in combinations(a,starsize):
                intersec = None
                for i in range(0, len(star)-1,2):
                    el1, el2 = star[i], star[i+1] 
                    if el1 != el2:
                        if intersec:
                            intersec = intersec.intersection(set([el1, el2]))
                            if len(intersec)==0:
                                intersec = None
                                break
                        else:
                            intersec = set([el1, el2])
                    else:
                        intersec = None
                        break
                if intersec:
                    answer = starsize
                    break
            if answer!=0:
                break
    return answer
params = [ [[0], 0]
, [[5,2,3,3,5,3], 4]
, [[0,3,3,0,7,2,0,2,2,0], 8]]
for i, param in enumerate(params):
    print(i)
    if test(*param[:-1]) != param[-1]:
        print('ans : ',param[-1])
        print('res : ', test(*param[:-1]))
        test(*param[:-1])
    
def solution(a:list):
    answer = 0
    cache = {}
    def sol(ab:list,inter:set):
        ans = 0
        ab.reverse()
        for i in range(len(ab)):
            ar=ab[i:]
            ar.reverse()
            tmp = []
            el1 = ar.pop()
            tmp.append(el1)
            while len(ar) > 0:
                el2=ar.pop()
                if el1!=el2:
                    tmp.append(el2)
                    break
            if len(tmp)==2:
                if len(inter.intersection(tmp))>0:
                    star = 1
                    if len(ar)>1:
                        key = (tuple(ar),tuple(inter.intersection(tmp)))
                        if key in cache:
                            star += cache.get(key)
                        else:
                            cache.update({key:sol(ar, inter.intersection(tmp))})
                            star += cache.get(key)
                    if ans < star:
                        ans = star
        return ans
    for i in range(len(a)):
        b = a[i:]
        b.reverse()
        el1 = b.pop()
        el2 = None
        while len(b)>0:
            el2 = b.pop()
            if el1!=el2:
                break
            else:
                el2 = None
        if el2 is not None:
            starsize = 1
            if len(b)>1:
                starsize += sol(b.copy(),set([el1,el2]))
            if answer < starsize:
                answer = starsize
    return answer*2

import numpy as np
import random
idx = 0
while True:
    target = 15
    a = list(np.random.randint(0,target, size=target))
    # n=random.randint(1,100)
    idx+=1
    print('{}번째 '.format(str(idx)))
    if solution(a.copy()) !=test(a.copy()):
        print('param : ', a)
        print('ans : ',test(a.copy()))
        print('wrong : ',solution(a.copy()))
        print('ans : ',test(a.copy()))
        print('wrong : ',solution(a.copy()))



# ans = solution(4, [4, 3, 3])#12
# print(ans)
# ans = solution(1, [2, 1, 2])#6
# print(ans)
# ans = solution(3, [1,1])#0
# print(ans)