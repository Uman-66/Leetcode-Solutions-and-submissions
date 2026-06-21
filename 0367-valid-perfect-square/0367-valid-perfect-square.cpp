class Solution {
public:
    bool isPerfectSquare(int num) {
        int l = 0, r = num;
        long ans = 0 , mid = 0;
        while(l <= r){
            mid = l + (r-l)/2;
            if(mid*mid == num){
                return true;
            }
            if(mid*mid < num){
                ans = mid;
                l = mid+1;
            }
            else{
                r = mid-1;
            }

        }
        return false;
    }
};