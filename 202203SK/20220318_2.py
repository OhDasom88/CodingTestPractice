'''

'''
params = [
[["1","2","4","3","3","4","1","5"], ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"], ["24","3415","4922","12492215","13"]]
, [["1","1","1","1","1","1","1"], ["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"], ["338","38","8888","3385551","38555","29"]]
]
def solution(arr:list, processes:list):
    answer = []
    cate,t1,t2,A,B,C = None,0,0,0,0,0
    pTime=0
    processes.reverse()
    tmp = processes.pop()
    if tmp[0]=='r':
        cate, t1,t2,A,B = tmp.split()
        answer.append(arr[A:B])
        if t1+t2 > pTime:
            pTime = t1+t2
    else:
        cate, t1,t2,A,B,C = tmp.split()
        arr[A:B] = C
        if t1+t2 > pTime:
            pTime = t1+t2
    wating = []
    while len(processes)>0:
        tmp1 = processes.pop()
        if len(wating)==0:
            if tmp1[0]=='r':
                cate,t1,t2,A,B = tmp1.split()
                answer.append(arr[A:B])
                if t1+t2 > pTime:
                    pTime = t1+t2
            else:
                cate,t1,t2,A,B,C = tmp1.split()
                arr[A:B] = C
                if t1+t2 > pTime:
                    pTime = t1+t2
            
        # while tmp[-1][1]==processes[-1].split()[1]:# 동시에 들어온 요청
        #     tmp.append()
        # tmp = sorted(tmp)# w를 뒤로 
        # while len(tmp)>0:
        #     process = tmp.pop()
            # if tmp1[-1][0]=='w':
            #     tmp2.append(tmp1.pop())
            # if tmp1[-1][0]=='r':
            #     t1,t2,A,B = tmp1[-1].split()
            #     answer.append(arr[A:B])
            #     if t1+t2 > pTime:
            #         pTime = t1+t2
        
    return answer

for param1, param2, ans in params:
    print('param1 : ',param1)
    print('param2 : ',param2)
    print('ans : ',ans)
    pred = solution(param1, param2)
    print('pred : ',pred)
    if ans != pred:
        solution(param1, param2)
    