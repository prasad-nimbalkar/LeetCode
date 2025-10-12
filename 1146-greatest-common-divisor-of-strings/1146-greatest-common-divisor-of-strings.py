class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def find_gcd(a, b):
            while b != 0:
                # a, b = b, a % b # without temp variable
                temp = a %  b
                a = b
                b = temp
            return a

        if str1 + str2 != str2 + str1:
            return ""

        gcd_len = find_gcd(len(str1), len(str2))
        return str1[:gcd_len]

'''     # using recursion
        def find_gcd(a, b):
            if b == 0:
                return a
            return find_gcd(b, a % b)
'''