# 1422
#
class Solution(object):
    def maxScore(self, s):
        i = 1
        length = len(s)
        maxScore = 0
        while i < length:
            rightSub = s[-(length-i):]
            leftSub = s[:i]
            score = 0
            j = 0
            while(j < len(rightSub)):
                if(rightSub[j] == "1"):
                    score += 1
                j+= 1 
            k = 0
            while(k < len(leftSub)):
                if(leftSub[k] == "0"):
                    score += 1
                k+= 1 
            if score > maxScore:
                maxScore = score
            i += 1

        return maxScore
        