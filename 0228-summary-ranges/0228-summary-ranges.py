class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res

        strt = nums[0]

        for num in range(1, len(nums) + 1):
            if num == len(nums) or nums[num] != nums[num - 1] + 1:
                end = nums[num - 1]

                if strt == end:
                    res.append(str(strt))
                else:
                    res.append(f"{strt}->{end}")

                if num < len(nums):
                    strt = nums[num]
        return res
