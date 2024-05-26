class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]


result = Solution().isPalindrome(121)
print(result)
