class Solution:
    # @return an integer
    def string_reverse(self, x):
        strx = str(x)
        if strx[0] == "-":
            return int("-" + strx[:0:-1])
        else:
            return int(strx[::-1])
    def int_reverse(self, x):
        tmp = abs(x)
        digit = []
        out = 0


        while tmp / 10 > 0:
            digit.append(tmp % 10)
            tmp = int(tmp/10)
        digit.append(tmp % 10)

        length = len(digit)

        for num in digit:
            length -= 1
            out += num * pow(10, length)

        if x < 0:
            return -out
        else:
            return out


if __name__ == "__main__":
    so = Solution()
    print so.int_reverse(-4656)
