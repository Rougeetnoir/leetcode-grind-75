# Pattern: Array + HashMap (Complement Lookup)

> 典型目标：在数组里快速判断/定位“是否存在某个值（或搭配值）”，用 HashMap 把查找从 O(n) 变成 O(1)。

---

## When to use (识别信号)

- 题目里出现：**pair / two numbers / sum / difference / complement**
- 需要：**快速判断某个值是否出现过**，或者 **值 -> 位置/次数** 的映射
- 暴力会是：两层循环 `O(n^2)`，而优化方向通常是：用 HashMap 记住“见过的东西”

---

## Core idea (一句话)

对每个数 `x`，我们想找的另一个数是 `y = target - x`。  
把「查 y 是否存在」变快：用 HashMap 存储 **value -> index**（或 value -> count）。

---

## Canonical example: Two Sum

### Problem
给定 `nums` 和 `target`，返回两个下标 `(i, j)` 使得：
`nums[i] + nums[j] == target`，且 `i != j`。

---

## Solutions

### Plan A — Brute Force
**Idea**
- 枚举所有 pair `(i, j)`，判断是否满足

**Time / Space**
- Time: `O(n^2)`
- Space: `O(1)`

**Why it’s slow**
- 每个元素都要跟后面所有元素配对检查

---

### Plan B — Two-pass HashMap (Store then search)
**Idea**
1. 第一遍：把每个数存到 `map[num] = index`
2. 第二遍：对每个 `num`，查 `need = target - num` 是否在 map 中
3. 注意：需要保证 `map[need] != i`

**Time / Space**
- Time: `O(n)`
- Space: `O(n)`

**Pros**
- 思路直观：先建索引，再查 complement

**Cons**
- 多一遍遍历

---

### Plan C — One-pass HashMap (Search while building)
**Idea**
- 从左到右遍历，每次先查 complement：
  - `need = target - num`
  - 如果 `need` 在 map：直接返回
  - 否则：记录当前数 `map[num] = i`

**Time / Space**
- Time: `O(n)`
- Space: `O(n)`

**Why it avoids reusing the same index**
- 因为查找发生在插入之前：只会匹配到“之前出现过”的元素

---

## Implementation template (Python pseudo)

```python
seen = {}  # value -> index

for i, num in enumerate(nums):
    need = target - num
    if need in seen:
        return [seen[need], i]
    seen[num] = i
