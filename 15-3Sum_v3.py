# this Solution has the best performance among all 15-3sum*.py.


class Solution(object):
    def _twoSum(self, nums, target, three_sum):
        if len(nums) <= 1:
            return
        if nums[0] + nums[1] > target:
            return
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                three_sum.append([-target, nums[i], nums[j]])
                while i < j:
                    if nums[i] == nums[i + 1]:
                        i += 1
                    elif nums[j] == nums[j - 1]:
                        j -= 1
                    else:
                        i += 1
                        break
        return

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        three_sum = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            self._twoSum(nums[i + 1:], -nums[i], three_sum)
        return three_sum

