class Solution(object):
    def longestCommonPrefix(self, strs):
        str1=min(strs,key=len)
        n=len(str1)
        
        ans=[]
        for i in strs:
            temp=""
            for j in range(0,n):
                if str1[j]==i[j]:
                    temp+=str1[j]
                else:
                    break
            ans.append(temp)
        ans1=min(ans,key=len)
        return ans1

                    

            
        