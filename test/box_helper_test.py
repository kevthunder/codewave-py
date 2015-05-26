import unittest
import textwrap
import re

import codewave_core.util as util
import codewave_core.codewave as codewave
import codewave_core.text_parser as text_parser
import codewave_core.box_helper as box_helper

import test.test_helper as test_helper

class BoxHelperTestCase(unittest.TestCase):
	def setUp(self):
		codewave.init()
		self.codewave = codewave.Codewave(text_parser.TextParser('Lorem Ipsum'))
		
	def test_detect_depth(self):
		text,sels = test_helper.extractSelections(textwrap.dedent("""\
			Lorem ipsum dolor
			<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
			<!-- ~  |Lorem ipsum dolor                     ~ -->
			<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
			Lorem ipsum dolor"""))
		self.codewave.editor.text = text
		self.boxHelper = box_helper.BoxHelper(self.codewave.context)
		self.assertEqual(self.boxHelper.getNestedLvl(sels[0].start),1)
		
	def test_detect_box_position(self):
		text,sels = test_helper.extractSelections(textwrap.dedent("""\
			Lorem ipsum dolor
			|<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
			<!-- ~  |Lorem ipsum dolor                     ~ -->
			<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->|
			Lorem ipsum dolor"""))
		self.codewave.editor.text = text
		self.boxHelper = box_helper.BoxHelper(self.codewave.context)
		self.assertIsNotNone(self.boxHelper.getBoxForPos(sels[1]))
		self.assertEqual(self.boxHelper.getBoxForPos(sels[1]).raw(), [sels[0].start,sels[2].start])
		
	def test_detect_box_position_when_nested(self):
		text,sels = test_helper.extractSelections(textwrap.dedent("""\
			Lorem ipsum dolor
			<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
			<!-- ~  |<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~ -->    ~ -->
			<!-- ~  <!-- ~  |Lorem ipsum dolor    ~ -->    ~ -->
			<!-- ~  <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~ -->|    ~ -->
			<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
			Lorem ipsum dolor"""))
		self.codewave.editor.text = text
		self.boxHelper = box_helper.BoxHelper(self.codewave.context)
		self.assertIsNotNone(self.boxHelper.getBoxForPos(sels[1]))
		self.assertEqual(self.boxHelper.getBoxForPos(sels[1]).raw(), [sels[0].start,sels[2].start])
		
	def test_detect_box_width(self):
		self.boxHelper = box_helper.BoxHelper(self.codewave.context)
		self.boxHelper.getOptFromLine('<!-- ~  123456789  ~ -->',False)
		self.assertEqual(self.boxHelper.width, 9)
		
	def test_detect_nested_box_outer_width(self):
		self.boxHelper = box_helper.BoxHelper(self.codewave.context)
		self.boxHelper.getOptFromLine('<!-- ~  <!-- ~  123456789  ~ -->  ~ -->',False)
		self.assertEqual(self.boxHelper.width, 24)
		
		
if __name__ == '__main__':
		unittest.main()