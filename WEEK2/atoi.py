# 8. String to Integer (atoi)


class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.lstrip()
        # Empty String edge case
        if not s:
            return 0
        
        n = len(s)
        i = 0
        sign_type = 1

        if i == n:
            return 0

        if s[i] == '-':
            sign_type = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        convert = 0

        while i < n:
            cur = s[i]
            if not cur.isdigit():
                break
            else:
                convert = convert * 10 + int(cur) #parsing the string into an integer
            i +=1

        convert = convert * sign_type
        if convert > 2**31 - 1:
            return 2**31 - 1
        elif convert <= -2**31:
            return -2**31
        else:
            return convert



