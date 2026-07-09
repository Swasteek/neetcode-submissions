class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        
        
        cnt=0
        for i in range(n):
            prev=i
            next=i
            while prev>=0 and next<n and s[prev]==s[next]:
                prev-=1
                next+=1
                cnt+=1
        for i in range(n):
            prev=i
            next=i+1
            while prev>=0 and next<n and s[prev]==s[next]:
                prev-=1
                next+=1
                cnt+=1

        return cnt
