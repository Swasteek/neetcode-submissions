class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s=s+str(len(i))+'#'+i
        return s

    def decode(self, s: str) -> List[str]:
        n=len(s)
        res=[]
        i=0
        while i<n:
            j=i+1
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            i=j+1
            j=i+length
            res.append(s[i:j])
            i=j
        return res
