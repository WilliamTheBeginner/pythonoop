# write test_ and what you're testing
import unittest
from outcome import Outcome


class TestOutcome(unittest.TestCase):

    def test(self):
        oc1 = Outcome('Red', 1)
        oc2 = Outcome('Red', 1)

        self.assertEqual(oc1.__hash__(), oc2.__hash__())


if __name__ == '__main__':
    unittest.main()
