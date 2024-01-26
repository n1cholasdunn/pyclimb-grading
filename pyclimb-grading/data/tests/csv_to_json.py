import unittest
from ..csv_to_json import get_data, Boulder, Ice, Route, Aid


class TestGradeTables(unittest.TestCase):
    def setUp(self):
        self.data_dir = "../data"
        self.boulder_data = get_data(
            f"{self.data_dir}/boulder.csv", "", Boulder)
        self.route_data = get_data(f"{self.data_dir}/routes.csv", "", Route)
        self.ice_data = get_data(f"{self.data_dir}/ice.csv", "", Ice)
        self.aid_data = get_data(f"{self.data_dir}/aid.csv", "", Aid)

    def test_tables_are_lists(self):
        for table in [self.boulder_data, self.route_data, self.ice_data, self.aid_data]:
            self.assertIsInstance(table, list)
            self.assertGreater(len(table), 1)

    def test_tables_score_is_int(self):
        for table in [self.boulder_data, self.route_data, self.ice_data, self.aid_data]:
            first_row = table[0]
            self.assertIsInstance(first_row.score, int)


if __name__ == "__main__":
    unittest.main()
