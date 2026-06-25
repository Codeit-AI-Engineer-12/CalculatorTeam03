import unittest

from ops.add import add


class AddValidationTests(unittest.TestCase):
    def test_add_returns_sum_for_natural_numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 4), 4)

    def test_add_rejects_missing_arguments(self):
        with self.assertRaises(ValueError):
            add(2)

        with self.assertRaises(ValueError):
            add()

    def test_add_rejects_invalid_values(self):
        with self.assertRaises(ValueError):
            add(2, -1)

        with self.assertRaises(ValueError):
            add(2.5, 3)

        with self.assertRaises(ValueError):
            add(2, "three")

        with self.assertRaises(ValueError):
            add(2, "   ")

        with self.assertRaises(ValueError):
            add(2, "@")

        with self.assertRaises(ValueError):
            add(True, 3)


if __name__ == "__main__":
    unittest.main()
