class Solution:
    def countBits(self, n: int) -> list[int]:
        num_ones = []

        for num in range(n + 1):
            num_one_bits = 0

            while num > 0:
                num_one_bits += 1 if num & 1 else 0
                num >>= 1
            
            num_ones.append(num_one_bits)
        
        return num_ones