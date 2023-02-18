/*
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
*/

import math
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        winStart = 0
        winSum = 0.0
        res = float(-inf)

        for i in range(len(nums)):
            winSum += nums[i]

            if i >= k-1:
                avgSum = winSum / k
                res = max(res, avgSum)

                winSum -= nums[winStart]
                winStart += 1

        return res