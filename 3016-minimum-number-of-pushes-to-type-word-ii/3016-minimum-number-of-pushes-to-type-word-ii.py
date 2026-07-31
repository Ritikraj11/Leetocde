from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        letter_c = Counter(word)
        total = 0
        sorted_c = sorted(letter_c.values(),reverse=True)
        for i, count in enumerate(sorted_c):
            if  i < 8:
                total += count
            elif i < 16:
                total += count * 2
            elif i < 24:
                total += count * 3
            else:
                total += count * 4
        return total 