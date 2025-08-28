class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif x == 0:
            return 0

        res = 1
        power = abs(n)

        while power:
            if power % 2 != 0:
                res *= x
            
            x *= x
            power //= 2
        
        return res if n > 0 else 1 / res