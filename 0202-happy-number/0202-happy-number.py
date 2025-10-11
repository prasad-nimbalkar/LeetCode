class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_of_squares(n):
            res = 0

            while n:
                res += (n % 10) ** 2
                n = n // 10
            return res

        slow, fast = n, sum_of_squares(n)
        while slow != fast:
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))
        
        return True if slow == 1 else False
