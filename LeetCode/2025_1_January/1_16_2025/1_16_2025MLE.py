# You've gotta be kidding me
# How much smaller can I get
class Solution(object):
    def xorAllNums(self, nums1, nums2):
        array =[]
        output = 0
        for i in nums1:
            for j in nums2:
                array.append(i^j)
        for x in array:
            output = output ^ x
        return output
