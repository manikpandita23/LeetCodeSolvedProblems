class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        evens = 0
        for num in nums:
            if not num & 1:
                evens += 1
                if evens >= 2:
                    return True
        return False
