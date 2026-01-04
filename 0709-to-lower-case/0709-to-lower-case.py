class Solution:
    def toLowerCase(self, s: str) -> str:
        res = []

        for ch in s:
            if "A" <= ch <= "Z":
                res.append(chr(ord(ch) + 32))
            else:
                res.append(ch)
        return "".join(res)


# Time: O(n)
# Spece: O(n)
