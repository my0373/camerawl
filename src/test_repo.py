from camerawl.repo import ImageRepo, ImagePath
import unittest

class TestImagePath(unittest.TestCase):
    def test_constructor(self):
        test_file_path = "/tmp"
        ip = ImagePath(test_file_path)
        result = ip.scan()
        print(result)
        self.assertIs(type(result),tuple)


if __name__ == '__main__':
    unittest.main()
