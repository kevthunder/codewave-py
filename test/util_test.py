import unittest
import textwrap
import re
import codewave_core.util as util
import codewave_core.codewave as codewave
import codewave_core.text_parser as text_parser

import test.test_helper as test_helper

class PhpTestCase(unittest.TestCase):

	
	def test_repeat_string(self):
		self.assertEqual(util.repeat('+-',3), '+-+-+-')
		
	def test_repeat_string_to_length(self):
		self.assertEqual(util.repeatToLength('+-',3), '+-+')
		
	def test_reverse_string(self):
		self.assertEqual(util.reverseStr('abcd'), 'dcba')
		
		
		
if __name__ == '__main__':
		unittest.main()