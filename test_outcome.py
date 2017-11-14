# write test_ and what you're testing
import unittest
import outcome


def add(x, y):
    return x + y


class Testadd(unittest.TestCase):
    def test(self):
        self.assertEqual(add(1, 3), 3)


if __name__ == '__main__':
    unittest.main()
