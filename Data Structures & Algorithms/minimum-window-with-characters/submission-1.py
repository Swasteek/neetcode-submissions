class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mpp=defaultdict(int)
        for i in t:
            mpp[i]+=1
        cnt=0
        x=len(t)
        maxlen=float('inf')
        mys=""
        l=0
        for r in range(len(s)):
            if mpp[s[r]]>0:
                cnt+=1
            mpp[s[r]]-=1
            while cnt==x:
                if r-l+1<maxlen:
                    maxlen=r-l+1
                    mys=s[l:r+1]
                mpp[s[l]]+=1
                if mpp[s[l]]>0:
                    cnt-=1
                l+=1
        return mys