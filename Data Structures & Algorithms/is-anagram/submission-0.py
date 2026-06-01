class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mpps,mppt={},{}
        for i in s:
            mpps[i]=mpps.get(i,0)+1
        for i in t:
            mppt[i]=mppt.get(i,0)+1
        return mpps==mppt

        