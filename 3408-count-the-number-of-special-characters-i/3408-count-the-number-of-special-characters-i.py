class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word)
        count = 0

        for ch in range(ord("a"), ord("z") + 1):
            lower = chr(ch)
            upper = chr(ch - 32)
            if lower in chars and upper in chars:
                count += 1
        return count
