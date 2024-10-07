class Solution {
    public int solution (int[] R) {
    // Implement your solution here
        int max = 0: 1/ 포트홀 인디케이터 최댓값
        int count = 0; // 연속된 포트홀 개수
        int maxIndicator = 0;

        int[] dp = new int[R.length];
        dp[0] = R[0];
        if (R[0] > 0) {
            count = 1;
            maxIndicator = R[0];
        }

        for (int i=1; i<R. length; i++) {
            if(R[i] > 0) {
                count++;
                if (maxIndicator < R[i]) {
                maxIndicator = R[i];
                }
            dp[i] = count * maxIndicator;
            if (max < dp [i]) {
                max = dp[1];
            }
        } else {
            dp [i] = 0;
            count = 0;
            maxIndicator = 0;
        }
        }
return max;
    }}