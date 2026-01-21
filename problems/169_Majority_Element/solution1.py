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

#时间 O(n)，但空间是 O(n)
# HashMap 计数（你现在的思路，O(n) space）

# 你现在代码有两个小点可以改得更“面试友好”：

# len(nums) / 2 会变成 float（虽然不影响比较，但习惯上用整数阈值）

# 即使不提前 return，最后也能找出最大频次（但题目保证一定存在 majority，所以提前 return 也 ok）

# 更简洁版本：
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        seen = {}
        threshold = len(nums) // 2
        
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            if seen[num] > threshold:
                return num