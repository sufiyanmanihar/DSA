class Solution:
    def isPalindrome(self, n: int) -> bool:
        if n<0:
            return False

        num = n
        reverse = 0
        while num>0:
            digit = num % 10 
            reverse = (reverse*10) + digit
            num = num//10
        return n == reverse

        