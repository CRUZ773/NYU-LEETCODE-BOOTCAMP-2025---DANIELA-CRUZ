# 53. Maximum Subarray (Kadane's Algorithm)
class Solution4:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane's Algorithm
        Time: O(n)
        Space: O(1)
        """
        max_sum = current_sum = nums[0]
        
        for num in nums[1:]:
            # Either extend current subarray or start new one
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum
    
    def maxSubArray_divide_conquer(self, nums: List[int]) -> int:
        """
        Divide and Conquer approach
        Time: O(n log n)
        Space: O(log n)
        """
        def helper(left, right):
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            
            # Max in left half
            left_max = helper(left, mid)
            # Max in right half
            right_max = helper(mid + 1, right)
            
            # Max crossing middle
            left_sum = float('-inf')
            curr_sum = 0
            for i in range(mid, left - 1, -1):
                curr_sum += nums[i]
                left_sum = max(left_sum, curr_sum)
            
            right_sum = float('-inf')
            curr_sum = 0
            for i in range(mid + 1, right + 1):
                curr_sum += nums[i]
                right_sum = max(right_sum, curr_sum)
            
            cross_sum = left_sum + right_sum
            
            return max(left_max, right_max, cross_sum)
        
        return helper(0, len(nums) - 1)
