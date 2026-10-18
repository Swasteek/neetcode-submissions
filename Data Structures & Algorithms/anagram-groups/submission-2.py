class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp=defaultdict(list)
        for i in strs:
            x=sorted(list(i))
            q="".join(x)
            mpp[q].append(i)
        return list(mpp.values())