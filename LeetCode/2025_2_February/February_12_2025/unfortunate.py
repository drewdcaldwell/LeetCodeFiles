# TLE
# Doesn't like O(n^2) :(

class Solution(object):
    def maximumSum(self,nums):
        def getSum(num):
            s_num = str(num)
            sum = 0
            j = 0
            while j < len(s_num):
                sum += int(s_num[j])
                j += 1
            return sum
        maxi = 0
        for i in range(len(nums)):
            #print(i)
            for j in range(i+1,len(nums)):
                #print(j)
                temp_max = 0
                if getSum(nums[i]) == getSum(nums[j]):
                    #print(getSum(nums[i]))
                    #print(getSum(nums[j]))
                    temp_max = nums[i] + nums[j]
                    maxi = max(maxi, temp_max)
        if maxi != 0:
            return maxi
        else: 
            return -1
        
