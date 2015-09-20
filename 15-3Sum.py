class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums = sorted(nums)
        two_sum = {}
        three_sum = {}
        for i in range(len(nums)):
            two_dict = two_sum.get(0 - nums[i], None)
            if two_dict:
                for key, value in two_dict.iteritems():
                    tmp = list(value)
                    tmp.append(nums[i])
                    tmp = sorted(tmp)
                    three_sum["%d,%d,%d" % (tmp[0], tmp[1], tmp[2])] = tmp

            j = 0
            while j < i:
                add_value = nums[i] + nums[j]
                if not two_sum.get(add_value):
                    two_sum[add_value] = {}
                key = (nums[j], nums[i]) if nums[j] < nums[i] else (nums[i], nums[j])
                two_sum[add_value]["%s,%s" % key] = [nums[j], nums[i]]
                j += 1

        return [v for k, v in three_sum.iteritems()]
