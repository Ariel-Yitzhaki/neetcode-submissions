class Solution:
    def isPalindrome(self, s: str) -> bool:
        ind1, ind2 = 0, len(s) - 1
        s = s.lower()
        while ind1 < ind2:
            if s[ind1].isalnum() and (not s[ind2].isalnum()):
                ind2 -= 1
            elif (not s[ind1].isalnum()) and s[ind2].isalnum():
                ind1 += 1
            elif s[ind1].isalnum() and s[ind2].isalnum():
                if s[ind1] != s[ind2]:
                    return False
                else:
                    ind1 += 1
                    ind2 -= 1
            else:
                ind1 += 1
                ind2 -= 1
        return True