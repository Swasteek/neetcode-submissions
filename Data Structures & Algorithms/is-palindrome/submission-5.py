class Solution:
    def isPalindrome(self, s: str) -> bool:
        my=""
        for i in s:
            if i.isalnum():
                my+=i.lower()
        return my==my[::-1]