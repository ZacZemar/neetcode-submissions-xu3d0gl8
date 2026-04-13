class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)
        output = []

        for i in range(len(sorted(nums))):
            start = sorted_nums[i]
            left = i + 1
            right = len(sorted_nums) -1
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            while left < right:
                if start + sorted_nums[left] + sorted_nums[right] < 0:
                    left += 1
                elif start + sorted_nums[left] + sorted_nums[right] > 0:
                    right -= 1
                elif start + sorted_nums[left] + sorted_nums[right] == 0:
                    output.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                        right -= 1
        return output