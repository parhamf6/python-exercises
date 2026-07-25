# version 1: brute force / simple approach
# Build a new string containing only alphanumeric characters.
# Convert all characters to lowercase, then compare the string with its reverse.
# Simple and easy to understand, but it uses extra memory to store the cleaned string.
# Time: O(n), Space: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        
        for i in s:
            if i.isalnum():
                st += i.lower()
        
        return st == st[::-1]


# version 2: optimal two pointer approach
# Instead of creating a new string, compare characters directly from both ends.
# Use two pointers:
# - left starts from the beginning.
# - right starts from the end.
# Skip non-alphanumeric characters and compare lowercase characters.
# We scan the string once without using extra memory.
# Time: O(n), Space: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters ignoring case
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
