class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        self.tree = [None] * (4 * self.n)

        self.build(1, 0, self.n - 1, s)

    def build(self, node, left, right, s):
        # Leaf node
        if left == right:
            self.tree[node] = (
                s[left],   # left character
                s[left],   # right character
                1,         # length
                1,         # prefix
                1,         # suffix
                1          # best
            )
            return

        mid = (left + right) // 2

        self.build(node * 2, left, mid, s)
        self.build(node * 2 + 1, mid + 1, right, s)

        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def merge(self, left, right):
        # Extract information
        left_char = left[0]
        right_char = right[1]

        length = left[2] + right[2]

        prefix = left[3]
        suffix = right[4]

        # Best answer without crossing the boundary
        best = max(left[5], right[5])

        # If the two boundary characters are equal,
        # we can combine the suffix of left with prefix of right.
        if left[1] == right[0]:

            # A repeating sequence crosses the middle
            best = max(best, left[4] + right[3])

            # Entire left segment has the same character
            if left[3] == left[2]:
                prefix = left[2] + right[3]

            # Entire right segment has the same character
            if right[4] == right[2]:
                suffix = right[2] + left[4]

        return (
            left_char,
            right_char,
            length,
            prefix,
            suffix,
            best
        )

    def update(self, node, left, right, index, char):
        # Reached the required position
        if left == right:
            self.tree[node] = (
                char,
                char,
                1,
                1,
                1,
                1
            )
            return

        mid = (left + right) // 2

        if index <= mid:
            self.update(
                node * 2,
                left,
                mid,
                index,
                char
            )
        else:
            self.update(
                node * 2 + 1,
                mid + 1,
                right,
                index,
                char
            )

        # Recalculate current node
        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )


class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):

        n = len(s)

        # Build segment tree
        seg = SegmentTree(s)

        answer = []

        # Process every query
        for i in range(len(queryCharacters)):

            char = queryCharacters[i]
            index = queryIndices[i]

            # Update character at index
            seg.update(
                1,
                0,
                n - 1,
                index,
                char
            )

            # Root contains the answer for entire string
            answer.append(seg.tree[1][5])

        return answer