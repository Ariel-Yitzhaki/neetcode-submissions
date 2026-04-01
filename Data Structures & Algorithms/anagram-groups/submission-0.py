class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = defaultdict(list)

        for s in strs:
            c = [0] * 26
            for i in range(len(s)):
                c[ord(s[i]) - ord('a')] += 1
            arr[tuple(c)].append(s)
        return list(arr.values())
