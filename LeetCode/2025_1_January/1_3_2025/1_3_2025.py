# 2270
class Solution(object):
    def waysToSplitArray(self, nums):
        totalSum = sum(nums)
        leftSide = 0
        count = 0
        for i in range(len(nums) -1):
            leftSide+= nums[i]
            totalSum -= nums[i]
            if leftSide >= totalSum:
                count += 1
        return count

        