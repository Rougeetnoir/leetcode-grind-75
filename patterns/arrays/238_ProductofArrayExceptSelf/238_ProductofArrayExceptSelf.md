Given an integer array `nums`, return *an array* `answer` *such that* `answer[i]` *is equal to the `product` of all the elements of* `nums` *except* `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and ***without using the division operation***.

**Example 1:**

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

**Example 2:**

```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

**Constraints:**

- `2 <= nums.length <= 10^5`
- `30 <= nums[i] <= 30`
- The input is generated such that `answer[i]` is **guaranteed** to fit in a **32-bit** integer.

**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)

Hint 1

Think how you can efficiently utilize `prefix` and `suffix`后缀 products to calculate the product of all elements except self for each index. Can you pre-compute the prefix and suffix products in linear time to avoid redundant calculations?

Hint 2

Can you minimize additional space usage by reusing memory or modifying the input array to store intermediate results?

# 思路 Problem Core Idea

这题在考察：如何在**不允许除法**的情况下，把“除了自己以外的所有元素乘积”拆成两个独立部分——`左侧所有数的乘积` × `右侧所有数的乘积`，并用一次线性扫描把它们高效组合起来。

Optimal Solution

核心做法是 **prefix + suffix**（前缀积与后缀积）。

1. 对每个位置 `i`：
- `prefix[i] = nums[0] * ... * nums[i-1]`（不含自己）
- `suffix[i] = nums[i+1] * ... * nums[n-1]`（不含自己）
    
    那么答案就是：`answer[i] = prefix[i] * suffix[i]`
    
1. 进一步把空间优化到 O(1)（不算输出数组）：
- 先用输出数组 `answer` 存 `prefix`
- 再从右往左用一个变量 `suffix_prod` 滚动维护后缀积，把 `answer[i] *= suffix_prod`

Python implementation

```python
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n //创建一个长度为 n 的列表，所有元素都初始化为 1。

        # answer[i] 先存 prefix：nums[0..i-1] 的乘积
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # 再乘上 suffix：nums[i+1..n-1] 的乘积
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
```

Time complexity `O(n)`：两次线性遍历。

Space complexity`O(1)` 额外空间：只用了常数变量 `prefix/suffix`；输出数组不计入额外空间。

## Key Reasoning Steps

- 定义不变量（非常关键）
    - 第一趟从左到右：循环到 `i` 时，`prefix` 始终等于 `nums[0..i-1]` 的乘积；把它写进 `answer[i]`，就实现了“左边所有数的乘积”。
    - 第二趟从右到左：循环到 `i` 时，`suffix` 始终等于 `nums[i+1..n-1]` 的乘积；把它乘到 `answer[i]` 上，就补齐“右边所有数的乘积”。
- 为什么不需要除法
    - 因为我们根本不去计算总乘积再除掉 `nums[i]`，而是把目标直接拆成互不重叠的两段乘积相乘。
- 为什么对 0 也天然正确
    - 如果数组里有 0，prefix/suffix 的乘积会自动把影响反映出来：
        - 若 `i` 位置不是 0，则 left 或 right 中必然包含 0，结果为 0。
        - 若 `i` 位置是 0，则结果等于“除该 0 外其它元素的乘积”（因为 left/right 不包含它）。
            
            不需要额外特判。
            

## Thinking Transition (Very Important)

常见直觉（但不满足要求）：

- 先算 `total_product = 所有元素乘积`，然后 `answer[i] = total_product / nums[i]`。
- 问题在于：题目禁止除法；且遇到 0 时除法思路会崩溃（除以 0 或需要分情况统计 0 个数）。

### 关键思维转变：

- “从算一个整体再去掉自己” 转变为 “直接把答案拆成两部分：左边乘积 × 右边乘积”。
- 到这一步，思路从“全局依赖一个 total”变成“每个位置依赖两个可线性维护的局部累积量（prefix/suffix）”。
- 再进一步：从“需要两个数组存 prefix/suffix”变成“prefix 存进输出数组，suffix 用一个滚动变量补上”，实现 O(1) 额外空间。

Lessons for Future Problems

- 当题目禁止除法或存在 0 时，优先考虑“拆分贡献”而不是“整体再移除”。
- “除了自己以外的聚合值”类问题，经常可以写成：`left_contrib[i] * right_contrib[i]`。
- 前缀/后缀是典型线性技巧：
    - 第一趟写入左贡献
    - 第二趟用滚动变量叠加右贡献
- 输出数组常常可以复用为 DP/前缀缓存，从而把额外空间降到 O(1)。