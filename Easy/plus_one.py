__author__ = 'Administrator'

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        length = len(digits)

        while length > 0:
            length -= 1
            digits[length] += 1
            if digits[length] == 10:
                digits[length] = 0
            else:
                break

        if digits[0] == 0:
            digits.insert(0, 1)

        return digits


if __name__ == "__main__":
    so = Solution()
    print so.plusOne([9,9,9,9,9,9,9])