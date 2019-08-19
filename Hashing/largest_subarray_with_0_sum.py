# Given an array having both positive an negative integers, returns the length of maximum subarray with 0 sum. 
# O(n) approach using hashing

def maxLen(arr):
    cur_sum=0
    max_len=0
    hash={}
    for i in range(len(arr)):
        cur_sum += arr[i]
        
        if cur_sum == 0:
            max_len = i+1
        
        if cur_sum in hash:
            l = (i-hash[cur_sum])
            if l>max_len:
                max_len=l   
        else:
            hash[cur_sum]=i
            
    return max_len

arr = [15,-2,2,-8,1,7,10,23]
print(maxLen(arr))


