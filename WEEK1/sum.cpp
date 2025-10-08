class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int lhs = 0;
        int rhs = numbers.size() - 1;
        
        while (lhs < rhs) {
            int totalSum = numbers[lhs] + numbers[rhs];
            if (totalSum == target) {
                
                return {lhs + 1, rhs + 1};
            } 
            else if (totalSum < target) {
                lhs++;  // increase sum
            } 
            else {
                rhs--; // decrease sum
            }
        }
        return {};
    }
};