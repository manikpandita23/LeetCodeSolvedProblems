class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        return self.solve(heights, 0, bricks, ladders)

    def solve(self, heights: List[int], i: int, bricks: int, ladders: int) -> int:
        if i == len(heights) - 1:
            return i
        diff = heights[i + 1] - heights[i]
        if diff > 0:
            ans = i
            if bricks >= diff:
                ans = max(ans, self.solve(heights, i + 1, bricks - diff, ladders))
            if ladders > 0:
                ans = max(ans, self.solve(heights, i + 1, bricks, ladders - 1))
            return ans
        else:
            return self.solve(heights, i + 1, bricks, ladders)
