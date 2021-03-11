from darn.local import run,ls
import unittest

class TestRun(unittest.TestCase):
    def test_run(self):
        with self.assertRaises(TypeError):
            run()


