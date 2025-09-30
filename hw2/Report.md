# Problem 1

> What is the advantage of using a tail pointer in a linked list?

There are multiple advantages from using a tail pointer in a linked list:
 1. Faster appends: a tail pointer enables O(1) (constant time) insertion at the end of a linked list by providing direct access to the last node, eliminating the need to traverse the entire list.
 2. List reversal: a tail pointer allows for quick reversal or traversal from the end of the list to the beginning. 
 3. List utilities: a tail pointer can facilitate other operations, such as appending one list to another, by instantly providing access to the end of the first list.


# Problem 2

Consider the following function:
```
function doIt(node):
    if node is null:
        return 
    doIt(node.next)
    print node.value
```

> Implement node and this function. Create a linked list with 12,3,5,2

Please see problem2_solution.py for the implementation of the node class and doIt function.

> What would the `doIt` function produce with your list?

**Output:** The doIt function would produce the following output:
```
2
5
3
12
```

The doIt function uses recursion to traverse the entire linked list first, then prints each node's value as it returns from the recursive calls. Since the print statement comes after the recursive call, the values are printed in reverse order of how they appear in the list. The function first reaches the end of the list (node with value 2), then prints 2, returns to the previous call and prints 5, then 3, and finally 12.


# Problem 3

Consider the following function:
```
function doIt(n)
    if n == 0:
        return 1
    else if n == 1:
        return 1
    else if n == 2:
        return 2
    else
        return doIt(n-1) + doIt(n-2) – doIt(n-3) 
```

> Implement this function and output doIt(1), doIt(3), doIt(6)

**Output** The doIt function would produce the following output:
```
Output of doIt(1) function:
1
Output of doIt(3) function:
2
Output of doIt(6) function:
4
```


# Problem 4

> Write a function to find the sum of the three middle nodes in a doubly linked list of sorted integers. You may assume the the list has an odd length:
Ex.
2,4,8,10,15,29,41,

Please see problem4_solution.py for the implementation of the function requested above.


