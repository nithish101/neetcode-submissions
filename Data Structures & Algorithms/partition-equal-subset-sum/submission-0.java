class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        if (sum % 2 == 1) {
            return false;
        }
        int target = sum / 2;
        HashSet<Integer> dp = new HashSet<>();
        dp.add(0);
        for (int num : nums) {
            HashSet<Integer> temp = new HashSet<>();
            for (int i : dp) {
                if (i + num == target) {
                    return true;
                }
                temp.add(i + num);
            }
            for (int i : temp) {
                dp.add(i);
            }
        }
        return false;
    }
}
