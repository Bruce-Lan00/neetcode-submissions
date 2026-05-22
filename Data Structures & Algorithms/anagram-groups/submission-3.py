class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # my sort solution
        """hashmap = {}
        for ele in strs:
            sort = ''.join(sorted(ele))
            if sort in hashmap:
                 hashmap[sort].append(ele)
            else:
                hashmap[sort] = [ele]
        return list(hashmap.values())"""

        # count solution
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())