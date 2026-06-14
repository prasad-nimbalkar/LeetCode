class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch_set = set()
        count = 0
        max_len = 0

        for ch in range(len(s)):
            while s[ch] in ch_set:
                ch_set.remove(s[count])
                count += 1
            ch_set.add(s[ch])
            max_len = max(max_len, ch - count + 1)
        return max_len
