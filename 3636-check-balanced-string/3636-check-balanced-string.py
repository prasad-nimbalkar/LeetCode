class Solution:
    def isBalanced(self, num: str) -> bool:
        e_sum, o_sum = 0, 0

        for i in range(len(num)):
            if i % 2 == 0:
                e_sum += int(num[i])
            else:
                o_sum += int(num[i])
        return e_sum == o_sum

        # for i, digit in enumerate(num):
        #     if i % 2 == 0:
        #         e_sum += int(digit)
        #     else:
        #         o_sum += int(digit)
        # return e_sum == o_sum
