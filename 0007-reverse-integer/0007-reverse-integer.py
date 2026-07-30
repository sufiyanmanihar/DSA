class Solution:
    def reverse(self, x: int) -> int:
        n = abs(x)

        # Reversing number
        reverse = 0
        while n>0:
            digit = n % 10
            reverse = (reverse*10) + digit
            n = n//10
        
        # check the negative condition
        if x < 0:
            reverse = -reverse 

        #checking the given range
        if reverse >= -2**31 and reverse <= 2**31 - 1:
            return reverse

        return 0