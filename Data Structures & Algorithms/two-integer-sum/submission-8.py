class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        Maps = {}

        for i, n in enumerate(nums):

            diff = target - n
            if diff in Maps:
                return [Maps[diff],i]

            Maps[n] = i





