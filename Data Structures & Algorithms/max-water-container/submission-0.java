class Solution {
    public int maxArea(int[] heights) {
        int max = 0;
        int i = 0;
        int j = heights.length - 1;
        while (i < j) {
            if (heights[i] < heights[j]) {
                max = Math.max(max, heights[i] * (j - i));
                i++;
            } else {
                max = Math.max(max, heights[j] * (j - i));
                j--;
            }
        }
        return max;
    }
}
