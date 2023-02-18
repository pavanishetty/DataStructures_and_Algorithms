/*
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
*/

import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        winStart = 0
        winSum = 0
        minLen = math.inf

        for winEnd in range(len(nums)):
            winSum += nums[winEnd]

            while winSum >= target:
                minLen = min(minLen, winEnd-winStart+1)

                winSum -= nums[winStart]
                winStart += 1

        if minLen == math.inf:
            minLen = 0
        return minLen
