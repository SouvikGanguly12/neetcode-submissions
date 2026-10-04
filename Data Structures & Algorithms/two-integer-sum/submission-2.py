class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            j = target - num
            if j in seen:
                return [seen[j], i]
            seen[num] = i