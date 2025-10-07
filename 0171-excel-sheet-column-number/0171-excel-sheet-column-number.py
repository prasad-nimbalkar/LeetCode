class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for T in range(len(columnTitle)):
            res = res * 26
            res = res + ord(columnTitle[T]) - ord("A") + 1
        return res
