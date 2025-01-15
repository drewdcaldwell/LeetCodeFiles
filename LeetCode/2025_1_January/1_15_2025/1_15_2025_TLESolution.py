# Actually really like the flow of this but unfortunately it's not fast enough


from collections import Counter

def minimizeXor(num1, num2):
    bits = countSetBits(bin(num2)[2:])
    # x must have at least bits many SetBits
    num1_bin = bin(num1)[2:]
    num1_freq = Counter(num1_bin)
    num2_bin = bin(num2)[2:]
    if len(num1_bin) < len(num2_bin):
        diff = len(num2_bin) - len(num1_bin)
        temp = num1_bin
        num1_bin = "0"*diff + temp
    i = len(num1_bin)
    while num1_freq["1"] != bits:
        num1_bin = num1_bin[:i] + "1" + num1_bin[i+1:]
        num1_freq = Counter(num1_bin)
        i -= 1
    return binaryToDecimal(int(num1_bin))
    
def countSetBits(num2):
    frequency = Counter(num2)
    return frequency["1"]
    
def binaryToDecimal(binary):
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal
    
# x has same num of 1's as num2
# Value of x XOR num1 is minimal
num1 = 3
num2 = 5
print(minimizeXor(num1,num2))  
