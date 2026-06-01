class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp=defaultdict(list)
        for i in strs:
            x="".join(sorted(i))
            mpp[x].append(i)
        return list(mpp.values())