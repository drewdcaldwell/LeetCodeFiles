#------------------------------------------------------------#
# Problem  Programmer  Date      Description                 #
#------------------------------------------------------------#
# 2683     DCALDWELL   1/17/25   Neighboring Bitwise XOR,    #
#                                Medium Difficulty           #
#------------------------------------------------------------#

class Solution(object):
    def doesValidArrayExist(self, derived):
        return sum(derived) % 2 == 0
        
