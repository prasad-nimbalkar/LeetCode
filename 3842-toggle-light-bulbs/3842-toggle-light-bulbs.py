class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        seen = []

        for i in bulbs:
            if i in seen:
                seen.remove(i)
            else:
                seen.append(i)
        return sorted(seen)
