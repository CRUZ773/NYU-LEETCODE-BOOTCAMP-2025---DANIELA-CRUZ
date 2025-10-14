# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        #reverse = []
        #reverse = s.split()
        #reverse = reverse[::-1]    
        #result = ' '.join(reverse)
        #result = result.lstrip()
        #result = result.rstrip()
        #return result
        
        return ' '.join(s.split()[::-1])