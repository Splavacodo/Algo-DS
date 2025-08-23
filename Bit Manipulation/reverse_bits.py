class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_bits = 0

        for i in range(32):
            bit = (n >> i) & 1
            reversed_bits += bit << (31 - i)
        
        return reversed_bits