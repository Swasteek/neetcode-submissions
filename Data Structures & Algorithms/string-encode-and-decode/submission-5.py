class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            x=len(i)
            s+=str(x)+"#"+i
        return s

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        i=0
        res=[]
        n=len(s)
        while i<n:
            num=""
            while i<n and s[i].isnumeric():
                num+=s[i]
                i+=1
            i+=1
            l=int(num)
            j=i+l
            res.append(s[i:j])
            i=j
        return res
