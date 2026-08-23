class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        diff = 0
        qdiff = 0

        for i in range(half):
            if num[i] == '?':
                qdiff += 1
            else:
                diff += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                qdiff -= 1
            else:
                diff -= int(num[i])

        return diff * 2 != -9 * qdiff