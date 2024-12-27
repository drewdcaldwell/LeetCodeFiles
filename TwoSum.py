class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        j = 1
        arr = []
        while i < len(nums):
            j = i+1
            while j < len(nums):
                if nums[i] +nums[j] == target:
                    arr.append(i)
                    arr.append(j)
                    return arr
                j += 1
            i+= 1 
