'''
a, b, c, d 네 사람이 모여 커플 매칭 게임을 진행합니다.

커플 매칭 게임의 규칙은 다음과 같습니다.

커플 매칭 게임은 1개 이상의 라운드로 이루어져 있습니다.
참가자들은 매 라운드마다 커플이 되고 싶은 사람 한 명을 지목할 수 있습니다. 
단, 직전 라운드에서 자신과 커플이 됐던 사람이나 자기 자신을 지목하면 규칙을 어기게 됩니다.
같은 라운드에서 두 사람이 서로를 지목한 경우에 커플이 됩니다. 
단, 이번 라운드에서 규칙을 어긴 사람은 이번 라운드에서는 커플이 될 수 없습니다.

각 라운드의 게임 정보를 담고 있는 2차원 문자열 배열 rounds가 매개변수로 주어질 때, 
참가자들이 규칙을 총 몇 번 어겼는지 return 하도록 solution 함수를 작성해주세요.

제한사항
1 ≤ rounds의 길이 ≤ 20
rounds의 n번째 원소는 n번째 라운드를 의미합니다.
rounds[i]는 4개의 원소를 가지고 있습니다.
rounds[i]의 원소는 "a", "b", "c", "d" 중의 하나입니다.
rounds[i]의 첫 번째 원소는 a가 지목한 사람, 두 번째 원소는 b가 지목한 사람, 
세 번째 원소는 c가 지목한 사람, 네 번째 원소는 d가 지목한 사람을 의미합니다.
'''
def solution(rounds):
    matched = []
    offense = []
    for i, round in enumerate(rounds):
        matched.append({})
        offense.append(set())
        matching = {fro:to for fro, to in zip(['a','b','c','d'],round)}
        for fro, to in matching.items():
            if fro == to:
                offense[-1].add(fro)
            elif i>0 and fro in matched[i-1] and matched[i-1].get(fro) == to:
                offense[-1].add(fro)
            elif matching.get(to)==fro:
                matched[-1].update({fro:to})
        for off in offense[-1]:
            if off in matched[-1]:
                matched[-1].pop(off)
    return sum([len(off) for off in offense])

params = [
    [[["b", "a", "a", "d"],["b", "c", "a", "c"], ["b", "a", "d", "c"]],	2],
    [[["b", "a", "d", "c"],["b", "a", "c", "d"]],	4],
    [[["b", "a", "d", "c"],["d", "c", "b", "a"],["b", "a", "d", "c"]],	0],
    [[["d", "a", "a", "a"],["c", "a", "a", "a"],["b", "a", "a", "a"]],	2],
]

for param in params:
    print('param : ',param[0])
    print('ans : ',param[-1])
    pred = solution(param[0])
    print('pred : ',pred)
    if pred != param[-1]:
        solution(param[0])