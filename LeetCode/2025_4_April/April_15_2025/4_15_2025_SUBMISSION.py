#------------------------------------------------------------#
# Problem  Programmer  Date      Description                 #
#------------------------------------------------------------#
# 1534     DCALDWELL   041525    Counting "good" triplets    #
#------------------------------------------------------------#

class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        arr_length = len(arr)
        count = 0
        for i in range(arr_length-2):
            for j in range(i+1,arr_length-1):
                for k in range(j+1, arr_length):
                    a_val = abs(arr[i] - arr[j])
                    b_val = abs(arr[j] - arr[k])
                    c_val = abs(arr[i] - arr[k])
                    if a_val <= a and b_val <= b and c_val <= c:
                        count += 1
        return count
  
