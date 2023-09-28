// problem without if else, switch case

import java.util.Scanner;

class LemonsProblem {
    public static void main(String ar[]) {
        Scanner s = new Scanner(System.in);
        try {
            int n = s.nextInt();
            int tot = 21;
            int num = (n < 0) ? -1 : tot - n;
            System.out.println((num < 0) ? "not valid number" : num);
        } catch (Exception e) {
            System.out.println("Enter a valid number not a character");
        }
        s.close();
    }
}
