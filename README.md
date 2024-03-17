# Leetcode_Studynote

This is my Studynote for Leetcode 😆 

Already attempted topics and questions are listed in the table below.

My Python 3 Solutions are attached in the repo.

| Topic                                      | Question                                                     |
| ------------------------------------------ | ------------------------------------------------------------ |
| Topic 1: Array                             |                                                              |
| 1) Binary Search                           | [Q704](https://leetcode.com/problems/binary-search/description/) [Q35](https://leetcode.com/problems/search-insert-position/submissions/1180827359/) |
| 2) Fast Slow pointer                       | [Q27](https://leetcode.com/problems/remove-element/) [Q26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) |
| 3) Forward Backward pointer                | [Q977](https://leetcode.com/problems/squares-of-a-sorted-array/description/) |
| 4) Sliding window                          | [Q209](https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1182936526/) [Q904 (hash map)](https://leetcode.com/problems/fruit-into-baskets/) |
| 5) Spiral Matrix                           | [Q59](https://leetcode.com/problems/spiral-matrix-ii/description/) [Q54](https://leetcode.com/problems/spiral-matrix/) |
| Topic 2: Linked List                       |                                                              |
| 1) Removing Elements                       | [Q203](https://leetcode.com/problems/remove-linked-list-elements/) |
| 2) Design Linked List                      | [Q707](https://leetcode.com/problems/design-linked-list/description/) |
| 3) Reverse Linked List                     | [Q206](https://leetcode.com/problems/reverse-linked-list/)   |
| 4) Swap Nodes Linked List                  | [Q24](https://leetcode.com/problems/swap-nodes-in-pairs/submissions/1193000641/) |
| 5) Remove Nth Node From End of Linked List | [Q19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1193499537/) |
| 6) Intersection of two Linked List         | [Q160](https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/1193510593/) |
| 7) Linked List Cycle                       | [Q142](https://leetcode.com/problems/linked-list-cycle-ii/submissions/1193518167/) (Hard) |
| Topic 3: Hashmap                           |                                                              |
| 1) Valid Anagram                           | [Q242](https://leetcode.com/problems/valid-anagram/) [Q383](https://leetcode.com/problems/ransom-note/) |






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

## Linked List （OOP）

### 0. General note

In programming, Class and Object are fundamental concepts in Object-Oriented Programming (OOP), but they represent two different entities:

**Class**: A class is a template used to create objects. It defines the structure of objects (through fields or attributes) and their behavior (through methods). The class itself is not an object but a template for creating objects.  `ListNode` is a class.

**Object**: An object is an instance created based on the definition of a class. Each object has its own attribute values, which are set according to the class definition. Each time we call `ListNode()` is creating a new `ListNode` object.

#### Code Explanation

```python
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
```

- `_init_`: initial state. By setting   `dummy_head = ListNode()`, we create an object called `dummy_head`, where     `dummy_head.val= 0` and `dummy_head.next = None` 

```python
#Example ListNode: 
ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 6, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: ListNode{val: 6, next: None}}}}}}} 
```

<img width="517" alt="Screenshot 2024-02-26 at 10 16 47 PM" src="https://github.com/BL-Starlord/Leetcode_Studynote/assets/81414955/95e6ea02-85cf-4c3d-8e1f-d371795439d3">

```python
#Example 1: Variables are references to object values but not containers of the data.
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy_head = ListNode(next = head)
				current = dummy_head
        
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy_head.next
```

- Variables are references to object values but not containers of the data.
  - Here current and dummy_head are two variables that refers to the same object `ListNode()`
  - dummy_head keeps pointing at the very first element of `ListNode()`
  - current is a pointer that moves and modify the object `ListNode()`  

```python
#Example 2
class ListNode: 
        def __init__(self, val=0,next = None):
                self.val = val
                self.next = next

head = ListNode(1,ListNode(2,ListNode(3)))
cur = head
pre = None
temp = cur.next
cur.next = pre
pre = cur
cur = temp #! This step won't affect pre
```

- Can create multiple variables to reference object, but one variable is independent of another variable
  - Here pre and cur are two variables that both refers to head


### 1. Removing Elements [Q203](https://leetcode.com/problems/remove-linked-list-elements/) 

- Technique： Dummy_head
- Pseudocode: Create a first empty element

```python
dummy_head = ListNode(next = head)
```

### 2. Design Linked List [Q707](https://leetcode.com/problems/design-linked-list/description/) 

- No Technique, great example

### 3. Reverse Linked List [Q206](https://leetcode.com/problems/reverse-linked-list/) 

- No Technique, great example

### 4. Swap Nodes Linked List [Q24](https://leetcode.com/problems/swap-nodes-in-pairs/submissions/1193000641/) 

- No Technique, great example

### 5. Remove Nth Node From End of Linked List [Q19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1193499537/) 

- Technique:(1) Fast_slow Pointer (2)Dummy_head

### 6. Intersection of two Linked List [Q160](https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/1193510593/)

- Technique:
  - (1) Get Linked List length 
  - (2) `pointerA == pointerB` can be used to identify if two linked lists are exactly the same

### 7. Linked List Cycle [Q142](https://leetcode.com/problems/linked-list-cycle-ii/submissions/1193518167/) (Hard)

- Technique: 
  - Use Fast_slow Pointer to detect cycle, Fast_pointer will eventually meet slow Pointer
  - Use mathematical relationship to find the loop starting position(requires a simple proof euqating $2*slow = fast$)

## Hashmap

### 0. General Note

When we encounter the need to quickly determine whether an element appears in a collection, we should consider using hashing.

However, hashing trades space for time because we need to use an extra array, set, or map to store the data to achieve fast lookup.

If you come across a scenario in an interview where you need to determine if an element has appeared before, you should think of hashing first!

#### Useful library: 

```python
from collections import defaultdict

int_dict = defaultdict(int) # Create a dictionary which contains int
list_dict = defaultdict(list) # Create a dictionary which contains list

# Example 1:
s = 'mississippi'
for k in s:
  int_dict[k] += 1 

# sorted(int_dict.items()) -> [('i', 4), ('m', 1), ('p', 2), ('s', 4)]

# Example 2:
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
for k, v in s:
    list_dict[k].append(v)

#sorted(list_dict.items()) -> [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```

### 1. Valid Anagram [Q242](https://leetcode.com/problems/valid-anagram/) [Q383](https://leetcode.com/problems/ransom-note/) 

- No technique, great example

