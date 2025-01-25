##############################################
# Learning how to use the deque from Collections
#
##############################################

# deque stands for DOUBLE - ENDED QUEUE
# Better than normal queue because it allows operations on both ends


from collections import deque

# Create a deque
d = deque([1, 2, 3])

# Add elements to the right (back)
d.append(4)
print(d)  # Output: deque([1, 2, 3, 4])

# Add elements to the left (front)
d.appendleft(0)
print(d)  # Output: deque([0, 1, 2, 3, 4])

# Remove elements from the right (back)
d.pop()
print(d)  # Output: deque([0, 1, 2, 3])

# Remove elements from the left (front)
d.popleft()
print(d)  # Output: deque([1, 2, 3])


#######   Key Methods   #########################

# Key Methods of deque:

#  append(x):            Adds x to the right (end) of the deque.
#  appendleft(x):        Adds x to the left (front) of the deque.
#  pop():                Removes and returns the rightmost (last) element.
#  popleft():            Removes and returns the leftmost (first) element.
#  extend(iterable):     Adds all elements from the iterable to the right of the deque.
#  extendleft(iterable): Adds all elements from the iterable to the left of the deque.
