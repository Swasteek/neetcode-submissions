class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mpp={}
        res=0
        l=0
        maxf=0
        for r in range(len(s)):
            mpp[s[r]]=1+mpp.get(s[r],0)
            maxf=max(maxf,mpp[s[r]])
            if r-l+1-maxf>k:
                mpp[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res