# -*- encoding: utf8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        k %= len(nums)
        nums[:] = nums[-k:]+nums[:-k]
        return nums

if __name__ == "__main__":
    so = Solution()
    nums = [1, 2]
    k = 1
    print so.rotate(nums, k)