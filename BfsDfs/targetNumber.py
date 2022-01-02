from itertools import product
def solution(numbers, target):
    '''
    사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
    '''
    answer = 0
    for operations in product([-1,1], repeat=len(numbers)):
        if sum([op*number for op, number in zip(operations, numbers)]) == target: answer +=1            
    return answer