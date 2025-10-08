class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
       int n = nums.size();
        vector<int> answer(n, 1);
        
        // prefix products
        int pre = 1;
        for (int i = 0; i < n; i++) {
            answer[i] = pre;
            pre *= nums[i];
        }

        // suffix products
        int suf = 1;
        for (int i = n - 1; i >= 0; i--) {
            answer[i] *= suf;
            suf *= nums[i];
        }

        return answer; 
    }
};