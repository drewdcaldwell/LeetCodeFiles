# Shortened TLESolution and still got a TLE
# Will keep trying until I get it.
from collections import Counter

class Solution(object):
    def minimizeXor(self,num1, num2):
        def binaryToDecimal(binary):
            decimal, i = 0, 0
            while(binary != 0):
                dec = binary % 10
                decimal = decimal + dec * pow(2, i)
                binary = binary//10
                i += 1
            return decimal

        # Get the binary strings of numbers
        length1 = len(bin(num1)[2:])
        x_bin = "0"*(32-length1) + bin(num1)[2:]
        length2 = len(bin(num2)[2:])
        num2_bin = "0"*(32-length2) + bin(num2)[2:]
        # Count the number of 1's in num2
        xbin_freq = Counter(x_bin)
        num2_freq = Counter(num2_bin)
        i = len(x_bin)
        while num2_freq["1"] != xbin_freq["1"]:
            x_bin = x_bin[:i] + "1" + x_bin[i+1:]
            xbin_freq = Counter(x_bin)
            i -= 1
        return binaryToDecimal(int(x_bin))
