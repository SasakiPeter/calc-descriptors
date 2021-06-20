import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  # NOQA
from logger import setup_logger
from utils.load import load_sdf


class Test(unittest.TestCase):
    def setUp(self):
        # self.sdf_file = 'data/base-3D.sdf'
        self.logger = setup_logger(__name__)

    def test_sdf(self):
        # expected = 'hoge'
        # actual = load_sdf(self.sdf_file)
        # self.logger.info(actual.shape)
        # self.logger.info(actual.columns)
        # self.assertEqual(expected, actual)
        pass

    def tearDown(self):
        # del self.sdf_file
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
