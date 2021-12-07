from math import sqrt
def solution(brown, yellow):
    target = (brown-4)/2
    for num in range(1, yellow+1):
        if yellow%num == 0 and target == num + yellow/num:
            return [yellow//num+2,num+2]

print(solution(10, 2))# [4,3]
print(solution(8, 1))# [3,3]
print(solution(24, 24))# [8,6]