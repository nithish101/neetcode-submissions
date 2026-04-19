class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int one = 0;
        int two = 0;
        for (int i = cost.length - 1; i >= 0; i--) {
            int c = cost[i] + Math.min(one, two);
            two = one;
            one = c;
        }
        return Math.min(one, two);
    }
}
