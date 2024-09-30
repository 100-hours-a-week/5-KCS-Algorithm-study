import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] arr = new int[M];

        for (int i=0; i<M; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        int left = 0;
        int right = arr[arr.length-1];
        int m, sum, answer = 0;
        while (left <= right) {
            m = (left + right) / 2;
            sum = 0;

            for(int i=0; i<M; i++) {
                if (arr[i] % m == 0) {
                    sum += arr[i] / m;
                } else {
                    sum += arr[i] / m + 1;
                }
            }

            if (sum > N) {
                left = m + 1;
            }
            else {
                right = m - 1;
                answer = m;
            }
        }

        System.out.println(answer);
    }
}