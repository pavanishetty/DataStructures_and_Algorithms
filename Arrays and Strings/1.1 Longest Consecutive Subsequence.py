/*
Longest Consecutive Sequence: Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time. */

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSeq = 0
        nums = set(nums)
        for n in nums:
            if n-1 not in nums:
                length = 0
                while n+length in nums:
                    length += 1

                longestSeq = max(length, longestSeq)
        return longestSeq