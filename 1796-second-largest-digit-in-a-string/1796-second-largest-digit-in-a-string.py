class Solution:
    def secondHighest(self, s: str) -> int:
        largest = -1
        second = -1

        for char in s:
            if char.isdigit():
                digit = int(char)

                if digit > largest:
                    second = largest
                    largest = digit

                elif largest > digit > second:
                    second = digit

        return second