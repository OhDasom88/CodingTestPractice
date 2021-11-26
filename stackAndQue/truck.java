package stackAndQue;

import java.util.LinkedList;

public class truck {
    public static void main(String[] args) {
        Solution1 sol = new Solution1();
        System.out.println(sol.solution(2, 10, new int[]{7,4,5,6}));// 8
        System.out.println(sol.solution(100, 100, new int[]{10}));// 101
        System.out.println(sol.solution(100, 100, new int[]{10,10,10,10,10,10,10,10,10,10}));// 110
    }
    
}

class Solution1 {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;

        LinkedList<Integer> bridge = new LinkedList<>();
        for (int i = 0; i < bridge_length; i++) {
            bridge.add(0);
        }

        LinkedList<Integer> trucks = new LinkedList<>();
        for (int i = 0; i < truck_weights.length; i++) {
            trucks.add(truck_weights[i]);
        }

        int curWeight = 0;
        while (trucks.size()>0 || curWeight >0) {
            answer += 1;
            int leaved = bridge.pollFirst();
            curWeight -= leaved;
            if (trucks.size() > 0) {
                int truck = trucks.pollFirst();
                if (curWeight + truck <= weight) {
                    curWeight += truck;
                    bridge.add(truck);
                }else{
                    trucks.addFirst(truck);
                    bridge.add(0);
                }
            }
        }
        return answer;
    }
}