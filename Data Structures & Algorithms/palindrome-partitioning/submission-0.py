class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res,path=[],[]
        n=len(s)

        def backtrack(ind):
            if ind==n:
                res.append(path[:])
                return
            for i in range(ind,len(s)):
                sub=s[ind:i+1]
                if sub==sub[::-1]:
                    path.append(s[ind:i+1])
                    backtrack(i+1)
                    path.pop()
        backtrack(0)
        return res
        