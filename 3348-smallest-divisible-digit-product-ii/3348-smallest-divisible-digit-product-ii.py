# Globally precompute the optimal digit configurations for factors of 2 and 3.
# Max prime counts for t <= 10^14: 2s <= 47, 3s <= 30
MAX_R2 = 47
MAX_R3 = 30
DP = [[None] * (MAX_R3 + 1) for _ in range(MAX_R2 + 1)]
DP[0][0] = ""

def _get_best(s1, s2):
    if s1 is None: return s2
    if s2 is None: return s1
    # We want the shortest string length. 
    # If tied, we want the lexicographically smallest.
    if len(s1) != len(s2):
        return s1 if len(s1) < len(s2) else s2
    return s1 if s1 < s2 else s2

for _r2 in range(MAX_R2 + 1):
    for _r3 in range(MAX_R3 + 1):
        if _r2 == 0 and _r3 == 0:
            continue
        
        _best = None
        # Digits > 1 that contribute to 2s and 3s: 2, 3, 4, 6, 8, 9
        for _d, _d_r2, _d_r3 in [(2, 1, 0), (3, 0, 1), (4, 2, 0), (6, 1, 1), (8, 3, 0), (9, 0, 2)]:
            _pr2 = max(0, _r2 - _d_r2)
            _pr3 = max(0, _r3 - _d_r3)
            
            if DP[_pr2][_pr3] is not None:
                _cand = DP[_pr2][_pr3] + str(_d)
                # Keep combinations strictly sorted to ensure they are lexicographically smallest
                _cand = "".join(sorted(_cand))
                _best = _get_best(_best, _cand)
                
        DP[_r2][_r3] = _best


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Count required prime factors for t
        temp_t = t
        R2 = R3 = R5 = R7 = 0
        while temp_t % 2 == 0: R2 += 1; temp_t //= 2
        while temp_t % 3 == 0: R3 += 1; temp_t //= 3
        while temp_t % 5 == 0: R5 += 1; temp_t //= 5
        while temp_t % 7 == 0: R7 += 1; temp_t //= 7
        
        # If there are leftover prime factors > 7 (like 11, 13), it's impossible to satisfy with digits 1-9
        if temp_t > 1:
            return "-1"
            
        N = len(num)
        
        # Maps digit -> (count of 2s, 3s, 5s, 7s)
        digit_primes = {
            0: (0,0,0,0), 1: (0,0,0,0), 2: (1,0,0,0), 3: (0,1,0,0),
            4: (2,0,0,0), 5: (0,0,1,0), 6: (1,1,0,0), 7: (0,0,0,1),
            8: (3,0,0,0), 9: (0,2,0,0)
        }
        
        # Prefix sum arrays for the prime counts of the digits inside `num`
        pref_c2 = [0] * (N + 1)
        pref_c3 = [0] * (N + 1)
        pref_c5 = [0] * (N + 1)
        pref_c7 = [0] * (N + 1)
        
        for i in range(N):
            d = int(num[i])
            if d == 0:
                break
            p2, p3, p5, p7 = digit_primes[d]
            pref_c2[i+1] = pref_c2[i] + p2
            pref_c3[i+1] = pref_c3[i] + p3
            pref_c5[i+1] = pref_c5[i] + p5
            pref_c7[i+1] = pref_c7[i] + p7
            
        # The shortest combination string we need purely for `t`
        req_str = DP[R2][R3]
        total_req_len = len(req_str) + R5 + R7
        
        # If it takes more digits to satisfy `t` than the length of `num`, 
        # we skip modifying `num` entirely, as we are forced to generate a longer number.
        if total_req_len > N:
            ans_len = total_req_len
            pad = ans_len - total_req_len  # 0
            ans = "1" * pad + req_str + "5" * R5 + "7" * R7
            return "".join(sorted(ans))
            
        first_zero = num.find('0')
        
        # Check if the original string `num` is already valid
        if first_zero == -1:
            if (pref_c2[N] >= R2 and pref_c3[N] >= R3 and 
                pref_c5[N] >= R5 and pref_c7[N] >= R7):
                return num
                
        # Try to modify `num` by keeping a prefix (from longest to shortest) and boosting a digit
        for i in range(N - 1, -1, -1):
            # A prefix cannot contain a '0'
            if first_zero != -1 and i > first_zero:
                continue
                
            # Bump the i-th digit up (meaning this variation strictly makes it > num)
            for d in range(int(num[i]) + 1, 10):
                p2 = pref_c2[i] + digit_primes[d][0]
                p3 = pref_c3[i] + digit_primes[d][1]
                p5 = pref_c5[i] + digit_primes[d][2]
                p7 = pref_c7[i] + digit_primes[d][3]
                
                # Factors we STILL need from the remainder of the available length
                r2 = max(0, R2 - p2)
                r3 = max(0, R3 - p3)
                r5 = max(0, R5 - p5)
                r7 = max(0, R7 - p7)
                
                req = DP[r2][r3]
                req_len = len(req) + r5 + r7
                
                # Can we fit the remaining prime requirements into the space left?
                if req_len <= N - 1 - i:
                    pad = N - 1 - i - req_len
                    # Append 1s as padding, and sort all inserted digits to keep them lexicographically minimal
                    suffix = "1" * pad + req + "5" * r5 + "7" * r7
                    return num[:i] + str(d) + "".join(sorted(suffix))
                    
        # If no modification at the current length `N` is valid, increase the length of the string to N+1
        M = N + 1
        pad = M - total_req_len
        ans = "1" * pad + req_str + "5" * R5 + "7" * R7
        return "".join(sorted(ans))