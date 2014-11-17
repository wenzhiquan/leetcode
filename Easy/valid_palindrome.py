__author__ = 'Administrator'


class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s == "":
            return True
        else:
            start = 0
            end = len(s) - 1

            while start < end:

                while not s[start].isalnum() and start < end:
                    start += 1
                while not s[end].isalnum() and start < end:
                    end -= 1
                if s[start].lower() != s[end].lower():
                    return False
                else:
                    start += 1
                    end -= 1
            return True



if __name__ == "__main__":
    so = Solution()
    print so.isPalindrome(",.,.,.,.,.,.,.,.,")