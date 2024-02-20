# Leetcode_Studynote


## Array

### 0. General note

+ Array[i] [j], i: rows, j: columns
+ Array[i] [j] [k]: first select the $i^{th}$ term in Array, then apply [j], finally apply [k]
+ Use index as pointer

### 1. Binary Search [Q704](https://leetcode.com/problems/binary-search/description/) [Q35](https://leetcode.com/problems/search-insert-position/submissions/1180827359/)

+ Application: Search in ordered array
+ Advantage: Time complexity $O(n) \to O(log_{2}(n))$ 
+ Description: Repeatedly compare the target with the middle value of the ordered array

### 2. Fast Slow pointer [Q27](https://leetcode.com/problems/remove-element/) [Q26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) 

- Application: modify an array based on itself
- Advantage: Time complexity $O(n^2) \to O(n)$ ,finish 2 for loops with 1 for loop
- Description: Set two variables: Fast=0, Slow=0, then iterate Fast from 0 to the end
