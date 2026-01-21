class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # squared_list = [x*x for x in nums]
        # squared_list.sort()
        # return squared_list

        #左右两边有正有负 #大的那个放到结果数组的末尾
        #指针向中间移动 从后往前填结果数组
        n = len(nums)
        res = [0] * n #创建一个长度为 n 的列表，所有元素都是

        l, r = 0, n-1
        pos = n - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[pos] = nums[l] ** 2
                l += 1
            else:
                res[pos] = nums[r] ** 2
                r -= 1
            pos -= 1
        return res



# 时间复杂度：`O(n)`
# 空间复杂度：`O(n)`需要一个新的结果数组来存放平方后的有序结果
# LeetCode 官方解法**不要求也不追求 in-place**，因为读写同一数组会破坏比较条件。