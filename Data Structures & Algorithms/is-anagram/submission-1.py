class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        mpps,mppt={},{}
        for i in s:
            mpps[i]=1+mpps.get(i,0)
        for j in t:
            mppt[j]=1+mppt.get(j,0)
        return mpps==mppt