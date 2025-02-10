# 3174
# Fun stack question

class Solution(object):
    def clearDigits(self, s):
        import re
        i = 0
        s_array = []
        output = ""
        while i < len(s):
            if re.match("[a-z]", s[i]):
                s_array.append(s[i])
            if re.match("[0-9]", s[i]):
                s_array.pop()
            i += 1

        for i in s_array:
            output += i

        return output
