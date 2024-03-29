""" Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

________________

speed
O(N)
"""


class Solution:

    def reverse(self, x: int) -> int:
        reversed_x = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            reversed_x = reversed_x * 10 + x % 10
            x = x // 10

        reversed_x = reversed_x * sign

        if reversed_x >= 2**31 - 1 or reversed_x <= -2**31:
            return 0

        return reversed_x


print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(120))
