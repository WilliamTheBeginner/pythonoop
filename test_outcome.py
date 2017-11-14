# write test_ and what you're testing
import unittest
from outcome import Outcome


class TestOutcome(unittest.TestCase):

    def test(self):
        oc1 = Outcome('1', 35)
        oc2 = Outcome('1', 17)

        self.assertEqual(oc1, oc2)


if __name__ == '__main__':
    unittest.main()
