#------------------------------------------------------------#
# Problem  Programmer  Date        Description               #
#------------------------------------------------------------#
# 3105     DCALDWELL   02/03/2025  Longest Monotonic Subarray#
#------------------------------------------------------------#


class Solution(object):
    def longestMonotonicSubarray(nums):
        count = 0
        maxi = float('-inf')
        mini = float('-inf')
        for i in range(len(nums) -1):
            if nums[i] < nums[i+1]:
                count += 1
            else: 
                count = 0
            maxi = max(maxi, count)

        count = 0
        for j in range(len(nums) - 1):
            if nums[j] > nums[j+1]:
                count += 1
            else: 
                count = 0
            mini = max(mini, count)

        if len(nums) == 1:
            return 1

        return (max(maxi, mini)+1)