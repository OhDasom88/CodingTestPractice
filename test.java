import java.time.LocalDate;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.Map.Entry;

public class test {

    public static void main(String[] args) {

        Map<String, LocalDate> map = new HashMap<>();
        while(true){
            Scanner sc = new Scanner(System.in);
            System.out.println("Sign up: 1");
            System.out.println("Login : 2");
            String instruction = sc.next();
            if(instruction.equals("1")){
                System.out.print("Enter your id - ");
                String id = sc.next();
                if(map.containsKey(id)){
                    System.out.println("Sign up failed");
                    System.out.println("Duplicated id. Try Another");
                }else{
                    map.put(id, LocalDate.now());
                    System.out.println("Sign up succeeded");
                }
    
            }else if(instruction.equals("2")){
                System.out.print("Enter your id - ");
                String id = sc.next();
                if(map.containsKey(id)){
                    System.out.println("login succeeded");
                }else{
                    System.out.println("login failed");
                }
    
            }else{
                System.out.println("Wrong Instruction Try Again");
            }
            
            
        }
        // for (int i = 0; i < 50; i++) {
        //     map.put(i, Math.random()); 
        // }

        // Set<Entry<Integer, Double>> set = map.entrySet();
        // Iterator<Entry<Integer, Double>> it = set.iterator();
        // Integer count = 0;
        // while(it.hasNext()){
        //     Entry<Integer, Double> ent =  it.next();
        //     if (ent.getValue()<0.5) {
        //         count ++;
        //         System.out.print(ent.getKey());
        //         System.out.print(" : ");
        //         System.out.print(ent.getValue());
        //         System.out.println();
        //     }
        // }
        // System.out.println("Count : "+count);
        
    }
}