"""
LeetCode <1> - <Two Sum>
Pattern: Array, Hash table
Difficulty: Easy

Time:O(n)
Space:O(n)

Notes:
Key idea: complement lookup
Pitfalls: duplicate values / same index
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        #solution 3 : One-pass HashMap, Time Complexity: O(n), Space Complexity:O(n)
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        
