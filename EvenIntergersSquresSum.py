
'''
Created on 22 May 2019

@author: vinod.pasalkar
'''
# This program print the sum of the squares of all even members from a list of integers. 

def sum_even_num(l):
        sum = 0
        for n in l:
            if n % 2 == 0:
                 sum=sum + (n**2)
            
        return sum    
print(sum_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

