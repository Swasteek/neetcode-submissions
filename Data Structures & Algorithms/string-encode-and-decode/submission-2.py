class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=str(len(i))+"#"+i
        return s
    def decode(self, s: str) -> List[str]:
        li=[]
        i=0
        n=len(s)
        while i<n:
            j=i
            length=""
            while j<n and s[j]!='#':
                length+=s[j]
                j+=1
            i=j+1
            x=int(length)
            j=i+x
            li.append(s[i:j])
            i=j
        return li