class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start_idx = 0
        end_idx = len(nums) - 1
        current_idx = (end_idx - start_idx) // 2
        if len(nums) == 1:
            if nums[current_idx] == target:
                return current_idx
            else:
                return -1
        while start_idx != end_idx + 1:
            if nums[current_idx] == target:
                return current_idx
            elif nums[current_idx] < target:
                start_idx = current_idx + 1
                current_idx = start_idx + ((end_idx - start_idx) // 2)
            else:
                end_idx = current_idx - 1
                current_idx = start_idx + ((end_idx - start_idx) // 2)
        return -1
        
        