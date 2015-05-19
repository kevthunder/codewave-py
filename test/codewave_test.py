import unittest

import codewave_core.codewave as codewave
import codewave_core.text_parser as text_parser

class DefaultWidgetSizeTestCase(unittest.TestCase):
	def setUp(self):
		self.codewave = codewave.Codewave(text_parser.TextParser('Lorem Ipsum'))
	def runTest(self):
		self.assertEqual(self.codewave.brakets, '~~')
		
		
if __name__ == '__main__':
    unittest.main()