class Solution:
    def threeSum(self, numbers: List[int]) -> List[List[int]]:
        numbers.sort()
        result = []
        for i in range(len(numbers)):
            if i>0 and numbers[i] == numbers[i-1]:
                continue
            left = i+1
            right = len(numbers) - 1
            while left <right:
                total = numbers[left] + numbers[right] + numbers[i]
                if total > 0:
                    right -= 1
                if total < 0 :
                    left += 1
                if total == 0 :
                    result.append([numbers[i],numbers[left] , numbers[right]])
                    left += 1
                    right -=1
                    while left < right and numbers[left] == numbers[left-1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right+1]:
                        right -= 1
        return result    