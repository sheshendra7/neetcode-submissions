class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        res =0 
        while l < r:
            area = (abs((r+1)-(l+1))) * min(heights[l],heights[r])
            if area > res :
                res =area
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res