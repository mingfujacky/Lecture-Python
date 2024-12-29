---
marp: true
theme: default
paginate: true
---
# Zero-based indexing
- index 從 0 開始，array位置的計算公式: Address = start address + box size * (Index)
- 如果 index 從 1 開始，array位置的計算公式需改成：Address = start address + box size * (Index -1 ), 多了一個減法的運算
![bg right:50% w:500 Zero-based indexing](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*sBfeTTqmIGgrbViLJNCr1A.png)