/**
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한 조건
n은 1이상 8000000000 이하인 자연수입니다.
*/

class Solution {
      public long solution(long n) {
          long answer = 0;
          int[] arr = longToArr(n);
          arr=sort(arr);
          answer = arrToNum(arr);


          return answer;
      }

      int[] longToArr(long n){
          int len=0;
          long m=n;
          while(true){
              n=(int)(n/10);
              len++;
              if(n==0){
                  break;
              }

          }// while

          int[] arr = new int[len];
          for(int i=0;i<len;i++){
              arr[i]=(int)(m%10);
              m=m/10;
          }
          return arr;
      }

      int[] sort(int[] arr){

          for(int i=1;i<arr.length;i++){
              for(int j=i;j>0;j--){
                  int temp = arr[j];
                  if(arr[j]>arr[j-1]){
                      arr[j]=arr[j-1];
                      arr[j-1]=temp;
                  }
              }// for
          }// for

          return arr;
      }

      long arrToNum(int[] arr){
          long num =0l;
          for(int i=0; i<arr.length;i++){
              num = num*10+arr[i];
          }// for
          return num;
      }
    }// class