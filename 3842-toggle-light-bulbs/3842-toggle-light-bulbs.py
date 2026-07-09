class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        seen = set()

        for i in bulbs:
            if i in seen:
                seen.remove(i)
            else:
                seen.add(i)
        return sorted(seen)
