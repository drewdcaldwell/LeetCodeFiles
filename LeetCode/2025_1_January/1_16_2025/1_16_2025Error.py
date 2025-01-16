# Different approach but not the correct answer yet...

class Solution(object):
    def xorAllNums(self, nums1, nums2):
        from collections import Counter
        output = 0
        freq1 = Counter(nums1)
        for i in freq1:
            freq1[i] += len(nums1)
        freq2 = Counter(nums1)
        for i in freq2:
            freq2[i] += len(nums2)
        freq = freq1+freq2
        for num in freq:
            if freq[num] %2:
                output ^= num
        return output
