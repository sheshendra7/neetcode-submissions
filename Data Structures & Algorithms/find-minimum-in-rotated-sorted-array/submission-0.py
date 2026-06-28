class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = nums[0]

        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                return nums[i]
            if nums[i] < minVal:
                minVal = nums[i]
        return minVal