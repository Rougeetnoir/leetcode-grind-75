class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n - 2):
            a = nums[i]

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if a > 0:
                break

            left, right = i + 1, n - 1
            target = -a
            
            while left < right:
                s = nums[left] + nums[right]
                
                if s < target:
                    left += 1
                
                elif s > target:
                    right -= 1
                
                else:
                    res.append([a,nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return res
