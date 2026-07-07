class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while i < len(min(strs, key=len)):
            if len(set([x[i] for x in strs])) != 1:
                break
            i += 1
        return "".join(strs[0][:i])