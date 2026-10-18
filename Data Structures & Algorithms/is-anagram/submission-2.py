class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mpps=Counter(s)
        mppt=Counter(t)
        return mpps==mppt