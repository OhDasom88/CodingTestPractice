from collections import defaultdict
def solution(n, recipes, orders):
    answer = 0

    recipeDic = defaultdict(int)
    for recipe in recipes:
        title, time = recipe.split()
        recipeDic[title] = int(time)
    # workers = defaultdict(int)
    workers = [0 for i in range(n)]
    for i, order in enumerate(orders):
        orderTitle, orderTime = order.split()
        orderTime = int(orderTime)
        nextWorker = workers.index(min(workers))
        if workers[nextWorker] < orderTime:
            workers[nextWorker] = orderTime + recipeDic[orderTitle]
        else:
            workers[nextWorker] += recipeDic[orderTitle]
        if i == len(orders)-1:
            answer = workers[nextWorker]
    return answer
print(solution(2, ["A 3","B 2"], ["A 1","A 2","B 3","B 4"]))#   7
print(solution(3, ["SPAGHETTI 3", "FRIEDRICE 2", "PIZZA 8"], ["PIZZA 1", "FRIEDRICE 2", "SPAGHETTI 4", "SPAGHETTI 6", "PIZZA 7", "SPAGHETTI 8"]))#12
print(solution(1, ["COOKIE 10000"], ["COOKIE 300000"]))# 310000