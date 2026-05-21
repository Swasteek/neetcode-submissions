class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def f(oc,cc,ans):
            if oc==cc==n:
                res.append(ans)
                return
            if oc<n:
                f(oc+1,cc,ans+'(')
            if cc<oc:
                f(oc,cc+1,ans+')')
        f(0,0,"")
        return res