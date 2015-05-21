import unittest
import textwrap
import re
import test.test_helper as test_helper

import codewave_core.util as util
import codewave_core.codewave as codewave
import codewave_core.text_parser as text_parser

class EditorTestCase(unittest.TestCase):
	def setUp(self):
		codewave.init()
		self.codewave = codewave.Codewave(text_parser.TextParser('Lorem Ipsum'))


	def test_set_cursor_pos(self):
		self.codewave.editor.text = 'lorem'
		self.codewave.editor.setCursorPos(2)
		self.assertEqual(self.codewave.editor.getCursorPos().raw(), [2,2])
		
		
		
if __name__ == '__main__':
		unittest.main()