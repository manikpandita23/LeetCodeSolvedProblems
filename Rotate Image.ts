/**
 Do not return anything, modify matrix in-place instead.
 */
function rotate(matrix: number[][]): void {
    const n = matrix.length;
    const m = matrix[0].length;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j <= i; j++) {
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]]
        }
    }
    for (let i = 0; i < n; i++) {
        matrix[i].reverse();
    }

};
