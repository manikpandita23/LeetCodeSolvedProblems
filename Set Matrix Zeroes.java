class Solution {
    public void setZeroes(int[][] matrix) {
        ArrayList<Integer> zero = new ArrayList<>();
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[0].length;j++){
                if(matrix[i][j]==0){
                    zero.add(i);
                    zero.add(j);
                }
            }
        }
        for(int r=0;r<zero.size();r=r+2){
            int fir=zero.get(r), sec=zero.get(r+1);
            for(int i=0;i<matrix.length;i++){
                for(int j=0;j<matrix[0].length;j++){
                    if(i==fir){
                        matrix[i][j]=0;
                    }
                    if(j==sec){
                        matrix[i][j]=0;
                    }
                }
            }
        }
    }
}
