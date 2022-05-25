import unittest
ALLOWED_MOVES = {
    0: [17, 10],
    1: [16, 18, 11],
    2: [17, 8, 19, 12],
    3: [18, 9, 20, 13],
    4: [19, 10, 21, 14],
    5: [20, 11, 22, 15],
    6: [21, 12, 23],
    7: [22, 13],
    8: [25, 18, 2],
    9: [24, 26, 19, 3],
    10: [25, 16, 0, 27, 20, 4],
    11: [26, 17, 1, 28, 21, 5],
    12: [27, 18, 2, 29, 22, 6],
    13: [28, 19, 3, 30, 23, 7],
    14: [29, 20, 4, 31],
    15: [30, 21, 5],
    16: [33, 1, 26, 10],
    17: [32, 0, 34, 2, 27, 11],
    18: [33, 1, 24, 8, 35, 3, 28, 12],
    19: [34, 2, 25, 9, 36, 4, 29, 13],
    20: [35, 3, 26, 10, 37, 5, 30, 14],
    21: [36, 4, 27, 11, 38, 6, 31, 15],
    22: [37, 5, 28, 12, 39, 7],
    23: [38, 6, 29, 13],
    24: [41, 9, 34, 18],
    25: [40, 8, 42, 10, 35, 19],
    26: [41, 9, 32, 16, 43, 11, 36, 20],
    27: [42, 10, 33, 17, 44, 12, 37, 21],
    28: [43, 11, 34, 18, 45, 13, 38, 22],
    29: [44, 12, 35, 19, 46, 14, 39, 23],
    30: [45, 13, 36, 20, 47, 15],
    31: [46, 14, 37, 21],
    32: [49, 17, 42, 26],
    33: [48, 16, 50, 18, 43, 27],
    34: [49, 17, 40, 24, 51, 19, 44, 28],
    35: [50, 18, 41, 25, 52, 20, 45, 29],
    36: [51, 19, 42, 26, 53, 21, 46, 30],
    37: [52, 20, 43, 27, 54, 22, 47, 31],
    38: [53, 21, 44, 28, 55, 23],
    39: [54, 22, 45, 29],
    40: [57, 25, 50, 34],
    41: [56, 24, 58, 26, 51, 35],
    42: [57, 25, 48, 32, 59, 27, 52, 36],
    43: [58, 26, 49, 33, 60, 28, 53, 37],
    44: [59, 27, 50, 34, 61, 29, 54, 38],
    45: [60, 28, 51, 35, 62, 30, 55, 39],
    46: [61, 29, 52, 36, 63, 31],
    47: [62, 30, 53, 37],
    48: [33, 58, 42],
    49: [32, 34, 59, 43],
    50: [33, 56, 40, 35, 60, 44],
    51: [34, 57, 41, 36, 61, 45],
    52: [35, 58, 42, 37, 62, 46],
    53: [36, 59, 43, 38, 63, 47],
    54: [37, 60, 44, 39],
    55: [38, 61, 45],
    56: [41, 50],
    57: [40, 42, 51],
    58: [41, 48, 43, 52],
    59: [42, 49, 44, 53],
    60: [43, 50, 45, 54],
    61: [44, 51, 46, 55],
    62: [45, 52, 47],
    63: [46, 53],
}


class TestSolution(unittest.TestCase):
    def test_moves(self):
        for i in range(puzzle.BOARD_SIZE ** 2):
            self.assertEqual(
                puzzle.get_moves(i), ALLOWED_MOVES[i], f"Expected {ALLOWED_MOVES[i]}"
            )

    def test_solution(self):
        self.assertEqual(puzzle.solution(0, 10), [0, 10], "Expected [0, 10]")


if __name__ == "__main__":
    unittest.main()