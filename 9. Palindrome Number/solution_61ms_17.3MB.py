class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)

        # Compare the string with its reverse (python inbuilt method, to check speed)
        return str_x == str_x[::-1]
    
# Runtime 61 ms Beats 55.17% Memory 17.3 MB Beats 24.98%
