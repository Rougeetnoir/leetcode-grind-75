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
        #solution 1 : brute force way, Time Complexity: O(n²) Space Complexity: O(1)
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


            


