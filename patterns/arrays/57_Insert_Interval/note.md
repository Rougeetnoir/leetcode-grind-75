下面只讲这题常用到的 **Python 语法/写法**（不直接给完整解答代码）。你可以把它当成“做题时要用的语法清单”。

---

## 1) 列表与区间的解包、读写

### 取出区间的 start / end

```python
for s, e in intervals:
    ...
```

或单个区间：

```python
s, e = newInterval
```

### 构造结果列表

```python
res = []
res.append([s, e])      # 追加一个区间
```

### 访问最后一个区间并修改它（用于合并）

```python
last_s, last_e = res[-1]
res[-1][1] = new_end    # 只改 end
```

---

## 2) 比较条件（判断是否重叠/是否在左侧/右侧）

这题核心判断只需要会写条件表达式：

### 完全在左侧（不重叠）

> 当前区间的 end < 新区间的 start

```python
if e < start:
    ...
```

### 完全在右侧（不重叠）

> 当前区间的 start > 新区间的 end

```python
elif s > end:
    ...
```

### 重叠（需要合并）

> 否则就是有交集

```python
else:
    start = min(start, s)
    end = max(end, e)
```

这里会用到 `min` / `max`。

---

## 3) 一次扫描时的“状态更新”写法

插入/合并时常见的写法是把 `newInterval` 的 `(start, end)` 当作可变的“当前合并区间”，不断被扩张：

```python
start, end = newInterval

# 遇到重叠时更新 start/end
start = min(start, s)
end   = max(end, e)
```

---

## 4) 提前插入与剩余追加（break / extend）

当你确定后面都在右侧时，可以：

### break 退出循环

```python
break
```

### 把剩余区间一次性接到结果后面

```python
res.extend(intervals[i:])   # 追加切片
```

需要会用切片：

```python
intervals[i:]   # 从 i 到末尾
```

---

## 5) 可选：用二分找插入位置（不必要，但提示提到了）

如果你想练二分，会用到 `bisect` 模块（按 start 找位置）：

```python
from bisect import bisect_left

starts = [s for s, e in intervals]
pos = bisect_left(starts, start)   # start 是 newInterval 的 start
```

注意：这题即使用二分，后面仍然要处理“与相邻区间合并”的逻辑，所以语法重点是 `bisect_left` + 列表推导式。

---

## 6) 题目常见坑对应的语法点

* `intervals` 可能为空：直接构造并返回列表（会用到 `if not intervals:`）

```python
if not intervals:
    return [newInterval]
```

* 结果里最后一定要把合并后的新区间放进去（会用 `append`）

* 返回二维列表（list of lists）

---

如果你愿意，我可以只给你一个“代码骨架”（只包含函数签名和注释占位，不给具体逻辑实现），让你把上面的语法填进去。
