"""
2486. Append Characters to String to Make Subsequence
You are given two strings s and t consisting of only lowercase English letters.
Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
"""
class Solution(object):
    def appendCharacters(self, s, t):
        sLength = len(s)
        tLength = len(t)
        sPointer = 0
        tPointer = 0

        while sPointer < sLength and tPointer < tLength:
            if s[sPointer] == t[tPointer]:
                tPointer += 1
            sPointer += 1
        return tLength - tPointer
