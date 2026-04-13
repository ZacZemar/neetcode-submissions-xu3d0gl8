class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        stored_container = 0

        while left < right:
            width = right - left
            container_product = width * min(height[left], height[right])
            stored_container = max(container_product, stored_container)
            if height[left] <= height[right]:
                left += 1
            else:
                right -=1

        return stored_container
        