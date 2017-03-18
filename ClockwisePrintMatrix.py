# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 16:27:44 2017
对于一个矩阵，请设计一个算法从左上角(mat[0][0])开始，顺时针打印矩阵元素。
给定int矩阵mat,以及它的维数nxm，请返回一个数组，数组中的元素为矩阵元素的顺时针输出。
测试样例：
[[1,2],[3,4]],2,2
返回：[1,2,4,3]
@author: Jessy
"""
#mat = [[5],
#       [6],
#       [7]
#       ]
import numpy as np
mat =np.array( [[5,6,2],
                [6,8,9],
                [7,1,4]
       ])
mat =np.array( [[5,6,2,1],
                [6,8,9,8],
                [7,1,4,12]
       ])
class Printer:
    def get_block(self, mat, n, m):
        # write code here
        out=[]
        start=[]
        if n < 2 or  m < 2:
            if n == 1 :
                out = mat[0]
            else:
                out = np.reshape(mat,(n,))
            return out
#        
        else:
            start = mat[0]
            end = mat[n-1][::-1]
            middle_left = mat[:,0][::-1][1:-1]
            middle_right = mat[:,m-1][1:-1]
            return np.concatenate((start,middle_right,end,middle_left))
 


    def clockwisePrint(self, mat, n, m):
        result = []
        while (n>0) & (m>0):
            result.extend(self.get_block(mat,n,m))
            n=n-2
            m=m-2
            mat=mat[1:-1,1:-1]
        return result
P=Printer() 
mat_new = P.get_block(mat,3,4)
result=P.clockwisePrint(mat,3,4)
