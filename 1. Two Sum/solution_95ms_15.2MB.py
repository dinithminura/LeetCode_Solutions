class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(len(nums)):
            numDict[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numDict and numDict[diff] != i:
                return [numDict[diff], i]


# Runtime 95 ms Beats 41.78% Memory 15.2 MB Beats 100%
