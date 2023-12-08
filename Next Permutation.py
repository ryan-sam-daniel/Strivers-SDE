from os import *
from sys import *
from collections import *
from math import *

def nextPermutation(permutation, n):
    # Write your code here.
    # Return a list.
    index=-1
    for i in range(n-2,-1,-1):
        if(permutation[i]<permutation[i+1]):
            index=i
            break;
    if(index==-1):
        permutation.reverse()
        return permutation
    for i in range(n-1,index,-1):
        if(permutation[i]>permutation[index]):
            permutation[i],permutation[index]=permutation[index],permutation[i]
            break
    permutation[index+1:]=reversed(permutation[index+1:])
    return permutation
