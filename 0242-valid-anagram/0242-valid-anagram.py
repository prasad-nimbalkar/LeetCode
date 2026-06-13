class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq1, freq2 = {}, {}
        for ch1, ch2 in zip(s, t):
            freq1[ch1] = freq1.get(ch1, 0) + 1
            freq2[ch2] = freq2.get(ch2, 0) + 1

        if freq1 == freq2:
            return True
        return False
