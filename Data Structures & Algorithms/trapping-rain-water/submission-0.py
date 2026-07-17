class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxleft = 0
        maxright = 0
        water = 0
        while left < right:
            if height[left] <= height[right]:
                maxleft = max(maxleft, height[left]) 
                water += maxleft - height[left] 
                left += 1 
            else:
                maxright = max(maxright, height[right]) 
                water += maxright - height[right] 
                right -= 1 
        return water