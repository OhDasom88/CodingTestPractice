package heap;

import java.util.Collections;
import java.util.LinkedList;
import java.util.concurrent.ThreadLocalRandom;
class Solution {
    public int insertNumInArr(LinkedList<Integer> list, int index, int target) {
        int numToCompare = list.get(index);
        int idx = -1;
        if (numToCompare<target) {
            if (list.size()-1==index||list.get(index+1)>=target) {
                idx = index+1;
            }else{
                idx = insertNumInArr(list, ((index + index/2) == index)? index+1: index + index/2, target);
            }
        }else if(target<numToCompare){
            if (0==index||list.get(index-1)<=target) {
                idx = index;                    
            }else{
                idx = insertNumInArr(list, (index/2 == index)? index-1: index/2, target);
            }
        }else{
            idx = index;
        };
        return idx;
    }

    public int solution(int[] scoville, int K) {
        int answer = 0;
        LinkedList<Integer> list = new LinkedList<>();
        for (int i = 0; i < scoville.length; i++) {
            list.add(scoville[i]);
        }
        Collections.sort(list);
        while (list.size()>=2 && list.getFirst()<K) {
            int target = list.pop()+2*list.pop();
            if (list.size()>0) {
                int index = insertNumInArr(list, list.size()/2, target);
                list.add(index, target);
            }else{
                list.add(target);
            }
            answer += 1;
        }
        if(list.size() < 2){
            return (list.pop() > K) ? answer : -1;
        }else{
            return answer;
        }
    }

    public int answer(int[] scoville, int K) {
        int answer = 0;
        LinkedList<Integer> list = new LinkedList<>();
        for (int i = 0; i < scoville.length; i++) {
            list.add(scoville[i]);
        }
        Collections.sort(list);
        while (list.size()>=2 && list.getFirst()<K) {
            int tmp = list.pop()+2*list.pop();
            if (list.size()>0) {
                
                for (int i = 0; i < list.size(); i++) {
                    if (list.get(i)>=tmp) {
                        list.add(i, tmp);
                        tmp = -1;
                        break;
                    };
                }
                if (tmp!=-1) {
                    list.add(tmp);
                }
            }else{
                list.add(tmp);
            }
            answer += 1;
            // Collections.sort(list);
        }
        if(list.size() < 2){
            return (list.pop() > K) ? answer : -1;
        }else{
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int [] scoville = null;
        // System.out.println(sol.answer(scoville, 7)); // 2
        // System.out.println(sol.solution(scoville, 7)); // 2
        ThreadLocalRandom rd = ThreadLocalRandom.current();
        while (true) {
            // scoville = new int[rd.nextInt(2, 1000000)];
            scoville = new int[rd.nextInt(2, 10)];
            for (int i = 0; i < scoville.length; i++) {
                scoville[i] = rd.nextInt(10);
            }
            int k = rd.nextInt(100);
            System.err.println(scoville.toString());
            System.err.println(sol.answer(scoville, k));
            // if (sol.answer(scoville, k) != sol.solution(scoville, k)) {
            //     System.out.println();
            // }
        }
    }
}

