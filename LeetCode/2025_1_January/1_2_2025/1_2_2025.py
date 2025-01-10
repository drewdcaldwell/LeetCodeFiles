# 2559
# Prefix Sum
#
class Solution(object):
    def vowelStrings(self, words, queries):
        myList =[0]
        output=[]
        count = 0
        for i in words:
            if (i[0] =="a" or i[0] =="e" or i[0] =="i" or i[0] =="o" or i[0] =="u") and (i[-1] == "a" or i[-1] == "e" or i[-1] == "i" or i[-1] == "o" or i[-1] == "u"):
                count += 1
            myList.append(count)
        for i in queries:
            start = i[0]
            end = i[1]
            output.append(myList[end+1]-myList[start])
        return output
        