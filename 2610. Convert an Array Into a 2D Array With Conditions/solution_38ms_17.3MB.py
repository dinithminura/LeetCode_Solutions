class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = {}
        ans = []

        for val in nums:
            if freq.get(val, 0) >= len(ans):
                ans.append([])

            ans[freq.get(val, 0)].append(val)
            freq[val] = freq.get(val, 0) + 1

        return ans
#  Runtime 38 ms Beats 100% Memory 17.3 MB Beats 20.19%
