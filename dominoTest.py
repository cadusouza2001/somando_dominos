import unittest

from domino import encontra_soma

class TestDomino(unittest.TestCase):
    def test_in(self):
        self.assertEqual(encontra_soma([[1, 4], [2, 9], [2, 1], [0, 4]]), "10 descartado o dominó 1 2")
        self.assertEqual(encontra_soma([[8, 1], [9, 4]]), "impossível")
        self.assertEqual(encontra_soma([[6, 3], [1, 2], [3, 1]]), "8 nenhum dominó descartado")
    def test_in1(self):
        self.assertEqual(encontra_soma([[11, 8], [5, 2], [3, 4], [1, 2]]), "18 nenhum dominó descartado")
    def test_in2(self):
        self.assertEqual(encontra_soma([[8, 16], [7, 14], [6, 12], [5, 10], [4, 8]]), "45 nenhum dominó descartado")
    # def test_in3(self):
    #     self.assertEqual(encontra_soma([[272, 46], [16, 66], [302, 803], [824, 880], [767, 995], [53, 808], [462, 268], [63, 441], [546, 852], [94, 847], [806, 496], [57, 486], [47, 436], [636, 732], [222, 582], [428, 270], [810, 558], [347, 225], [294, 202], [401, 786], [880, 55], [657, 390], [120, 333], [201, 772], [744, 788], [655, 457], [680, 640], [339, 447], [846, 23], [663, 717], [172, 713], [220, 237], [944, 750], [969, 401], [338, 663], [559, 457], [147, 434]]), "17592 descartado o dominó 120 333")


if __name__ == '__main__':
    unittest.main()