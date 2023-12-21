class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_set = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in chars_set:
                chars_set.remove(s[l])
                l += 1
            chars_set.add(s[r])
            res = max(res, r - l + 1)
        return res

# Runtime 76 ms Beats 26.11% Memory 14 MB Beats 100%
