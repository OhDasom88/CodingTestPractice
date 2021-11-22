from collections import defaultdict


def solution(clothes):
    answer = 1
    items = defaultdict(list)
    for el in clothes:
        items[el[-1]].append(el[0])

    for v in items.values():
        answer *= len(v)+1
    return answer -1

'''
스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.
ㄴ제한사항
    clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
    스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
    같은 이름을 가진 의상은 존재하지 않습니다.
    clothes의 모든 원소는 문자열로 이루어져 있습니다.
    모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
    스파이는 하루에 최소 한 개의 의상은 입습니다.
''' 
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))# 5
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))# 3