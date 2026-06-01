class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        if n==1:
            return strs[0]
        w1,w2=strs[0],strs[1]
        a=0
        minl=min(len(w1),len(w2))

        while a<minl and w1[a]==w2[a]:
            a+=1
        for i in range(2,n):
            cw=strs[i]
            while cw[:a]!=w1[:a]:
                a-=1
        return w1[:a]
        