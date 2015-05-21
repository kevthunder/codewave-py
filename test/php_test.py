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
		self.codewave = codewave.Codewave(text_parser.TextParser('Lorem Ipsum'))
		
	def test_create_php_tag(self):
		self.codewave.editor.setLang('php')
		test_helper.setEditorContent(self.codewave.editor, '~~php|~~')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, textwrap.dedent("""\
			<?php
			  |
			?>"""))
			
	def test_expand_if(self):
		self.codewave.editor.setLang('php')
		test_helper.setEditorContent(self.codewave.editor, textwrap.dedent("""\
			<?php 
			~~if|~~
			?>"""))
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, '<?php \nif(|){\n  \n}\n?>')
				 
	# def test_add_php_tags_to_executable_code(self):
		# self.codewave.editor.setLang('php')
		# test_helper.setEditorContent(self.codewave.editor, '~~if|~~')
		# self.codewave.onActivationKey()
		# test_helper.assertEditorResult(self,self.codewave.editor, textwrap.dedent("""\
			# <?php if(|){ ?>
				
				
				
			# <?php } ?>"""))
				 
	# def test_add_no_inner_php_tags_to_functions(self):
		# self.codewave.editor.setLang('php')
		# test_helper.setEditorContent(self.codewave.editor, '~~f|~~')
		# self.codewave.onActivationKey()
		# test_helper.assertEditorResult(self,self.codewave.editor, textwrap.dedent("""\
			# <?php
				# function |() {
					
				# }
			# ?>"""))
			
	# def test_add_php_tag_to_boxes(self):
		# self.codewave.editor.setLang('php')
		# test_helper.setEditorContent(self.codewave.editor, '~~box|~~ Lorem Ipsum ~~close~~ ~~/box~~')
		# self.codewave.onActivationKey()
		# test_helper.assertEditorResult(self,self.codewave.editor, textwrap.dedent("""\
			# <?php
			# /* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
			# /* ~   Lorem Ipsum ~~close~~   ~ */
			# /* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
			# ?>|"""))
				 
	# def test_remove_php_tag_when_closing_box(self):
		# self.codewave.editor.setLang('php')
		# test_helper.setEditorContent(self.codewave.editor, textwrap.dedent("""\
			# <?php
			# /* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
			# /* ~   Lorem Ipsum ~~close|~~   ~ */
			# /* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
			# ?>"""))
		# self.codewave.onActivationKey()
		# test_helper.assertEditorResult(self,self.codewave.editor, '|')
		
		
		
if __name__ == '__main__':
		unittest.main()