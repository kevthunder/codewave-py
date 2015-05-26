import unittest
import textwrap
import re

import codewave_core.util as util
import codewave_core.codewave as codewave
import codewave_core.text_parser as text_parser
import codewave_core.command as command

import test.test_helper as test_helper

class CmdAuthoringTestCase(unittest.TestCase):
	def setUp(self):
		codewave.init()
		command.initCmds()
		self.codewave = codewave.Codewave(text_parser.TextParser('Lorem Ipsum'))
		

	def tearDown(self):
		command.initCmds()

	def test_show_edit_box_for_new_command(self):
		self.codewave.editor.setLang('js')
		test_helper.setEditorContent(self.codewave.editor, '~~e|dit new_cmd~~')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, textwrap.dedent("""
			/* ~~core:edit new_cmd~~~~~ */
			/* ~  ~~help~~            ~ */
			/* ~                      ~ */
			/* ~  ~~/help~~           ~ */
			/* ~  ~~source~~          ~ */
			/* ~  |                    ~ */
			/* ~  ~~/source~~         ~ */
			/* ~  ~~save~~ ~~close~~  ~ */
			/* ~~/core:edit~~~~~~~~~~~~ */
			"""))
			
	def test_save_new_command(self):
		self.assertIsNone(self.codewave.context.getCmd('new_cmd'))
		self.codewave.editor.setLang('js')
		test_helper.setEditorContent(self.codewave.editor, textwrap.dedent("""\
			/* ~~core:edit new_cmd~~~~~ */
			/* ~  ~~help~~            ~ */
			/* ~                      ~ */
			/* ~  ~~/help~~           ~ */
			/* ~  ~~source~~          ~ */
			/* ~  Lorem ipsum         ~ */
			/* ~  ~~/source~~         ~ */
			/* ~  ~~|save~~ ~~close~~  ~ */
			/* ~~/core:edit~~~~~~~~~~~~ */"""))
		self.codewave.onActivationKey()
		self.assertIsNotNone(self.codewave.context.getCmd('new_cmd'))
		test_helper.assertEditorResult(self,self.codewave.editor, '|')
		
	
	def test_new_command_should_expand(self):
		self.codewave.editor.setLang('js')
		test_helper.setEditorContent(self.codewave.editor, textwrap.dedent("""
			/* ~~core:edit new_cmd~~~~~ */
			/* ~  ~~help~~            ~ */
			/* ~                      ~ */
			/* ~  ~~/help~~           ~ */
			/* ~  ~~source~~          ~ */
			/* ~  Lorem ipsum         ~ */
			/* ~  ~~/source~~         ~ */
			/* ~  ~~|save~~ ~~close~~  ~ */
			/* ~~/core:edit~~~~~~~~~~~~ */
			"""))
		self.codewave.onActivationKey()
		test_helper.setEditorContent(self.codewave.editor, """~~new_cmd|~~""")
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, 'Lorem ipsum|')
		
	def test_allow_command_alias(self):
		self.codewave.editor.setLang('js')
		test_helper.setEditorContent(self.codewave.editor, '~~alias hello hello2|~~')
		self.codewave.onActivationKey()
		test_helper.setEditorContent(self.codewave.editor, '~~hello2|~~')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, 'Hello, World!|')
		

		
if __name__ == '__main__':
		unittest.main()