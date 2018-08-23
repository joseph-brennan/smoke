import java.util.*;
import java.io.*;
import java.math.*;

class test {

    static int comp(int val) {
        return val*val*val*val-val;
    }

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        int m = 274;
        for (int i = 0; i < n; i++) {
            int t = in.nextInt();
            if (comp(t) < comp(m)) {
                m = t;
            }
        }

       System.out.println(n > 0 ? -m : 0);
    }
}
