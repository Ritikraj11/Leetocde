class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(num):
            prod = 1
            while num > 0:
                prod *= num % 10
                num //= 10
            return prod

        x = n
        while True:
            if digit_product(x) % t == 0:
                return x
            x += 1