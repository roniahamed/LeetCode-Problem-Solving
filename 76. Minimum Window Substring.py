class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_ln = len(s)
        t_ln = len(t)
        if t_ln > s_ln:
            return ""
        left, right = 0, 0
        min_length = float('inf')
        result = [-1,-1]
        t_count = Counter(t)
        windows = defaultdict(int)
        have, need = 0, len(t_count)

        for right in range(s_ln):
            windows[s[right]] += 1

            if s[right] in t_count and t_count[s[right]] == windows[s[right]]:
                have += 1
            while have == need:
                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    result = [left, right]
                windows[s[left]] -= 1
                if s[left] in t_count and windows[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
        l,r = result
        return s[l:r+1] if min_length != float('inf') else ""
        