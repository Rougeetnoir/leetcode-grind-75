class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 模式：双指针同向（不同数组）
        # s指针慢 A slow pointer i scans s, Advance i only when characters match; If i reaches the end of s, then s is a subsequence of t.
        # t指针快 A fast pointer j scans t, Always advance j

        i = 0
        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1
        return i == len(s)