class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        keys = []

        for word in strs:
            key = "".join(sorted(word))
            found = False

            for i in range(len(keys)):
                if keys[i] == key:
                    groups[i].append(word)
                    found = True
                    break

            if not found:
                keys.append(key)
                groups.append([word])

        return groups
        