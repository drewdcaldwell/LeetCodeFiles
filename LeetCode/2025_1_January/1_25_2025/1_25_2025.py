#------------------------------------------------------------#
# Problem  Programmer  Date      Description                 #
#------------------------------------------------------------#
# 2948     DCALDWELL  1/25/25    Make Lexicographically      #
#                                Smallest Array by           #
#                                Swappping Elements          #
#------------------------------------------------------------#
"""
   :type nums: List[int]
   :type limit: int
   :rtype: List[int]
"""
# In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit
def lexicographicallySmallestArray(nums, limit):
    
    from collections import deque
    
    nums_sorted = sorted(nums)

    curr_group = 0
    num_to_group = {}
    num_to_group[nums_sorted[0]] = curr_group
    group_to_list = {}                                             # group_to_list is a dictionary where the key is a 
    group_to_list[curr_group] = deque([nums_sorted[0]])            # group identifier (curr_group), and the value is a deque (double-ended queue) 
                                                                   # that will hold the elements for that group.

    for i in range(1, len(nums)):
        if abs(nums_sorted[i] - nums_sorted[i - 1]) > limit:
                             # new group
            curr_group += 1
                             # assign current element to group
        num_to_group[nums_sorted[i]] = curr_group
                             # add element to sorted group deque
        if curr_group not in group_to_list:
            group_to_list[curr_group] = deque()
        group_to_list[curr_group].append(nums_sorted[i])
                             # iterate through input and overwrite each element 
                             # with the next element in its corresponding group
    for i in range(len(nums)):
        num = nums[i]
        group = num_to_group[num]
        nums[i] = group_to_list[group].popleft()                                # By using deque.popleft(), you always take the smallest available number 
                                                                                # from each group (since nums_sorted is sorted). This guarantees that the 
                                                                                # final result is the lexicographically smallest possible array after grouping and reordering.
        
    return nums              # Return the lexicographically smallest array 
                             # that can be obtained by performing the 
                             # operation any number of times.    
    

        
#Input: 
nums = [1,5,3,9,8]
limit = 2

print(lexicographicallySmallestArray(nums, limit))
#Output: [1,3,5,8,9]


#-------------------------------------------------------------------------#
#                         NOTES                                           #
#-------------------------------------------------------------------------#
# An array a is lexicographically smaller than an array b if in the first 
# position where a and b differ, array a has an element that is less than 
# the corresponding element in b. For example, the array [2,10,3] is 
# lexicographically smaller than the array [10,2,3] because they differ 
# at index 0 and 2 < 10.
