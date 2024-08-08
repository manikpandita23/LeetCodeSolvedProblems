class Solution {
public:
    vector<vector<int>> spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        vector<vector<int>> result;
        vector<vector<int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int steps = 1;
        int dir = 0;
        result.push_back({rStart, cStart});
        int totalCells = rows*cols;
        while(result.size()<totalCells){
            for (int i =0; i<2; ++i){
                for (int j=0; j<steps; ++j){
                    rStart +=directions[dir][0];
                    cStart +=directions[dir][1];
                    if (rStart>=0 && rStart<rows && cStart>=0 && cStart<cols){
                        result.push_back({rStart, cStart});
                    }
                }
                dir = (dir+1)%4;
            }
            ++steps;
        }
        return result;
    }
};
