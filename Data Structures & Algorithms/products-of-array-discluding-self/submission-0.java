class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prevProduct = new int[nums.length];
        prevProduct[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            prevProduct[i] = prevProduct[i - 1] * nums[i - 1];
        }
        int rightProduct = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            int temp = nums[i];
            nums[i] = rightProduct * prevProduct[i];
            rightProduct *= temp;
        }
        return nums;
    }
}  
