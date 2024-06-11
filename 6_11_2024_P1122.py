"""
1122. Relative Sort Array

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
"""



class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        
        output = []
        extra =[]
        for i in arr2:
            for j in arr1:
                if i ==j:
                    output.append(j)

        for i in arr1:
            if i not in arr2:
                extra.append(i)

        extra = sorted(extra)

        output += extra
        return output
