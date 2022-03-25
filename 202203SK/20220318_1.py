'''

'''
params = [ [["pencil","cilicon","contrabase","picturelist"], ["en nc pe","ico ili lic","a b","u"]]
, [["abcdeabcd","cdabe","abce","bcdeab"], ["abcd eabc","be da","ce","None"]]]


from collections import defaultdict
def solution(goods):
    def sol(good:str, num:int):
        if len(good) ==num+1: 
            return 'None'
        tmp = set()
        for i in range(0,len(good)-num+1):
            key = good[i:i+num]
            cnt = 0
            for g in goods:
                if key in g:
                    cnt +=1
                    if cnt >1:
                        break
            if cnt ==1:
                tmp.add(key)
        if len(tmp) ==0:
            return sol(good, num+1)
        else:
            return ' '.join(sorted(tmp))
    answer = []
    for good in goods:
        answer.append(sol(good,1))
    return answer
for param, ans in params:
    print('param : ',param)
    print('ans : ',ans)
    pred = solution(param)
    print('pred : ',pred)
    if ans != pred:
        solution(param)
    