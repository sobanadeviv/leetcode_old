class Solution(object):
    def romanToInt(self, s):
        arr1=["I","V","X","L","C","D","M"]
        arr2=[1,5,10,50,100,500,1000]
        n=len(s)
        ans=0
        j=0
        for i in range(n-1,-1,-1):
            ele=s[i]
            ind=arr1.index(ele)
            val=arr2[ind]
            if j>val:
                ans=ans-val
            else:
                ans=ans+val
                j=val
           
        return ans
            
        
