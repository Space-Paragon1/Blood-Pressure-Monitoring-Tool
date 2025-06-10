import unittest
from bp_utils import determine_bp

class TestBloodPressureClassification(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(determine_bp(110, 70), "normal")

    def test_elevated(self):
        self.assertEqual(determine_bp(125, 85), "elevated_blood_pressure")

    def test_hypertensive(self):
        self.assertEqual(determine_bp(145, 95), "hypertensive")

if __name__ == "__main__":
    unittest.main()
