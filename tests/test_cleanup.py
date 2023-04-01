import os
import unittest

from cleanup.cleanup import remove_links

class TestRemoveLinks(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_file.md'
        with open(self.test_file, 'w') as f:
            f.write('---\naliases: blog\ntags: blog\n---\n\nThis should [[Link|stay]].')

    def tearDown(self):
        os.remove(self.test_file)

    def test_remove_links(self):
        remove_links(self.test_file)
        with open(self.test_file, 'r') as f:
            content = f.read()
        self.assertEqual(content, '---\naliases: blog\ntags: blog\n---\nThis should stay.\n')

if __name__ == '__main__':
    unittest.main()
