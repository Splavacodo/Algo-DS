class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        product = [0 for _ in range(len(num1) + len(num2))]

        num1, num2 = num1[::-1], num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])

                product[i + j] += digit
                product[i + j + 1] += product[i + j] // 10
                product[i + j] %= 10
        
        product = product[::-1]
        start = 0

        while product[start] == 0:
            start += 1
        
        product = map(str, product[start:])

        return "".join(product)
