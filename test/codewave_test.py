import unittest
import textwrap
import re
import test.test_helper as test_helper

import codewave_core.util as util
import codewave_core.codewave as codewave
import codewave_core.text_parser as text_parser

class CodewaveTestCase(unittest.TestCase):
	def setUp(self):
		codewave.init()
		self.codewave = codewave.Codewave(text_parser.TextParser('Lorem Ipsum'))
		
	def test_brakets(self):
		self.assertEqual(self.codewave.brakets, '~~')
		
	def test_create_brakets(self):
		test_helper.setEditorContent(self.codewave.editor, 'lo|rem')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, 'lo~~|~~rem')
		
	def test_create_brakets_begining(self):
		test_helper.setEditorContent(self.codewave.editor, '|lorem')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~lorem')
		
	def test_wrap_selection(self):
		test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~\nlorem ipsum\n~~/~~')
		
	def test_create_brakets_end(self):
		test_helper.setEditorContent(self.codewave.editor, 'lorem|')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, 'lorem~~|~~')
		
	def test_reduce_brakets(self):
		test_helper.setEditorContent(self.codewave.editor, 'lorem~~|~~ipsum')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, 'lorem|ipsum')
		
	def test_reduce_brakets_begining(self):
		test_helper.setEditorContent(self.codewave.editor, '~~|~~lorem')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, '|lorem')
		
	def test_expand_hello(self):
		test_helper.setEditorContent(self.codewave.editor, '- ~~|hello~~')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, '- Hello, World!|')
		
	def test_expand_hello_cursor_middle(self):
		test_helper.setEditorContent(self.codewave.editor, '- ~~hel|lo~~')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, '- Hello, World!|')
		
	def test_expand_hello_cursor_end(self):
		test_helper.setEditorContent(self.codewave.editor, '- ~~hello|~~')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, '- Hello, World!|')
		
	def test_expand_hello_cursor_middle_end_bracket(self):
		test_helper.setEditorContent(self.codewave.editor, '- ~~hello~|~')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, '- Hello, World!|')
		
	def test_expand_hello_cursor_after(self):
		test_helper.setEditorContent(self.codewave.editor, '- ~~hello~~|')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, '- Hello, World!|')
		
	def test_expand_hello_begining(self):
		test_helper.setEditorContent(self.codewave.editor, '~~|hello~~')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, 'Hello, World!|')
		
	def test_expand_closing_tag(self):
		test_helper.setEditorContent(self.codewave.editor, '- ~~hello~~ ~~/hello|~~')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, '- Hello, World!|')
		
	def test_non_exiting_commands_should_not_change(self):
		test_helper.setEditorContent(self.codewave.editor, '- ~~non_exiting_command|~~')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, '- ~~non_exiting_command|~~')
		
	def test_escaped_commands_should_unescape(self):
		test_helper.setEditorContent(self.codewave.editor, '~~!hello|~~')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, '~~hello~~|')
		
	def test_create_box(self):
		test_helper.setEditorContent(self.codewave.editor, '~~box|~~ Lorem Ipsum ~~close~~ ~~/box~~')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, textwrap.dedent("""\
			<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
			<!-- ~   Lorem Ipsum ~~close~~   ~ -->
			<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->|"""))
			
	# def test__boxes_should_use_different_comment_style(self):
		# self.codewave.editor.setLang('js')
		# test_helper.setEditorContent(self.codewave.editor, '~~box|~~ Lorem Ipsum ~~close~~ ~~/box~~')
		# self.codewave.onActivationKey()
		# test_helper.assertEditorResult(self,self.codewave.editor, textwrap.dedent("""\
			# /* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
			# /* ~   Lorem Ipsum ~~close~~   ~ */
			# /* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */|"""))
		
	def test_close_box(self):
		self.codewave.editor.setLang('html')
		test_helper.setEditorContent(self.codewave.editor, textwrap.dedent("""\
			<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
			<!-- ~   Lorem Ipsum ~~close|~~   ~ -->
			<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->"""))
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, '|')
		
	def test_create_nested_box(self):
		self.codewave.editor.setLang('html')
		test_helper.setEditorContent(self.codewave.editor, textwrap.dedent("""\
			<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
			<!-- ~  Lorem ipsum dolor                     ~ -->
			<!-- ~  ~~box|~~                               ~ -->
			<!-- ~  sit amet, consectetur                 ~ -->
			<!-- ~  ~~/box~~                              ~ -->
			<!-- ~  adipiscing elit.                      ~ -->
			<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->"""))
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, textwrap.dedent("""\
			<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
			<!-- ~  Lorem ipsum dolor                     ~ -->
			<!-- ~  <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->  ~ -->
			<!-- ~  <!-- ~  sit amet, consectetur  ~ -->  ~ -->
			<!-- ~  <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->|  ~ -->
			<!-- ~  adipiscing elit.                      ~ -->
			<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->"""))
			 
	def test_close_nested_box(self):
		self.codewave.editor.setLang('html')
		test_helper.setEditorContent(self.codewave.editor, textwrap.dedent("""\
			<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
			<!-- ~  Lorem ipsum dolor                     ~ -->
			<!-- ~  <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->  ~ -->
			<!-- ~  <!-- ~  sit amet, consectetur  ~ -->  ~ -->
			<!-- ~  <!-- ~  ~~close|~~              ~ -->  ~ -->
			<!-- ~  <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->  ~ -->
			<!-- ~  adipiscing elit.                      ~ -->
			<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->"""))
		self.codewave.onActivationKey()
		self.assertRegex(self.codewave.editor.text,
			re.compile('^'+util.escapeRegExp( textwrap.dedent("""\
				<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
				<!-- ~  Lorem ipsum dolor                     ~ -->
				<!-- ~  ##spaces## ~ -->
				<!-- ~  adipiscing elit.                      ~ -->
				<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->""")
			).replace('\\#\\#spaces\\#\\#','\\s*')+'$'))
	
	# def test_closed_nested_box_should_be_aligned(self):
		# self.codewave.editor.setLang('html')
		# test_helper.setEditorContent(self.codewave.editor, textwrap.dedent("""\
			# <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
			# <!-- ~  Lorem ipsum dolor                     ~ -->
			# <!-- ~  <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->  ~ -->
			# <!-- ~  <!-- ~  sit amet, consectetur  ~ -->  ~ -->
			# <!-- ~  <!-- ~  ~~close|~~              ~ -->  ~ -->
			# <!-- ~  <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->  ~ -->
			# <!-- ~  adipiscing elit.                      ~ -->
			# <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->"""))
		# self.codewave.onActivationKey()
		# matchExp = re.compile('^'+util.escapeRegExp( textwrap.dedent("""\
				# <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
				# <!-- ~  Lorem ipsum dolor                     ~ -->
				# <!-- ~  ##spaces##  ~ -->
				# <!-- ~  adipiscing elit.                      ~ -->
				# <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->""")
			# ).replace('\\#\\#spaces\\#\\#','(\\s*)')+'$')
		# self.assertRegex(self.codewave.editor.text, matchExp)
		# match = re.search(matchExp,self.codewave.editor.text)
		# self.assertEqual(len(match.group(1)), 36)
		# test_helper.assertEditorResult(self,self.codewave.editor, textwrap.dedent("""\
			# <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
			# <!-- ~  Lorem ipsum dolor                     ~ -->
			# <!-- ~  |                                      ~ -->
			# <!-- ~  adipiscing elit.                      ~ -->
			# <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->"""))
			 
	# def test_close_parent_of_nested_box(self):
		# self.codewave.editor.setLang('html')
		# test_helper.setEditorContent(self.codewave.editor, textwrap.dedent("""\
			# <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
			# <!-- ~  Lorem ipsum dolor                     ~ -->
			# <!-- ~  <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->  ~ -->
			# <!-- ~  <!-- ~  sit amet, consectetur  ~ -->  ~ -->
			# <!-- ~  <!-- ~  ~~close~~              ~ -->  ~ -->
			# <!-- ~  <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->  ~ -->
			# <!-- ~  adipiscing elit.                      ~ -->
			# <!-- ~  ~~close|~~                             ~ -->
			# <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->"""))
		# self.codewave.onActivationKey()
		# test_helper.assertEditorResult(self,self.codewave.editor, '|')
		
		
	# def test_follow_alias_with_name_wildcard(self):
		# self.codewave.editor.setLang('html')
		# test_helper.setEditorContent(self.codewave.editor, '~~php:outer:f|~~')
		# self.codewave.onActivationKey()
		# test_helper.assertEditorResult(self,self.codewave.editor, textwrap.dedent("""\
				# <?php
					# function |() {
						
					# }
				# ?>"""))
		
	
	# def test_replace_box(self):
		# self.codewave.editor.setLang('js')
		# test_helper.setEditorContent(self.codewave.editor, textwrap.dedent("""\
			# /* ~~~~~~~~~~~~~~~~~~~~~~~~~~ */
			# /* ~  ~~test:replace_box|~~  ~ */
			# /* ~~~~~~~~~~~~~~~~~~~~~~~~~~ */"""))
		# self.codewave.onActivationKey()
		# test_helper.assertEditorResult(self,self.codewave.editor, textwrap.dedent("""\
			# /* ~~~~~~~~~~~~~~~~~ */
			# /* ~  Lorem ipsum  ~ */
			# /* ~~~~~~~~~~~~~~~~~ */|"""))
			
  # def test_emmet(self):
    # self.codewave.editor.setLang('html')
    # test_helper.setEditorContent(self.codewave.editor, '~~ul>li|~~')
    # self.codewave.onActivationKey()
    # test_helper.assertEditorResult(self,self.codewave.editor, textwrap.dedent("""\
      # <ul>
        # <li>|</li>
      # </ul>"""))
	
	def test_display_help(self):
		self.codewave.editor.setLang('html')
		test_helper.setEditorContent(self.codewave.editor, '~~help|~~')
		self.codewave.onActivationKey()
		self.assertIn('~~~~~~~~~~', self.codewave.editor.text)
		self.assertIn('Codewave', self.codewave.editor.text)
		self.assertIn('/ /__/ _ \\/ _` / -_\\ \\/\\/ / _` \\ V / -_/', self.codewave.editor.text) # slice from the ascii logo
		self.assertIn('~~close~~', self.codewave.editor.text)
		
	def test__help_demo_should_expend_editing_intro(self):
		self.codewave.editor.setLang('html')
		test_helper.setEditorContent(self.codewave.editor, '~~help:demo|~~')
		self.codewave.onActivationKey()
		self.assertIn('~~~~~~~~~~', self.codewave.editor.text)
		self.assertIn('~~close~~', self.codewave.editor.text)
		self.assertNotIn('~~help:editing:intro~~', self.codewave.editor.text)
		self.assertIn('Codewave allows you to make your own commands', self.codewave.editor.text)
		
		
if __name__ == '__main__':
		unittest.main()