# 1930
#
class Solution(object):
    def countPalindromicSubsequence(self, s):
        # Use a set to store unique palindromes of length 3
        palindromes = set()
    
        # Arrays to keep track of characters seen before and after the current index
        left_seen = [set() for _ in range(len(s))]
        right_seen = [set() for _ in range(len(s))]
        
        # Fill left_seen
        for i in range(1, len(s)):
            left_seen[i] = set(left_seen[i - 1])  # Copy the previous set
            left_seen[i].add(s[i - 1])
        
        # Fill right_seen
        for i in range(len(s) - 2, -1, -1):
            right_seen[i] = set(right_seen[i + 1])  # Copy the next set
            right_seen[i].add(s[i + 1])
        
        # Check for unique palindromes
        for i in range(1, len(s) - 1):
            for char in left_seen[i]:
                if char in right_seen[i]:
                    palindromes.add(char + s[i] + char)
        
        return len(palindromes)
        