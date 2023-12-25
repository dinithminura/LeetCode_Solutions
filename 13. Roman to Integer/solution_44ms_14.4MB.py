values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

class Solution:
    def isSubstractionUse(self, p1: str, p2: str) -> bool:
        if p1 == "I" and (p2 == "V" or p2 == "X"):
            return True
        elif p1 == "X" and (p2 == "L" or p2 == "C"):
            return True
        elif p1 == "C" and (p2 == "D" or p2 == "M"):
            return True
        else:
            return False

    def romanToInt(self, s: str) -> int:
        p = 0
        value = 0
        while p < len(s):
            if (p + 1) == len(s):
                value += values[s[p]]
                p += 1
            else:
                if self.isSubstractionUse(s[p], s[p + 1]):
                    value += values[s[p + 1]] - values[s[p]]
                    p += 2
                else:
                    value += values[s[p]]
                    p += 1

        return value


# Runtime 44 ms Beats 88.14% Memory 14.4 MB Beats 100%
