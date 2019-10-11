'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Could you solve it without converting the integer to a string?
'''
def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_int = 0

        n = x
        while n > reversed_int:
            rem = n % 10
            reversed_int *= 10
            reversed_int += rem
            n = n // 10

        print(reversed_int,n)
        return reversed_int == n or reversed_int//10 == n
