class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        words = text.split()
        letters = list(brokenLetters)

        filtered_words = []

        for word in words:
            if not any(letter in word for letter in letters):
                filtered_words.append(word)
        return(len(filtered_words))