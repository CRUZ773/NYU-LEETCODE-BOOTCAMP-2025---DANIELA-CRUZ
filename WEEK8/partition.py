# 416. Partition Equal Subset Sum
class Solution6:
    def canPartition(self, nums: List[int]) -> bool:
        """
        0/1 Knapsack problem - DP approach
        Time: O(n * sum/2)
        Space: O(sum/2)
        """
        total = sum(nums)
        
        # If total is odd, can't partition into equal sums
        if total % 2 == 1:
            return False
        
        target = total // 2
        
        # dp[i] = True if we can make sum i
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            # Traverse backwards to avoid using same element twice
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]