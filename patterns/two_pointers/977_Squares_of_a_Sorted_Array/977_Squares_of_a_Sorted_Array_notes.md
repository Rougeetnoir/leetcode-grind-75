好，我们**把 977 这道题完整收个尾**。下面是一个**可直接背、可直接复述、可直接写代码的总结版**。

---

## 977. Squares of a Sorted Array —— 解题思路 & 要点总结

---

## 一、题目本质（先定性）

* 输入数组 `nums` **已按非递减排序**
* 但 **平方会破坏顺序**
* 目标：在 **O(n)** 时间内得到平方后的有序数组

👉 关键：**不能直接平方再排序**

---

## 二、核心洞察（这题的“破题点”）

> 在一个已排序数组中，
> **平方后的最大值一定来自最左端或最右端**

原因：

* 左端：绝对值最大的负数
* 右端：最大的正数

---

## 三、为什么用 Two Pointers？

因为每一步只需要比较：

```text
abs(nums[l]) vs abs(nums[r])
```

就能确定：

* 当前区间内的 **最大平方值**

---

## 四、整体解题思路（标准流程）

1. **准备结果数组**

   ```python
   res = [0] * n
   ```
2. **设置三个指针**

   * `l`：左读指针（从 0 开始）
   * `r`：右读指针（从 n-1 开始）
   * `pos`：写指针（从 n-1 开始）
3. **循环比较左右两端平方**

   * 大的平方 → 放到 `res[pos]`
   * 移动对应读指针
   * `pos -= 1`
4. **直到所有位置填满**

---

## 五、指针角色分工（一定要清楚）

| 指针    | 作用   | 说明            |
| ----- | ---- | ------------- |
| `l`   | 左读指针 | 只读 `nums[l]`  |
| `r`   | 右读指针 | 只读 `nums[r]`  |
| `pos` | 写指针  | 只写 `res[pos]` |

📌 **读和写必须分离**，不能 in-place 覆盖

---

## 六、`pos` 的关键作用（本题灵魂）

* 结果数组是 **从小到大**
* 我们每一步拿到的是 **当前最大平方**
* 所以必须：

  ```python
  从 res 的末尾往前写
  ```

👉 `pos` 用来精确控制“写入位置”

---

## 七、边界与细节（常见坑）

1. 循环条件必须是：

   ```python
   while l <= r
   ```

   防止遗漏中间元素

2. **不能直接修改 `nums`**

   * 会破坏后续比较逻辑

3. `res = [0] * n` 是安全的（int 不可变）

---

## 八、复杂度（官方最优解）

* **时间复杂度：** `O(n)`
* **空间复杂度：** `O(n)`

---

## 九、官方最优解代码（最终版）

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        l, r = 0, n - 1
        pos = n - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[pos] = nums[l] * nums[l]
                l += 1
            else:
                res[pos] = nums[r] * nums[r]
                r -= 1
            pos -= 1

        return res
```

---

## 十、面试一句话总结（非常重要）

> This problem can be solved in O(n) time using two pointers by comparing the absolute values at both ends and filling the result array from right to left.

---

### ✅ 到这一步，你对这题已经是 **“完全掌握 + 可迁移”** 状态了

如果你下一步想：

* 立刻用同一模板刷 `Merge Sorted Array`
* 或让我出一题你来独立设计 `pos`
* 或总结一个 **Two Pointers 速判清单**

直接说一声，我们继续。
