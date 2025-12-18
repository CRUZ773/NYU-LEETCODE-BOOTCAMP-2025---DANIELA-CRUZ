# 322. Coin Change
class Solution5:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Dynamic Programming - Bottom up
        dp[i] = minimum coins needed to make amount i
        Time: O(amount * len(coins))
        Space: O(amount)
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1

