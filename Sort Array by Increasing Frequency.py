from typing import List
from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        nums.sort(key=lambda x: (freq[x], -x))
        return nums
sol = Solution()
nums1 = [1, 1, 2, 2, 2, 3]
print(sol.frequencySort(nums1))  
nums2 = [2, 3, 1, 3, 2]
print(sol.frequencySort(nums2))  
nums3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
print(sol.frequencySort(nums3))  
