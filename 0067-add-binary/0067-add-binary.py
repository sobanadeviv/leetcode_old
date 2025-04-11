class Solution(object):
    def addBinary(self, a, b):
        x1=int(a,2)
        y1=int(b,2)
        z=bin(x1+y1)
        return z[2:]
        