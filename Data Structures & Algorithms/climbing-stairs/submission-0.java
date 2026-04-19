class Solution {
    public int climbStairs(int n) {
       int curr = 0;
       int dp1 = 1;
       int dp2 = 0;
       for (int i = n; i >= 1; i--) {
            curr = dp1 + dp2;
            dp2 = dp1;
            dp1 = curr;
            curr = 0;
       }
       return dp1;
    }
}
