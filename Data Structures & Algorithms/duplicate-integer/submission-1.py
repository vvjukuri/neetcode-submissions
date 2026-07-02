class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for number in nums:
            if number in dup:
                return True
            dup.add(number)
        return False