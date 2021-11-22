from collections import defaultdict

def solution(genres, plays):
    answer = []
    d = defaultdict(int)
    for i in range(len(plays)):
        d[genres[i]]+=plays[i] 

    tmp = None
    cnt = 0
    for i in sorted([[-d.get(genres[i]), -plays[i], i] for i in range(len(plays))], key=lambda item : item):
        
        if tmp and tmp == i[0] and cnt >=2:
            continue
        elif tmp and tmp != i[0]:
            cnt = 0
        tmp = i[0]
        cnt += 1
        answer.append(i[-1])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500], ))# [4, 1, 3, 0]