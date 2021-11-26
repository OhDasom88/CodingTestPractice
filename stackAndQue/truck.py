from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0 for i in range(bridge_length)])
    trucks  = deque(truck_weights)
    curWeight = 0
    while len(trucks) > 0 or curWeight > 0:
        answer+=1
        leaved = bridge.popleft()
        curWeight -= leaved
        if len(trucks) > 0:
            truck = trucks.popleft()
            if curWeight +truck <= weight:
                curWeight += truck
                bridge.append(truck)
            else:
                trucks.appendleft(truck)
                bridge.append(0)
    return answer

print(solution(2,10,[7,4,5,6]))#8
print(solution(100,100,[10]))#101
print(solution(100,100,	[10,10,10,10,10,10,10,10,10,10]))#110
print(solution(5,5,	[2, 2, 2, 2, 1, 1, 1, 1, 1]))#19
print(solution(5,5,	[1, 1, 1, 1, 1, 2, 2, 2, 2]))#19