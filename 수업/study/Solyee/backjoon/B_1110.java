package backjoon;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class B_1110 {
    public static void main(String[] args) throws IOException {
        // scanner는 시간이 오래 걸림... 따라서 bufferedreader를 사용해야 시간초과가 안뜬다!!!
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        int new_num=num ;
        int count_num = 0;
        do {
            count_num++;
            num = ((num % 10) * 10) + (((num / 10) + (num % 10)) % 10);
        } while (new_num != num);
        System.out.println(count_num);
    }
}
