import java.util.*;
import java.io.*;
import java.math.*;

class test {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        int m = 10000000;
        for (int i = 0; i < n; i++) {
            int t = in.nextInt();
            if (Math.abs(t) < Math.abs(m) || (Math.abs(t) == Math.abs(m) && t > m)) {
                m = t;
            }
        }

       System.out.println(n > 0 ? m : 0);
    }
}
