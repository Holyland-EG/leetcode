class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n >= 1000:
            n = list(str(n))
            i = -3
            while abs(i) < len(n):
                n[i:i] = '.'
                i -= 4
            return ''.join(n)
        return str(n)