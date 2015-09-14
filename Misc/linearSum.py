
__author__ = 'shearora'

def linear_sum(s,n):
    if(n==0):
        return 0
    else:
        return linear_sum(s,n-1)+s[n]

s = [0,1,2,3]
print(linear_sum(s,3))