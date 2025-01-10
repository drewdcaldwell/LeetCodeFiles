# 1408
#
class Solution(object):
    def stringMatching(self, words):
        string = ""
        output = []
        temp = 0
        for i in words:
            string = ""
            for j in words:
                if i != j:
                    string += j + " "
            if i in string:
                output.append(i)
        return output

 