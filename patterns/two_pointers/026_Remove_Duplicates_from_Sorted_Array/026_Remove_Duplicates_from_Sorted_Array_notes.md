思路：有问题版本

```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        for i in range(len(nums)):
            #第一个数，可以保留
            if i == 0:
                #doing nothing
                val = nums[i]
                k += 1
            #从第二个数开始判断和前一个数是否一样
            elif nums[i] == val:
                #去掉这一个数，k不变，继续loop
                del nums[i]
            else:
                #新的不重复的数字出现了
                val = nums[i]
                k += 1
        return k
```

你这个思路**方向是对的**（想用“当前值 vs 上一个保留值”来判断），但这个实现**确实有几个关键问题**，而且正好是 LeetCode 很爱考的坑。我们一步一步拆解 👇

---

## 一、你这版代码“哪里有问题”

### ❌ 1. **在 for 循环里 `del nums[i]` 是致命错误**

```python
for i in range(len(nums)):
    ...
    del nums[i]

```

问题有两个：

### （1）删除元素会导致 **索引错乱**

- `del nums[i]` 后，后面的元素会整体左移
- 但 `for i in range(len(nums))` 的 `i` 仍然按原来的索引递增
- 结果：**会跳过元素**

👉 举个例子：

```python
nums = [1,1,1,2]
i = 1 -> del nums[1] -> nums = [1,1,2]
i = 2 -> nums[2] = 2
# 中间那个 1 被跳过了

```

---

### （2）时间复杂度退化到 O(n²)

- `del nums[i]` 是 **O(n)** 操作（后面的元素要移动）
- 最坏情况下每个元素都删一次 → **O(n²)**

而题目要求的是 **O(n)**。

---

### ❌ 2. `k` 的含义和数组真实状态不同步

你希望：

- `k` = 不重复元素个数
- 前 `k` 个元素是结果

但你一边 `del`，一边 `k += 1`，

**数组长度、索引、k 三者已经失去一致性**，逻辑会非常难以维护。

---

## 二、正确的思维方式（Two Pointers）

> 核心思想一句话：
> 
> 
> **不要删除元素，只“覆盖”元素**
> 

---

### 🧠 为什么能这样做？

因为：

- 数组是 **有序的**
- 重复元素一定是 **连续的**
- 我们只关心前 `k` 个位置对不对

---

## 三、标准 Two Pointers 解法（推荐）

### 思路拆解

- 用一个指针 `k`：
    - 指向 **下一个应该写入新值的位置**
- 从第 1 个元素开始遍历
- 只要发现 `nums[i] != nums[k-1]`
    - 就把它写到 `nums[k]`
    - `k += 1`

---

### ✅ 正确代码（Python）

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1  # 第一个元素一定是唯一的

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k

```

---

## 四、用你的 Example 手动走一遍

### 示例 2

```python
nums = [0,0,1,1,1,2,2,3,3,4]

```

| i | nums[i] | nums[k-1] | 操作 | nums（前部） | k |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 0 | skip | [0] | 1 |
| 2 | 1 | 0 | write | [0,1] | 2 |
| 3 | 1 | 1 | skip | [0,1] | 2 |
| 4 | 1 | 1 | skip | [0,1] | 2 |
| 5 | 2 | 1 | write | [0,1,2] | 3 |
| 6 | 2 | 2 | skip | [0,1,2] | 3 |
| 7 | 3 | 2 | write | [0,1,2,3] | 4 |
| 8 | 3 | 3 | skip | [0,1,2,3] | 4 |
| 9 | 4 | 3 | write | [0,1,2,3,4] | 5 |

✅ 前 `k=5` 个元素正是答案

---

## 五、和你原始思路的“一一对应关系”

| 你的想法 | 正确做法 |
| --- | --- |
| 用 `val` 记住上一个值 | 用 `nums[k-1]` |
| 遇到重复就删除 | 遇到重复就跳过 |
| 维护 `k` | `k` 只在写入时 +1 |
| 修改数组长度 | 不修改长度，只覆盖 |

---

## 六、一句话总结（面试版）

> 这是一个典型的 Two Pointers + In-place 覆盖问题
> 
> 
> **不要在遍历时删除元素，只移动“写指针”**
> 

如果你愿意，下一步我可以：

- 把这题写成你 **pattern/Two Pointers 的 notes.md**
- 或对比讲解 **Remove Duplicates II（最多保留 2 个）**
- 或帮你总结一个 **“什么时候不能 del”的 Python 心法表**

你来选 👍

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #两个指针，一个k一个i
        k = 1 #第一个数肯定是unique的
        
        for i in range(1,len(nums)): #从第二个数开始遍历
            if nums[i] != nums[k-1]:  #把k当做处理后的正确list, 如果现在遍历到的值nums[i]和之前我们处理好的list的前一个值nums[k-1]是一样的，那么跳过这个i,也不处理k，直接遍历下一个，
                nums[k] = nums[i]
                k += 1
                
        return k
```

**算法思想**：Two Pointers（快慢指针）✔

**是否 in-place**：是（只覆盖，不扩容、不删除）✔

**时间复杂度**：O(n)✔

**空间复杂度**：O(1)✔

**逻辑清晰度**：高