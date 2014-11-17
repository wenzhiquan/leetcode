__author__ = 'Administrator'


# class Solution:
#     # @param A  a list of integers
#     # @param m  an integer, length of A
#     # @param B  a list of integers
#     # @param n  an integer, length of B
#     # @return nothing
#     def merge(self, A, m, B, n):
#
#         merged = []
#         numA = 0
#         numB = 0
#
#         while numA < m and numB < n:
#             if A[numA] <= B[numB]:
#                 merged.append(A[numA])
#                 numA += 1
#             else:
#                 merged.append(B[numB])
#                 numB += 1
#
#         if numA < m:
#             for i in range(numA, m):
#                 merged.append(A[i])
#         if numB < n:
#             for i in range(numB, n):
#                 merged.append(B[i])
#
#         A = merged
#
#         return A

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        # startIndex = 0
        #
        # for num in B:
        #     if m == 0:
        #         A.insert(m, num)
        #         m += 1
        #         continue
        #     for i in range(startIndex, m):
        #         if A[i] > num:
        #             A.insert(i, num)
        #             m += 1
        #             startIndex = i
        #             break
        #         elif i == m-1:
        #             A.insert(m, num)
        #             m += 1
        i = m - 1
        j = n - 1
        k = m + n - 1

        for num in range(m, m+n):
            A.insert(num, 0)

        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[k] = A[i]
                k -= 1
                i -= 1
            else:
                A[k] = B[j]
                k -= 1
                j -= 1
        while j >= 0:
            A[k] = B[j]
            k -= 1
            j -= 1

        return A


if __name__ == "__main__":
    so = Solution()
    print so.merge([-1,0,0,3,3,3], 6, [1,2,2], 3)