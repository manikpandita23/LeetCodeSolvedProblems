class Solution {
public:
    bool isMagic(vector<vector<int>>& grid, int row, int col) {
        vector<int> count(10, 0); 
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                int num = grid[row + i][col + j];
                if (num < 1 || num > 9 || count[num] > 0)
                    return false;
                count[num]++;
            }
        }

        int sum = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]; // the sum of the first row
        
        
        for (int i = 0; i < 3; ++i) {
            if (grid[row + i][col] + grid[row + i][col + 1] + grid[row + i][col + 2] != sum)
                return false;
        }

       
        for (int j = 0; j < 3; ++j) {
            if (grid[row][col + j] + grid[row + 1][col + j] + grid[row + 2][col + j] != sum)
                return false;
        }

        
        if (grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2] != sum)
            return false;
        if (grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col] != sum)
            return false;

        return true;
    }

    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int rows = grid.size(), cols = grid[0].size();
        int count = 0;

   
        for (int i = 0; i <= rows - 3; ++i) {
            for (int j = 0; j <= cols - 3; ++j) {
                if (isMagic(grid, i, j)) {
                    count++;
                }
            }
        }

        return count;
    }
};
