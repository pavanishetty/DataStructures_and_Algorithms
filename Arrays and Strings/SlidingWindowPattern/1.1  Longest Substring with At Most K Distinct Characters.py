/*
Longest Substring with At Most K Distinct Characters
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.
*/

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        winStart = 0
        maxLen = 0
        hashmap = {}
        charCount = 0

        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 0
            hashmap[s[i]] += 1
            charCount += 1

            while(len(hashmap)>k):
                 hashmap[s[winStart]] -= 1
                 charCount -= 1
                 if hashmap[s[winStart]] == 0:
                     del hashmap[s[winStart]]
                 winStart += 1

            maxLen = max(maxLen, charCount) 

        return maxLen