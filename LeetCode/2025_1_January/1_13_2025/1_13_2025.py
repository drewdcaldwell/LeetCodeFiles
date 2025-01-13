######################################
#    3223                  1/13/2025    
######################################
class Solution(object):
    def minimumLength(self, s):
        from collections import Counter
        frequency = Counter(s)
        sum = 0
        for i in frequency:
            if frequency[i] % 2 == 0:
                frequency[i] = 2
            else:
                frequency[i] = 1
            sum += frequency[i]
        return sum


"""
#######################################
#  Test Code
########################################

def minimumLength(s):
    from collections import Counter
    frequency = Counter(s)
    sum = 0
    for i in frequency:
        if frequency[i] % 2 == 0:
            frequency[i] = 2
        else:
            frequency[i] = 1
        sum += frequency[i]
    return sum
        
    
s = "abaacbcbb"
print(minimumLength(s))

"""
