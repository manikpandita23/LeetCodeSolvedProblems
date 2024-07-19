class Solution:
    def luckyNumbers(self, matrix):
        min_in_rows = {min(row) for row in matrix}
        max_in_columns = {max(col) for col in zip(*matrix)}
        lucky_nums = min_in_rows & max_in_columns
        return list(lucky_nums)
sol = Solution()
matrix1 = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
print(sol.luckyNumbers(matrix1))  
matrix2 = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
print(sol.luckyNumbers(matrix2))  
matrix3 = [[7, 8], [1, 2]]
print(sol.luckyNumbers(matrix3))  
