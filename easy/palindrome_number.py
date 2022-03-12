class Solution(object):
    def isPalindrome(self, x):
        """
        Check if an integer is a palindrome - it reads the same backward as forward
        :type x: int
        :rtype: bool
        """
        x=str(x)
        if x[::] == x[::-1]:
            return True
        
        return False
    