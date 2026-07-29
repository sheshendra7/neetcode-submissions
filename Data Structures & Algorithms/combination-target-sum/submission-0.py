class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, arr, tot):
            if tot == target:
                res.append(arr.copy())
                return
            
            if i >= len(nums) or tot > target:
                return
            
            arr.append(nums[i])
            backtrack(i, arr, tot+nums[i])
            arr.pop()
            backtrack(i+1,arr, tot)
            
        
        backtrack(0,[],0)
        return res