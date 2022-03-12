class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        start = 1
        for idx, val in enumerate(nums):
            target_diff = target - val
            for idx_2, val_2 in enumerate(nums[idx+1:], idx+1):
                if val_2 == target_diff:
                    result.append(idx)
                    result.append(idx_2)
                    return result