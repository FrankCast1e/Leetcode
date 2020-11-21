class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums)-1
        while left < right:
            medium = (left+right)//2
            count = 0
            for n in nums:
                if 