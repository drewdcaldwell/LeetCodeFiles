"""
846. Hand of Straights
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
"""
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        #Initial check
        if len(hand) % groupSize != 0:
            return False

        #get freq.
        c = collections.Counter(hand)

        #sort
        sort = sorted(c)

        for i in sort:
            if c[i] > 0:
                for j in range(groupSize)[::-1]:
                    c[i+j] -= c[i]
                    if c[i+j] < 0:
                        return False
        
        return True

