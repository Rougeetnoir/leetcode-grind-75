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
        #solution 2: Two-pass HashMap Time Complexity: O(n), Space Complexity:O(n)
        # First pass: build the hash map
        num_to_index = {}
        for i, num in enumerate(nums):
            num_to_index[num] = i
            
        # Second pass: search for complements 
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index and num_to_index[complement] != i:
                return [i, num_to_index[complement]]


