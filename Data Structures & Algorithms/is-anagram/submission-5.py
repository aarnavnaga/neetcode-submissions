class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count1 = {}
        for i in range(0, len(s)):
            a = s[i]
            b = t[i]
            count1[a] = count1.get(a, 0) + 1
            count1[b] = count1.get(b, 0) - 1
        return all(c == 0 for c in count1.values())


        