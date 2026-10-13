class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = 0
        seen = []
        while n < len(nums):
            if nums[n] not in seen:
                seen.append(nums[n])
                n += 1
            else:
                return True
        return False
            

