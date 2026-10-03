class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen = set()
        maxLen = 0
        currLen = 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                currLen += 1
                maxLen = max(maxLen, currLen)
                r += 1
            else:
                seen.remove(s[l])
                l += 1
                currLen -= 1
        return maxLen

