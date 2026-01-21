class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        #两个指针，一个k一个i
        k = 1 #第一个数肯定是unique的
        
        for i in range(1,len(nums)): #从第二个数开始遍历
            if nums[i] != nums[k-1]:  #把k当做处理后的正确list, 如果现在遍历到的值nums[i]和之前我们处理好的list的前一个值nums[k-1]是一样的，那么跳过这个i,也不处理k，直接遍历下一个，
                nums[k] = nums[i]
                k += 1
                
        return k