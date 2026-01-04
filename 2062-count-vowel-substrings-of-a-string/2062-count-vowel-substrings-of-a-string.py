class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        last = {v: -1 for v in vowels}

        res = 0
        segment_start = 0

        for r, ch in enumerate(word):
            if ch not in vowels:
                # reset on consonant
                segment_start = r + 1
                for v in vowels:
                    last[v] = -1
                continue

            last[ch] = r

            # check if all vowels are present
            min_last = min(last.values())
            if min_last >= segment_start:
                res += min_last - segment_start + 1

        return res


# Time: O(n)
# Space: O(n)