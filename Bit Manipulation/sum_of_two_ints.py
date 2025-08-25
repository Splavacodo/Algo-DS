class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_signed = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1

            a = (a ^ b) & mask
            b = carry & mask
        
        return a if a <= max_signed else ~(a ^ mask)
            