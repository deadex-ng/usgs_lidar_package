import unittest
import sys 

sys.path.append('../utils')

from file_handler import FileHandler

class TestFileHandler(unittest.TestCase):
    
    def test_set_output_file_name(self):
        file = FileHandler()
        actual = file.set_output_file_name('iowa')
        expected = ('laz/iowa.las','tif/iowa.tif')
        self.assertEqual(actual, expected)
        

        
if __name__ == '__main__':
  unittest.main()