# Leetcode_Studynote


## Array

### 0. General note

+ Array[i][j], i: rows, j: columns
+ Array[i][j][k]: first select the $i^{th}$ term in Array, then apply [j], finally apply [k]

### 1. Binary Search [Q704](https://leetcode.com/problems/binary-search/description/) [Q35](https://leetcode.com/problems/search-insert-position/submissions/1180827359/)

+ Only applicable for ordered array
+ Use index as search result
+ Use right - left >= 0 as condition
	- target in [left, mid) : right = mid -1
	- target in (mid, right]: left = mid + 1
	- target is mid
