class Solution:
    def compress(self, s: List[str]) -> int:
        i = 0
        write = 0
        n = len(s)
        while i<n:
            ch = s[i]
            count = 0
            while i<n and ch == s[i]:
                count+=1
                i+=1
            s[write] = ch
            write+=1

            if count>1:
                for dig in str(count):
                    s[write]=dig
                    write+=1

        return write