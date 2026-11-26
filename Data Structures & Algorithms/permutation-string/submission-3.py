class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        front = 0
        end = len(s1)
        from collections import Counter
        while end <= len(s2):
            c1 = Counter(s1)
            c2 = Counter(s2[front:end])
            if c2 == c1:
                return True
            front += 1
            end += 1
        return False