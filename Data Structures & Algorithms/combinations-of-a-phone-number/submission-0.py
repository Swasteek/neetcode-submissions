class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        cmb=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        path=[]
        ans=[]
        def f(ind):
            if ind==len(digits):
                ans.append("".join(path))
                return
            x=ord(digits[ind])-ord("2")
            for i in cmb[x]:
                path.append(i)
                f(ind+1)
                path.pop()
        f(0)
        return ans