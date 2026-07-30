class Solution:
    def minimumPushes(self, word: str) -> int:
        push_count = 0
        if len(word) <= 8 :
            return(len(word))
        if len(word) > 8 and len(word)<=16:
            extra = len(word) - 8
            return (8 + extra*2)
        if len(word) > 16 and len(word) <= 24:
            ex1 = len(word) - 16
            return (8 + 8*2 + ex1*3)
        else:
            ex = len(word) - 24
            return (8 + 8*2 + 8*3 + ex*4)