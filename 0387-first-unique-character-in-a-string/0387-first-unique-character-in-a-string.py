class Solution:
    def firstUniqChar(self, s: str) -> int:
        s = s.lower()
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        for idx, ch in enumerate(s):
            if freq[ch] == 1:
                return idx
        return -1
