class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n # 创建一个长度为 n 的列表，所有元素都初始化为 1

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1): #从数组最后一个位置开始，一直遍历到第一个位置，实现“逆序遍历”
            answer[i] *= suffix
            suffix *= nums[i]

        return answer