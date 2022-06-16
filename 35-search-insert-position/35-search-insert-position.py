class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            current = start + ((end - start) // 2)
            if nums[current] == target:
                return current
            elif nums[current] < target:
                start = current + 1
            else:
                end = current - 1
        if nums[current] < target:
            return current + 1
        else:
            if current == 0:
                return 0
            else:
                return current