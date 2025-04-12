import unittest
;Реализовать merge sort написать к функции unit-тесты 

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


class Test_merge_sort(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_sorted_array(self):
        self.assertEqual(merge_sort([2, -3, 4, 1, 3]), [-3, 1, 2, 3, 4])

    def test_reverse_array(self):
        self.assertEqual(merge_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_duplicates(self):
        self.assertEqual(merge_sort([4, 3, 2, 1, 4, 4, 3, 4, 3, 4, 2, 1]),
                         [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4])

    def test_half_sorted1(self):
        self.assertEqual(merge_sort([1, 2, 3, 6, 5, 4]), [1, 2, 3, 4, 5, 6])

    def test_half_sorted2(self):
        self.assertEqual(merge_sort([3, 2, 1, 4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_merge(self):
        self.assertEqual(merge([1, 4, 6], [2, 3, 5]), [1, 2, 3, 4, 5, 6])

    def test_merge_empty(self):
        self.assertEqual(merge([], []), [])

    def test_merge_one_empty(self):
        self.assertEqual(merge([], [1, 2]), [1, 2])

    def test_merge_duplicate(self):
        self.assertEqual(merge([1, 2, 3], [1, 2, 3]), [1, 1, 2, 2, 3, 3])

    def test_merge_reverse(self):
        self.assertEqual(merge([3, 2, 1], [4, 5, 6]), [3, 2, 1, 4, 5, 6])

    def test_merge_negative(self):
        self.assertEqual(merge([-1, 2, -3], [-4, 1, -2]),
                         [-4, -1, 1, -2, 2, -3])

    def test_different_len_merge(self):
        self.assertEqual(merge([1, 2, 3], [1, 2, 3, 3, 3, 2]),
                         [1, 1, 2, 2, 3, 3, 3, 3, 2])


if __name__ == "__main__":
    unittest.main()
