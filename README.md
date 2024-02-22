# Leetcode_Studynote


## Array

### 0. General note

+ Array[i] [j], i: rows, j: columns
+ Array[i] [j] [k]: first select the $i^{th}$ term in Array, then apply [j], finally apply [k]
+ Use index as pointer
+ Predefine values as float('inf'), 
  + ex. result = [float('inf')] * len(nums) , this sets an empty array with length len(nums)


### 1. Binary Search [Q704](https://leetcode.com/problems/binary-search/description/) [Q35](https://leetcode.com/problems/search-insert-position/submissions/1180827359/)

+ Application: Search in ordered array
+ Advantage: Time complexity $O(n) \to O(log_{2}(n))$ 
+ Description: Repeatedly compare the target with the middle value of the ordered array

### 2. Fast Slow pointer [Q27](https://leetcode.com/problems/remove-element/) [Q26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) 

- Application: modify an array based on itself
- Advantage: Time complexity $O(n^2) \to O(n)$ ,finish 2 for loops with 1 for loop
- Description: Set two variables: Fast=0, Slow=0, then iterate Fast from 0 to the end

### 3. Forward Backward pointer [Q977](https://leetcode.com/problems/squares-of-a-sorted-array/description/) 

- Application: modify an array from two ends
- Description: Set two variables: Forward_pointer = 0, Backward_pointer = len(nums)

### 4. Sliding window [Q209](https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1182936526/) [Q904 (hash map)](https://leetcode.com/problems/fruit-into-baskets/) 

- Application: Find a minimum length subarray that satisfy certain property
- Advantage: Time complexity $O(n^2) \to O(n)$ 
- Description: Evaluate the region between Forward and Backward pointer
- Algorithm: 2 whiles

