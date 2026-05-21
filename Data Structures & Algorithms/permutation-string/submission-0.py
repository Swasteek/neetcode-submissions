class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1=Counter(s1)
        n1,n2=len(s1),len(s2)
        for i in range(n2-n1+1):
            if s2[i] in c1:
                c2=Counter(s2[i:i+n1])
                if c1==c2:
                    return True
        return False

        