class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = []
        for character in s:
            if character.isalnum():
                palindrome.append(character.lower())
        reversed_pal = palindrome.copy()
        reversed_pal.reverse()
        if palindrome == reversed_pal:
            return True
        return False
        