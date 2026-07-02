class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, number in enumerate(nums):
            needed = target - number
            if needed in seen:
                return [seen[needed],i]
            seen[number] = i
        return seen