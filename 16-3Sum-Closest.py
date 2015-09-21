# This solution is based on 15-3Sum_v3.py


class Solution(object):
    def _twoSumClosest(self, nums, current, target, closest):
        if len(nums) <= 1:
            return closest
        if nums[0] + nums[1] + current - target > abs(target - closest):
            return closest
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] + current - target >= abs(target - closest):
                j -= 1
            elif nums[i] + nums[j] + current - target <= -abs(target - closest):
                i += 1
            else:
                closest = nums[i] + nums[j] + current
                if closest == target:
                    return closest
        return closest

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 3:
            return sum(nums)
        nums = sorted(nums)
        closest = sum(nums[0:3])

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0 and nums[i] - target > abs(closest - target):
                break
            if nums[i] < 0 and 3 * nums[i] - target > abs(closest - target):
                break

            closest = self._twoSumClosest(nums[i + 1:], nums[i], target, closest)
            if closest == target:
                return closest

        return closest
