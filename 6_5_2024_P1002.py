"""
1002. Find Common Characters
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
"""
class Solution:
    def commonChars(self, words):
        ans = collections.Counter(words[0])
        for word in words:
            ans &= collections.Counter(word)
        return list(ans.elements())    
