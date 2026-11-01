class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = ["".join(sorted(word)) for word in strs]
        indices = {}
        for i in range(len(sorted_strs)):
            word = sorted_strs[i]
            if word in indices:
                indices[word].append(i)
            else:
                indices[word] = [i]

        out = []
        for values in indices.values():
            out.append([strs[i] for i in values])
        return out