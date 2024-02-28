# Leetcode_Studynote


## Array

### 0. General note

+ (1) Array[i] [j], i: row, j: column

  + Array[i] [j] [k]: first select the $i^{th}$ term in Array, then apply [j], finally apply [k]

+ (2) Index start from 0

+ (3) Cannot delete value from an array, but can overwrite

  + Technique: Predefine array as `float('inf')`, then overwrite them

    ```python
    result = [float('inf')] * len(nums) 
    ```

     The above sets an empty array with length `len(nums)` 



### 1. Binary Search [Q704](https://leetcode.com/problems/binary-search/description/) [Q35](https://leetcode.com/problems/search-insert-position/submissions/1180827359/)

+ Application: Search in ordered array
+ Advantage: Time complexity $O(n) \to O(log_{2}(n))$ 
+ Description: Repeatedly compare the target with the middle value of the ordered array
+ Technique: **循环不变量**, for each loop, some rules should be strictly followed. 
  + Ex. in each while loop we should strictly identify whether target lies within [left,mid) or [left,mid] 


### 2. Fast Slow pointer [Q27](https://leetcode.com/problems/remove-element/) [Q26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) 

- Application: modify an array based on rules on itself

- Advantage: Time complexity $O(n^2) \to O(n)$ ,finish 2 for loops with 1 for loop

- Pseudocode: Set two pointers

  ```python
  Fast_pointer,Slow_pointer = 0,0
  while Fast_pointer < len(array): #iterate Fast_pointer from 0 to end
  ```

### 3. Forward Backward pointer [Q977](https://leetcode.com/problems/squares-of-a-sorted-array/description/) 

- Application: modify an array from two ends

- Pseudocode: Set two variables: Forward_pointer = 0, Backward_pointer = len(nums)

  ```python
  Fast_pointer,Slow_pointer = 0,len(array) - 1
  while Fast_pointer < len(array): #iterate pointers from two ends
  ```

### 4. Sliding window [Q209](https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1182936526/) [Q904 (hash map)](https://leetcode.com/problems/fruit-into-baskets/) 

- Application: Find a minimum length subarray that satisfy certain property

- Advantage: Time complexity $O(n^2) \to O(n)$ 

- Pseudocode: Evaluate the region between **Fast** and **Slow** pointers

  ```python
  Fast_pointer,Slow_pointer = 0,0
  while/if (rule1):
    Fast_pointer += 1
    while/if (rule2):
      Slow_pointer += 1
  ```

### 5.Spiral Matrix [Q59](https://leetcode.com/problems/spiral-matrix-ii/description/) [Q54](https://leetcode.com/problems/spiral-matrix/) 

- Application: Create Spiral matrix
- Technique 1: **循环不变量**, for each loop, some rules should be strictly followed. 
  + Ex. in each loop we iterate clockwise, 左闭右开，上闭下开，右闭左开，下闭上开
- Technique 2: `for i in range(10,0,-1):`  This will offer i from 10 to 1(右闭左开)

## Linked List

### 0. General note

```python
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
```

- `_init_` defines the initial state, meaning that the initial `ListNode.val= 0`, and `ListNode.next = None` 

```python
#Example List Node: 
ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 6, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: ListNode{val: 6, next: None}}}}}}} 
```

<img width="517" alt="Screenshot 2024-02-26 at 10 16 47 PM" src="https://github.com/BL-Starlord/Leetcode_Studynote/assets/81414955/95e6ea02-85cf-4c3d-8e1f-d371795439d3">


### 1. Removing Elements [Q203](https://leetcode.com/problems/remove-linked-list-elements/) 

- Technique： Dummy_head

### 2. 
