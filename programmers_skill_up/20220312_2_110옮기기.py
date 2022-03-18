'''
0과 1로 이루어진 어떤 문자열 x에 대해서, 
당신은 다음과 같은 행동을 통해 x를 최대한 사전 순으로 앞에 오도록 만들고자 합니다.

x에 있는 "110"을 뽑아서, 임의의 위치에 다시 삽입합니다.
예를 들어, x = "11100" 일 때, 여기서 중앙에 있는 "110"을 뽑으면 x = "10" 이 됩니다. 
뽑았던 "110"을 x의 맨 앞에 다시 삽입하면 x = "11010" 이 됩니다.

변형시킬 문자열 x가 여러 개 들어있는 문자열 배열 s가 주어졌을 때, 
각 문자열에 대해서 위의 행동으로 변형해서 만들 수 있는 문자열 중 
사전 순으로 가장 앞에 오는 문자열을 배열에 담아 return 하도록 solution 함수를 완성해주세요.
'''
def solution(s:list):
    cache = {}
    def sol(target:str):
        cnt = target.count('110')
        if cnt ==0:
            return target, 0
        else:
            idx = target.find('110')
            while idx!=-1:
                target = target[:idx]+target[idx+3:]
                idx = target.find('110')
            if target not in cache:
                cache.update({target: sol(target)})
            newT, newCnt = cache.get(target)
            return newT, newCnt+cnt
    answer = []
    for string in s:
        if string not in cache:
            cache.update({string: sol(string)})
        target, cnt = cache.get(string)
        idx = target.find('1'*min(2,len(target)))
        temp = ''
        if idx ==-1 :
            if target[idx] =='1':
                temp = target[:idx]+'110'*cnt+target[idx]
            else:
                temp = target + '110'*cnt
        else:
            temp = target[:idx] + '110'*cnt + target[idx:]
        answer.append(temp)
    return answer
params = [('110','110'),('0101110','0101101'),("0111111010","0110110111"),('101110110','101101101'),("1110","1101"),("100111100","100110110")]
for param, ans in params:
    print('param: ', param)
    print('ans: ', ans)
    print('pred: ', solution([param])[0])
    if ans != solution([param])[0]:
        print(solution([param])[0])
