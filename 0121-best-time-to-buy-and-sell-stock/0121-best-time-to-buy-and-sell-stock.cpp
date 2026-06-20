class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min = INT_MAX;
        int profit = 0;
        for(int val : prices){
            if(val < min){
                min = val;
            }
           if ((val - min) > profit){
                profit = val - min;
           }
        }
    return profit;
    }
};