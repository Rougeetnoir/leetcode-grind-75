````md
# LeetCode 121 — Best Time to Buy and Sell Stock

## Pattern
- Array / One-pass scan
- Keep **min so far** + **best profit so far**
- (Kadane-like idea: best difference with constraint buy before sell)

---

## Problem
Given `prices[i]` = price on day `i`, choose **one** day to buy and a **later** day to sell.  
Return the **maximum profit**. If no profit possible, return `0`.

---

## Key Insight
If we sell on day `j`, the best buy day must be the **lowest price before j**.

So while scanning:
- Track `min_price` = lowest price seen so far
- Track `max_profit` = best `(current_price - min_price)` seen so far

---

## Brute Force (Baseline)
Try all pairs `(i, j)` with `i < j`.

**Time:** `O(n^2)`  
**Space:** `O(1)`

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)

        for i in range(n):
            for j in range(i + 1, n):
                max_profit = max(max_profit, prices[j] - prices[i])

        return max_profit
````

**Pitfall**

* Don’t name a variable `max` (it shadows Python built-in `max()`).

---

## Why slicing + max() is NOT good

Code like:

```python
max_profit = 0
for i in range(len(prices) - 1):
    profit = max(prices[i+1:]) - prices[i]
    max_profit = max(max_profit, profit)
```

Looks short, but:

* `prices[i+1:]` creates a **new list** each time → extra work and memory
* `max(...)` scans the slice → another `O(n)`
* Done inside a loop → overall still **O(n^2)** time
* Slice creation adds **O(n)** extra space per iteration (peak `O(n)`)

**Time:** `O(n^2)`
**Space:** peak `O(n)` due to slicing

---

## Optimal Solution (One-pass)

### Idea

Scan once:

* Update `min_price`
* Compute profit if sell today: `p - min_price`
* Update `max_profit`

**Time:** `O(n)`
**Space:** `O(1)`

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for p in prices:
            if p < min_price:
                min_price = p
            else:
                max_profit = max(max_profit, p - min_price)

        return max_profit
```

---

## Walkthrough Example

`prices = [7, 1, 5, 3, 6, 4]`

* Start: `min_price = inf`, `max_profit = 0`
* p=7  → min=7
* p=1  → min=1
* p=5  → profit=4 → max_profit=4
* p=3  → profit=2 → max_profit=4
* p=6  → profit=5 → max_profit=5
* p=4  → profit=3 → max_profit=5

Answer = `5` (buy at 1, sell at 6)

---

## Edge Cases

* Strictly decreasing: `[7,6,4,3,1]` → return `0`
* Single day: `[5]` → return `0`
* Equal prices: `[2,2,2]` → return `0`

---

## Complexity Summary

| Approach                  |     Time |       Space | Notes             |
| ------------------------- | -------: | ----------: | ----------------- |
| Brute Force (double loop) | `O(n^2)` |      `O(1)` | simplest baseline |
| Slicing + max()           | `O(n^2)` | peak `O(n)` | slice copies cost |
| One-pass min tracking     |   `O(n)` |      `O(1)` | best solution     |

---

## Common Pitfalls

* Shadowing built-ins: `max = 0` (avoid!)
* Forgetting the constraint **buy before sell**
* Miscounting complexity when using slicing (`prices[i+1:]`)

```

如果你想把它放进你之前的 `pattern/array+greedy`（或 `array`）目录结构里，我也可以按你现在的文件夹习惯再给你一个“题目 README + solution1/solution2 命名建议”。
```
