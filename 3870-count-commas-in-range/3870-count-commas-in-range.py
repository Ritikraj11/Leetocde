import math
class Solution:
    def countCommas(self, n: int) -> int:
        # l = math.ceil(math.log10(n))
        # div = math.ceil(l/3)

        if n < 999:
            return 0
        else:
            return n - 999

        