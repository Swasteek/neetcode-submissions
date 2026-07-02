class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            res+=str(len(i))+"#"+i
        return res
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        n=len(s)
        while i<n:
            x=""
            while i<n and s[i]!="#":
                x+=s[i]
                i+=1
            length=int(x)
            i+=1
            j=i+length
            res.append(s[i:j])
            i=j
        return res