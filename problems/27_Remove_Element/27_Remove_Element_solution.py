class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

#第一次的思路：
# 思路：和26题一样
# in place的list，两种编号方法，方法i和方法k，i表示原来的list的index，k表示我们in place处理之后的list的index

# 26题Remove Duplicates from Sorted Array，第一个数肯定是unique的，所以k和i都从1开始遍历。

# 这一题因为要从第一个值开始判断是不是val, 所以k和i都从0开始遍历。

# 我之前比较困惑的是：
# 我知道`nums[i] != val`的情况下是需要把方法i下的`nums[i]`，在方法k下找到它应该在的index.
# 我之前想错的一点是，如果`nums[i] = val`，我总想给它剔除原来的list，但其实我只需要跳过它，不处理它，也不更新k，等于新的编号方法里不考虑它就好了！