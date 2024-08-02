class Solution {
    public int minSwaps(int[] nums) {
        int n = nums.length;
        int k = 0;
        for (int num : nums) {
            if (num == 1) k++;
        }
        if (k == 0 || k == n) return 0;
        int currentZeros = 0;
        for (int i = 0; i < k; i++) {
            if (nums[i] == 0) currentZeros++;
        }
        
        int minZeros = currentZeros;
        for (int i = 1; i < n; i++) {
            if (nums[i - 1] == 0) currentZeros--; 
            if (nums[(i + k - 1) % n] == 0) currentZeros++;
            minZeros = Math.min(minZeros, currentZeros);
        }
        return minZeros;
    }
}
