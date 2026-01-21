class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] = seen[num] + 1
                if seen[num] > len(nums) / 2:
                    return num
            else:
                seen[num] = 1