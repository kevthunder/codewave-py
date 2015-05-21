import unittest
import textwrap
import re
import test.test_helper as test_helper

import codewave_core.util as util
import codewave_core.codewave as codewave
import codewave_core.text_parser as text_parser

class PhpTestCase(unittest.TestCase):
	def setUp(self):
		codewave.init()
		self.replacement = None
		self.editor = None
		
	# def test_editor_should_be_settable(self):
		# self.editor = text_parser.TextParser('lorem Ipsum')
		# self.replacement = util.Replacement(1,2,'a')
		# self.replacement.withEditor(self.editor)
		# self.assertEqual(self.replacement.editor(), self.editor)
		
	# def test_take_prefix_option(self):
		# self.editor = text_parser.TextParser('lorem Ipsum')
		# self.replacement = util.Replacement(1,2,'a',{'prefix':'test'}).withEditor(self.editor)
		# self.assertEqual(self.replacement.prefix, 'test')
		
	# def test_editor_should_be_settable(self):
		# self.editor = text_parser.TextParser('lorem Ipsum')
		# self.replacement = util.Wrapping(0,5,'(',')')
		# self.replacement.withEditor(self.editor)
		# self.assertEqual(self.replacement.editor(), self.editor)
		
		
		
		
		
if __name__ == '__main__':
		unittest.main()