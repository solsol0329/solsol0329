package backjoon;

import java.util.Arrays;
import java.util.Scanner;

public class B_1037 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int [] arr = new int [num];
        for (int i = 0; i < num; i++) {
            arr[i] = sc.nextInt();
        }
        Arrays.sort(arr);
        if (num==1) {
            System.out.println(arr[0]*arr[0]);
        } else {
            System.out.println(arr[0]*arr[num-1]);
        }
    }
}
