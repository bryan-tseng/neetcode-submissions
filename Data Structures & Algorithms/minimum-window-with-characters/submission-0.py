class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        c_t = Counter(t)
        window = Counter()
        contain_count = 0
        letters_needed = len(c_t)
        start = 0
        best_start = 0
        best_end = 0
        best_length = float("inf")
        for end in range(len(s)):
            character = s[end]
            window[character] += 1
            if character in c_t and window[character] == c_t[character]:
                contain_count += 1
            while contain_count == letters_needed:
                if best_length > end - start + 1:
                    best_start = start
                    best_end = end
                    best_length = end - start + 1
                window[s[start]] -= 1
                if s[start] in c_t and window[s[start]] < c_t[s[start]]:
                    contain_count -= 1
                start += 1
        if best_length == float("inf"):
            return ""
        return s[best_start:best_end + 1]