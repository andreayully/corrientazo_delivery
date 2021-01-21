import unittest
import delivery_routes

expect_ans = [{'drone_id': '01', 'coord': (-2, 4), 'orientation': 'N'},
              {'drone_id': '01', 'coord': (-3, 3), 'orientation': 'S'},
              {'drone_id': '01', 'coord': (-4, 2), 'orientation': 'E'}]


class TestDeliveryRooutes(unittest.TestCase):
    def test_read_order_file(self):
        self.assertEqual(delivery_routes.read_order_file(), expect_ans)



if __name__ == "__main__":
    unittest.main()
