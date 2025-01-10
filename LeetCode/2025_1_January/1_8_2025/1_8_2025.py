# 3042, Easy
#
class Solution(object):
    def countPrefixSuffixPairs(self, words):
        def isPrefixAndSuffix(str1, str2):
            if str1 == str2[-len(str1):] and str1 == str2[:len(str1)]:
                return True
            return False
        
        count = 0
        i = 0
        j = 1
        while i < len(words):
            j = i + 1
            while j < len(words):
                temp = False
                if i != j:
                    temp = isPrefixAndSuffix(words[i],words[j])
                    if temp is True:
                        count += 1
                j += 1
            i += 1

        return count