class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = ""

        for ch in s:
            if ord('a') <= ord(ch) <= ord('z') or ord('0') <= ord(ch) <= ord('9'):
                res+= ch
        
        l,r = 0,len(res)-1

        while l < r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1
        
        return True