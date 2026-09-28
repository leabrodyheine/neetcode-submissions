class Solution:
    def isPalindrome(self, s: str) -> bool:
        sLower = s.lower()
        cleanS = "".join(char for char in sLower if char.isalnum())

        l, r = 0, len(cleanS) - 1

        while l < r:
            if cleanS[l] == cleanS[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
