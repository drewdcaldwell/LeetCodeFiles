"""
409. Longest Palindrome
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.
"""

class Solution:
    def longestPalindrome(self, s):
        charFrequency = Counter(s)
        oddFrequencyCount = 0
        for frequency in charFrequency.values():
            if frequency % 2 == 1:
                oddFrequencyCount += 1
        if oddFrequencyCount > 1:
            return len(s) - oddFrequencyCount + 1
        return len(s)
            
