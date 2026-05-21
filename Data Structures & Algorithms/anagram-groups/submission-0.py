class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for ele in strs:
            sort = ''.join(sorted(ele))
            if sort in hashmap:
                 hashmap[sort].append(ele)
            else:
                hashmap[sort] = [ele]
        return list(hashmap.values())