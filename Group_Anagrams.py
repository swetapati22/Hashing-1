"""
# Time Complexity :
- O(N * K log K), where N is the number of strings and K is the maximum length of a string.
  Sorting each string takes O(K log K), and we do this for N strings.

# Space Complexity :
- O(N * K), for storing the grouped anagrams in a hashmap.

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            anagram_map[key].append(word)

        return list(anagram_map.values())
