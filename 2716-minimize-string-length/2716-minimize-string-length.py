class Solution:
    def minimizedStringLength(self, s: str) -> int:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        return len(freq)
