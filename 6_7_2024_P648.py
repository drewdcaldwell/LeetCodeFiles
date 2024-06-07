"""
648. Replace Words
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative.
For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".
Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it.
If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.
Return the sentence after the replacement.
"""
class Solution(object):
    def replaceWords(self, dictionary, sentence):

        word_array = sentence.split()
        dict_set = set(dictionary)

        def shortest_root(word, dict_set):
            for i in range(len(word)):
                root = word[0:i]
                if root in dict_set:
                    return root
            return word
        
        for word in range(len(word_array)):
            word_array[word] = shortest_root(word_array[word], dict_set)

        return " ".join(word_array)
