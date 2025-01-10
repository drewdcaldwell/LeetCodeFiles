class Solution(object):
    def wordSubsets(self, words1, words2):
        from collections import Counter
        # Get min frequency that words in words1 must have
        freq = Counter()
        for w in words2:
            # Count the current word
            current = Counter(w)
            # For each character in the word we just counted
            for char in current:
                # Change the frequency of that char in our freq. hash if the val
                # is greater than what is currently in freq.
                freq[char] = max(freq[char],current[char])
        # Initialize Output
        output = []
        # Get words containing subsets
        for w in words1:
            # Count the freq of current word in words1
            current = Counter(w)
            # If for every character in the word in words1. The min freq is met
            if all(current[char] >= freq[char] for char in freq):
                # Add the word in word1 to output
                output.append(w)
        return output
