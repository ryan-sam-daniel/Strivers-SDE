from math import *
from collections import *
from sys import *
from os import *

def rotateMatrix(mat, n, m):

    # Write your code here
    for layer in range(min(n,m)//2):
        top_row=mat[layer][layer]
        for i in range(layer,n-layer-1):
            mat[i][layer]=mat[i+1][layer]
        for i in range(layer,m-layer-1):
            mat[n-layer-1][i]=mat[n-layer-1][i+1]
        for i in range(n-layer-1,layer,-1):
            mat[i][m-layer-1]=mat[i-1][m-layer-1]
        for i in range(m-layer-1,layer,-1):
            mat[layer][i]=mat[layer][i-1]
        mat[layer][layer+1]=top_row
