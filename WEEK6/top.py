# 347. Top K Frequent Elements
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Bucket Sort approach - O(n) time complexity
        Time: O(n)
        Space: O(n)
        """
        # Count frequencies
        count = Counter(nums)
        
        # Create buckets where index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        
        # Collect top k frequent elements
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result
    
    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        """
        Alternative: Min-heap approach
        Time: O(n log k)
        Space: O(n)
        """
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

