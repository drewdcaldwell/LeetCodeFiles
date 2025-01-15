# 2429. Took way too long
# 1/15/2025
from collections import Counter

class Solution(object):
    def minimizeXor(self,num1, num2):
        b1 = bin(num1)[2:]
        b2 = bin(num2)[2:]
        count_num2 = b2.count("1")
        if len(b2)>len(b1):
            b1 = b1.zfill(len(b2))
        else:
            b2 = b2.zfill(len(b1))
        a1 = [0]*len(b1)
        change = 0
        for i in range(len(b1)):
            if b1[i]=="1" and count_num2>0:
                a1[i]=1
                count_num2-=1
                if i == len(b1)-1:
                    change = 1
            if i==len(b1)-1:
                if count_num2>0:
                    for j in range(len(b1)-1,-1,-1):
                        if change == 1:
                            change = 0
                            continue
                        if a1[j]==0 and count_num2>0:
                            a1[j]=1
                            count_num2-=1
        ans = 0
        for i in a1:
            ans = ans*2 + i

        return ans
    
        
