def LongestSubsetWithZeroSum(arr):
    # Write your code here.
    mpp = {}
    sum_val = 0
    maxi = 0
    for i in range(len(arr)):
        sum_val += arr[i]
        if sum_val == 0:
            maxi = i + 1
        else:
            if sum_val in mpp:
                maxi = max(maxi, i - mpp[sum_val])
            else:
                mpp[sum_val] = i
    return maxi
