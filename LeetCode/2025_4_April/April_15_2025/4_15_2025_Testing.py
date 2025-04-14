def countGoodTriplets(arr, a, b, c):
    arr_length = len(arr)
    count = 0
    #print(arr_length)
    for i in range(arr_length-2):
        for j in range(i+1,arr_length-1):
            for k in range(j+1, arr_length):
                # Testing the outputs to make sure I am using correct indices
                #print("===================BEGINNING=========================")
                #print("     i: " +str(i) + "        j: " +str(j) +"        k: " +str(k) )
                #print("arr[i]: " +str(arr[i]) + "  arr[j]: " +str(arr[j]) +"  arr[k]: " +str(arr[k]) )
                #print("====================++END++==========================")
                a_val = abs(arr[i] - arr[j])
                b_val = abs(arr[j] - arr[k])
                c_val = abs(arr[i] - arr[k])
                if a_val <= a and b_val <= b and c_val <= c:
                    # Testing to ensure I get the expected good triplets.
                    #print("GOOD TRIPLET: i=" +str(arr[i]) +", j= " +str(arr[j]) +", k = "+str(arr[k]))
                    count += 1
    return count
  
arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3

print(countGoodTriplets(arr,a,b,c))
        
