import unittest
from unittest.mock import patch
from calculator import calculator

class TestCalculator(unittest.TestCase):

    # Penjumlahan
    @patch('builtins.input', side_effect=["1", "5", "3"])
    def test_penjumlahan(self, mock_inputs):
        result = calculator()
        self.assertEqual(result, 8)

    # Pengurangan
    @patch('builtins.input', side_effect=["2", "15", "5"])
    def test_pengurangan(self, mock_inputs):
        result = calculator()
        self.assertEqual(result, 10)

    # Perkalian
    @patch('builtins.input', side_effect=["3", "1", "3"])
    def test_perkalian(self, mock_inputs):
        result = calculator()
        self.assertEqual(result, 1)

    # Pembagian
    @patch('builtins.input', side_effect=["4", "15", "5"])
    def test_pembagian(self, mock_inputs):
        result = calculator()
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()