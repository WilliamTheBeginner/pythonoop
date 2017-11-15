# write test_ and what you're testing
import unittest
from outcome import Outcome


class TestOutcome(unittest.TestCase):

    def test(self):
        oc1 = Outcome('1', 35)
        oc2 = Outcome('1', 17)
        oc3 = Outcome('2', 2)

        self.assertEqual(oc1, oc2)
        self.assertEqual(oc1.__hash__(), oc2.__hash__())
        self.assertEqual(oc3.winAmount(50), 100)


if __name__ == '__main__':
    unittest.main()
