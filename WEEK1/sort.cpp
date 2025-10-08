class Solution {
public:
    void sortColors(vector<int>& nums) {
       int low = 0;           // pointer red
        int mid = 0;           // pointer white
        int high = nums.size() - 1; // pointer for blue)


        while (mid <= high) {
            if (nums[mid] == 0) {
                swap(nums[low], nums[mid]);
                mid++;
                low++;
            }
            else if (nums[mid] == 1) {
                mid++;
            }
            else { // nums[mid] == 2
                swap(nums[mid], nums[high]);
                high--;
            }
        } 
    }
};