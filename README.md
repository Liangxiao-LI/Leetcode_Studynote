# Leetcode_Studynote


## Array

### 1. Binary Search [Q704](https://leetcode.com/problems/binary-search/description/)

+ Only applicable for ordered array
+ Use index as search result
+ Use right - left >= 0 as condition
	- target in [left, mid) : right = mid -1
	- target in (mid, right]: left = mid + 1
	- target is mid