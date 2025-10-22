---
marp: true
theme: default
class: 
size: 16:9
paginate: true
footer: 國立陽明交通大學 電子與光子學士學位學程
headingDivider: 1
style: |
  section::after {
    content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total);
  }
  
  .middle-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .middle-grid img {
    width: 75%;
  }
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }
  .grid img {
    width: 100%;
  }
  .red-text {
    color: red;
  }
  
  .blue-text {
    color: blue;  
  }

  .small-text {
    font-size: 0.80rem;
  }
---
# Zero-based indexing
- index 從 0 開始，array位置的計算公式: Address = start address + box size * (Index)
- 如果 index 從 1 開始，array位置的計算公式需改成：Address = start address + box size * (Index -1 ), 多了一個減法的運算
![bg right:50% w:500 Zero-based indexing](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*sBfeTTqmIGgrbViLJNCr1A.png)