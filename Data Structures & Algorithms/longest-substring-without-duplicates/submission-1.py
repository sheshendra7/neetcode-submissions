class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmpSet = set()
        j = 0
        res = 0
        for i in range(len(s)):
            while s[i] in tmpSet:
                tmpSet.remove(s[j])
                j += 1
            tmpSet.add(s[i])
            res = max(abs(j-i)+1,res)
        
        return res