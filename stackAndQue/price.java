package stackAndQue;

public class price {
    public static void main(String[] args) {
        Solution sol  = new Solution();
        System.out.println(sol.solution(new int[]{1, 2, 3, 2, 3}));//[4, 3, 1, 1, 0]
    }
    
}
class Solution {
    public int[] solution(int[] prices) {
    	// List<Integer> list = new LinkedList<Integer>();
    	int[] answer = new int[prices.length];
    	for(int i=0;i<prices.length;i++){
        	for(int j=i+1;j<prices.length;j++){
        		if(prices[i]>prices[j] || j==prices.length-1){
        			answer[i]=(j-i);
                    break;
        		}
        	}
        }
    	
        return answer;
    }
}
