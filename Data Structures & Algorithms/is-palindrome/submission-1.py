class Solution:
    def isPalindrome(self, s: str) -> bool:
        d=[i.lower() for i in s if i.isalnum()]
        return d==d[::-1]
        