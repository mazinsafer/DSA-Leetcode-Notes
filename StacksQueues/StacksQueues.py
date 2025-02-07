## when thinking about a stack, think about an array being built from left to right
    ## for example appending an array: [3,4, ...] where 3 is on the bottom and 4 is on top
    ## popping is going to remove the last element of the array (whats on top of the stack)
    ## peek is asking whats on top of the stack
    ## IsEmpty

## when thinking about a queue think about a line for a movie, where the first person in line is the first to leave the line
    ## Enqueue is just append
    ## Dequeue is popping from the left (takes off first thing in the queue)
    ## Dequeue is only O(1) in a doubly linked list
    ## Ok to use dynamic arrays for stacks, not for queues




# Stacks - Last in First Out (Lifo)

stk = []

# Append to top of stack - O(1)
stk.append(5)

stk.append(4)
stk.append(3)

print(stk)

# Pop from stack - O(1)
x = stk.pop()

# Ask what's on the top of stack - O(1) - Peek
print(stk[-1])

# Ask if something is in the stack - O(1) - True or False
if stk:
  print(True)

# Queues - First in First out (Fifo)

from collections import deque

q = deque()

# Enqueue - Add element to the right - O(1)
q.append(5)
q.append(6)
q.append(7)
print(q)

# Deqeue (pop left) - Remove element from the left - O(1)
q.popleft()

print(q)

# Peek from left side - O(1)
print(q[0])

# Peek from right side - O(1)
print(q[-1])