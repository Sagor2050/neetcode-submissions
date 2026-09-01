class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for s in strs:
            chars = sorted(s)
            key = "".join(chars)

            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        result = [] 
        for key in groups:
            result.append(groups[key])
        return result 