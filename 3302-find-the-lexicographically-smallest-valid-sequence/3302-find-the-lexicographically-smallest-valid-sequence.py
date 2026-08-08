from bisect import bisect_left
from typing import List


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        # positions[c] = all indices where character c occurs in word1
        positions = [[] for _ in range(26)]

        for i, ch in enumerate(word1):
            positions[ord(ch) - ord('a')].append(i)

        # ---------------------------------------------------------
        # run_start[i] = first index of the same-character run
        # run_end[i]   = last index of the same-character run
        # ---------------------------------------------------------

        run_start = [0] * n
        run_end = [0] * n

        start = 0
        for i in range(n):
            if i > 0 and word1[i] != word1[i - 1]:
                start = i
            run_start[i] = start

        end = n - 1
        for i in range(n - 1, -1, -1):
            if i < n - 1 and word1[i] != word1[i + 1]:
                end = i
            run_end[i] = end

        # ---------------------------------------------------------
        # exact[j]
        #
        # Largest index from which word2[j:] can be matched
        # EXACTLY.
        #
        # exact[m] = n means empty suffix.
        # ---------------------------------------------------------

        exact = [0] * (m + 1)
        exact[m] = n

        for j in range(m - 1, -1, -1):
            c = ord(word2[j]) - ord('a')
            p = positions[c]

            # We need an occurrence before exact[j + 1]
            k = bisect_left(p, exact[j + 1]) - 1

            if k >= 0:
                exact[j] = p[k]
            else:
                exact[j] = -1

        # ---------------------------------------------------------
        # almost[j]
        #
        # Largest index from which word2[j:] can be matched with
        # AT MOST one mismatch.
        #
        # almost[m] = n
        # ---------------------------------------------------------

        almost = [0] * (m + 1)
        almost[m] = n

        for j in range(m - 1, -1, -1):

            target = word2[j]
            c = ord(target) - ord('a')

            # Option 1:
            # Match this character exactly.
            # The remaining suffix may still use the mismatch.
            p = positions[c]

            k = bisect_left(p, almost[j + 1]) - 1

            same = -1

            if k >= 0:
                same = p[k]

            # Option 2:
            # Use the mismatch at this position.
            # Therefore the remaining suffix must match exactly.
            different = -1

            limit = exact[j + 1]

            if limit > 0:

                i = limit - 1

                if word1[i] != target:
                    different = i
                else:
                    # Skip the entire run of target characters.
                    different = run_start[i] - 1

            almost[j] = max(same, different)

        # Impossible even with one mismatch
        if almost[0] == -1:
            return []

        # ---------------------------------------------------------
        # GREEDY
        # ---------------------------------------------------------

        ans = []
        prev = -1

        # Has the one mismatch already been used?
        mismatch_used = False

        for j in range(m):

            target = word2[j]
            start = prev + 1

            c = ord(target) - ord('a')
            p = positions[c]

            # -----------------------------------------------------
            # If mismatch is already used:
            #
            # We MUST match exactly from now on.
            # -----------------------------------------------------

            if mismatch_used:

                k = bisect_left(p, start)

                if k >= len(p):
                    return []

                candidate = p[k]

                # Remaining suffix must also be exactly matchable.
                if candidate >= exact[j + 1]:
                    return []

                ans.append(candidate)
                prev = candidate

                continue

            # -----------------------------------------------------
            # Mismatch has NOT been used yet.
            #
            # Candidate 1:
            # Match current character exactly.
            #
            # We can still use one mismatch later.
            # -----------------------------------------------------

            k = bisect_left(p, start)

            same_candidate = -1

            if k < len(p):
                candidate = p[k]

                if candidate < almost[j + 1]:
                    same_candidate = candidate

            # -----------------------------------------------------
            # Candidate 2:
            # Use mismatch NOW.
            #
            # Therefore the rest must match exactly.
            # -----------------------------------------------------

            different_candidate = -1

            limit = exact[j + 1]

            if start < n and start < limit:

                if word1[start] != target:
                    different_candidate = start

                else:
                    # word1[start] == target.
                    # Find the first position after this run
                    # having a different character.
                    candidate = run_end[start] + 1

                    if candidate < n and candidate < limit:
                        different_candidate = candidate

            # -----------------------------------------------------
            # Choose the smallest index.
            # This guarantees lexicographically smallest answer.
            # -----------------------------------------------------

            if same_candidate == -1:
                candidate = different_candidate

            elif different_candidate == -1:
                candidate = same_candidate

            else:
                candidate = min(
                    same_candidate,
                    different_candidate
                )

            if candidate == -1:
                return []

            # If we selected the different-character candidate,
            # the mismatch has now been consumed.
            if candidate == different_candidate:
                mismatch_used = True

            ans.append(candidate)
            prev = candidate

        return ans