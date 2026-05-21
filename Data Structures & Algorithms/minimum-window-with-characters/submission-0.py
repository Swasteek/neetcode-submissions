class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mpp=defaultdict(int)
        for i in t:
            mpp[i]+=1
        my=""
        l,cnt,x,mini=0,0,len(t),int(1e9)
        for r in range(len(s)):
            if mpp[s[r]]>=1:
                cnt+=1
            mpp[s[r]]-=1
            while cnt==x:
                if r-l+1<mini:
                    my=s[l:r+1]
                    mini=r-l+1
                mpp[s[l]]+=1
                if mpp[s[l]]>=1:
                    cnt-=1
                l+=1
        return my