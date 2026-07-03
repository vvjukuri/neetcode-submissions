class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kfrequent = {}
        for number in nums:
            kfrequent[number] = kfrequent.get(number,0) + 1
        sorted_keys = sorted(kfrequent, key=lambda k: kfrequent[k], reverse=True)
        return sorted_keys[:k]
