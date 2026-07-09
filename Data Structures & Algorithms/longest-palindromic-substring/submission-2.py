class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==1:
            return s
        longest=1
        my=s[0]
        for i in range(n):
            prev=i-1
            next=i+1
            while prev>=0 and next<n and s[prev]==s[next]:
                new=next-prev+1
                if new>longest:
                    longest=new
                    my=s[prev:next+1]
                prev-=1
                next+=1
        for i in range(n):
            prev=i
            next=i+1
            while prev>=0 and next<n and s[prev]==s[next]:
                new=next-prev+1
                if new>longest:
                    longest=new
                    my=s[prev:next+1]
                prev-=1
                next+=1

        return my

        