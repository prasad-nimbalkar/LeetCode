class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        duplicates = 0

        for num in nums:
            if num in seen:
                duplicates = num
            else:
                seen.add(num)
        return duplicates
