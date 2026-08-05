import java.util.Scanner;

class Solution {
    public String toLowerCase(String s) {
        System.out.println(s.toLowerCase());
        return s.toLowerCase(); 
        
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("s = " );
        String a = sc.nextLine();
        Solution sols = new Solution();
        sols.toLowerCase(a);
  
    }
}
