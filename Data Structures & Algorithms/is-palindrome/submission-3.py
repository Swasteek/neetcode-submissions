class Solution:
    def isPalindrome(self, s: str) -> bool:
        my=[i.lower() for i in s if i.isalnum()]
        print(my)
        return my==my[::-1]