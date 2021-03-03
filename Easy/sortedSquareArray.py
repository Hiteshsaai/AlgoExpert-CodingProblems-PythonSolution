class Solution:

    ##SOLUTION 1:
    def sortedSquaredArray1(self, array):

        # Time O(n) || Space O(n)
        if not array:
            return array
        if len(array) == 1:
            return [array[0] ** 2]

        res = [0] * len(array)

        for i in range(0, len(array)):

            res[i] = array[i] ** 2

        res.sort()
        return res

    ##SOLUTION 2:
    def sortedSquaredArray2(self, array):
        # Time O(nlogn) || Space O(1)
        if not array:
            return array

        if len(array) == 1:
            return [array[0] ** 2]

        for idx in range(0, len(array)):  # O(n)
            if array[idx] > 0:
                array[idx] = -array[idx]

        array.sort()  # O(nlogn)

        for idx in range(0, len(array)):

            array[idx] = array[idx] ** 2

        return array[::-1]  # O(n)


if __name__ == "__main__":

    print(Solution().sortedSquaredArray1([1, 2, 3, 5, 6, 8, 9]))
    print(Solution().sortedSquaredArray1([-10, -5, 0, 5, 10]))
