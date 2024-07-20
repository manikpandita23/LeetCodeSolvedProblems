class Solution:
    def restoreMatrix (self, rowSum, colSum):
        m, n = len(rowSum), len(colSum)
        matrix = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                val = min(rowSum[i], colSum[j])
                matrix [i][j] = val
                rowSum[i]-=val
                colSum[j]-=val
        return matrix
sol = Solution()
rowSum1 = [3, 8]
colSum1 = [4, 7]
print(sol.restoreMatrix(rowSum1, colSum1))

rowSum2 = [5, 7, 10]
colSum2 = [8, 6, 8]
print(sol.restoreMatrix(rowSum2, colSum2))
