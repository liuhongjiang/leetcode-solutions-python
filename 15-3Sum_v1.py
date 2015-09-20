class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        positives = {}
        negatives = {}
        zeros = 0
        for num in nums:
            if num > 0:
                positives[num] = 1
            else:
                negatives[num] = 1

            if num == 0:
                zeros += 1

        three_sum = {}
        for i in range(len(nums)):

            if nums[i] <= 0:
                j = 0
                while j < i:
                    add_value = nums[i] + nums[j]
                    if -add_value in positives:
                        tmp = [nums[i], nums[j], -add_value]
                        tmp = sorted(tmp)
                        three_sum["%d,%d,%d" % tuple(tmp)] = tmp
                    j += 1
            else:
                j = len(nums) - 1
                while j > i:
                    add_value = nums[i] + nums[j]
                    if -add_value in negatives:
                        tmp = [nums[i], nums[j], -add_value]
                        tmp = sorted(tmp)
                        three_sum["%d,%d,%d" % tuple(tmp)] = tmp
                    j -= 1

        three_list = [v for k, v in three_sum.iteritems()]
        if zeros >= 3:
            three_list.append([0,0,0])

        return three_list