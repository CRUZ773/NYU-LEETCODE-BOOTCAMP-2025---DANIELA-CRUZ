# 438. Find All Anagrams in a String


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ana = {}
        n1 = len(s)
        n2 = len(p)
        p_count = Counter(p)
        s_count = Counter(s[:n2-1])
        i = 0
        substring_list = []

        if n1 < n2:
            return []
        
        for i in range(n2 - 1, n1):
            # add new character in window
            s_count[s[i]] += 1

            # save start index
            if s_count == p_count:
                substring_list.append(i - n2 + 1)

            
            left_char = s[i - n2 + 1]
            s_count[left_char] -= 1
            if s_count[left_char] == 0:
                del s_count[left_char] 

        return substring_list


