class Solution {
public:
    int healper(int i , vector<int>&v , int sum , int n , int &k){
        if(i == v.size() || sum == n){
            if(k >= 2)
                return 1;
            return 0;
        }

        int nottake = healper(i+1,v,sum,n,k);
        int take = 1;
        if(sum + v[i] <= n){
            k++;
            take = v[i]*healper(i,v,sum+v[i],n,k);
        }

        return max(take,nottake);
    }
    int integerBreak(int n) {
        vector<int> v;
        for(int i=1; i<=n; i++)
            v.push_back(i);
        int k = 0;
        return healper(0,v,0,n,k);
    }
};
