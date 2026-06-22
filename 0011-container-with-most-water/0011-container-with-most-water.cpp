class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0 ,n = height.size() ,r = n-1, maxx= INT_MIN;
        while(l<r){
            int w = r - l;
            int h = min(height[l], height[r]);
            int curr = w * h;
            maxx = max(maxx, curr) ;
            if(height[l] < height[r]){
                l++;
            }
            else{
                r--;
            }

        }
        return maxx;
    }
};