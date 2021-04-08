import unittest
import assesment

 
class TestAssesment(unittest.TestCase):
    def test_parking_floors(self):
        self.assertEqual(assesment.parking_floors(fourth_floor),5)

    def test_parking_floors(self):
        self.assertEqual(assesment.Parking_floors(third_floor),5)

    def test_parking_floors(self):
        self.assertEqual(assesment.parking_floors(second_floor),5)

    def test_parking_floors(self):
        self.assertEqual(assesment.parking_floors(first_floor),5)

    def test_user_options(self):
        result=assesment.choose_option(int)
        self.assertTrue(result,int)
if __name__ == "__main__":
    unittest.main()
