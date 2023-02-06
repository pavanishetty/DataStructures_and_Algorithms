/* Problem Statement 
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
*/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s)-1

        while lp < rp:
            while s[lp].isalnum() is not True and lp < rp:
                lp += 1
            while s[rp].isalnum() is not True and lp < rp:
                rp -= 1
            if s[lp].lower() != s[rp].lower():
                return False

            lp += 1
            rp -= 1
        
        return True
#think about when we have more than one delimiter consecutively ".,"
