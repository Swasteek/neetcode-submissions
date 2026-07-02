class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mpp=defaultdict(int)
        res=0
        maxf=0
        left=0
        for right in range(len(s)):
            mpp[s[right]]+=1
            maxf=max(maxf,mpp[s[right]])
            while (right-left+1)-maxf>k:
                mpp[s[left]]-=1
                left+=1
            res=(right-left+1)
        return res