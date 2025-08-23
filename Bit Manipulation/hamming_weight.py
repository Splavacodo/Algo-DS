class Solution:
    def hammingWeight(self, n: int) -> int:
        num_set_bits = 0

        while n > 0:
            if n % 2 != 0:
                num_set_bits += 1
            
            n = n >> 1
        
        return num_set_bits   
