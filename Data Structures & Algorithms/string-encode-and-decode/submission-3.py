class Solution:

    def encode(self, strs: List[str]) -> str:
        s = []
        for string in strs:
            s.append(str(len(string)) + '#' + string)
        return "".join(s)
    def decode(self, s: str) -> List[str]:
        res = []
        i, flag = 0, 1
        length = 0
        while i < len(s):
            if s[i] == '#':
                i += 1
                res.append(s[i:i + length])
                i += length
                length = 0
                flag = 1
            else:
                length = length * 10 + int(s[i])
                i += 1       
        return res
            