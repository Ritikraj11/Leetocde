class Solution:
    def stoneGameIX(self, stones):
        c0 = 0
        c1 = 0
        c2 = 0

        for stone in stones:
            if stone % 3 == 0:
                c0 += 1
            elif stone % 3 == 1:
                c1 += 1
            else:
                c2 += 1

        # Case 1: even number of 0-remainder stones
        if c0 % 2 == 0:
            return c1 > 0 and c2 > 0

        # Case 2: odd number of 0-remainder stones
        return abs(c1 - c2) > 2