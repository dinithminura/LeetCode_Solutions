class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        lp = 0
        rp = len(string) - 1

        while lp <= rp:
            if string[lp] == string[rp]:
                lp += 1
                rp -= 1
            else:
                return False
        return True

# Runtime 72 ms Beats 17.48% Memory 14.3 MB Beats 100%
