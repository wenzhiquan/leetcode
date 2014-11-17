__author__ = 'Administrator'


class Solution:
    # @return a list of lists of integers
    def getRow(self, rowIndex):
        return self.generate(rowIndex+1)[rowIndex]

    def generate(self, numRows):

        pascal_triangle = []

        if numRows > 0:
            pascal_triangle.append([1])

            last_array = []
            for num in range(1, numRows):
                tmp_array = []
                for line in range(num + 1):
                    if line == 0:
                        tmp_array.append(1)
                    elif line == num:
                        tmp_array.append(1)
                        pascal_triangle.append(tmp_array)
                        last_array = tmp_array
                        break
                    else:
                        tmp_array.append(last_array[line-1] + last_array[line])

        return pascal_triangle

if __name__ == "__main__":
    so = Solution()
    print so.getRow(3)