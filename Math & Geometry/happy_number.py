class Solution:
    def isHappy(self, n: int) -> bool:
        nums_seen = set()

        while n != 1:
            digit_sum = 0

            for num in str(n):
                digit_sum += int(num)**2
            
            if digit_sum in nums_seen:
                return False
            else:
                nums_seen.add(digit_sum)
                n = digit_sum
        
        return True
            
