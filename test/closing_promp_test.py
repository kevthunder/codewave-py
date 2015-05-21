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
		
	# def test_add_listener(self):
		# self.assertEqual(len(self.codewave.editor.changeListeners), 0)
		# test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		# self.codewave.onActivationKey()
		# self.assertEqual(len(self.codewave.editor.changeListeners), 1)
		
	# def test_create_ref_in_Codewave_obj(self):
		# self.assertEqual(len(self.codewave.editor.changeListeners), 0)
		# test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		# self.codewave.onActivationKey()
		# self.assertIsNotNone
		
	# def test_remove_ref_when_stopping(self):
		# self.assertEqual(len(self.codewave.editor.changeListeners), 0)
		# test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		# self.codewave.onActivationKey()
		# self.assertIsNotNone
		# self.codewave.closingPromp.stop()
		# self.assertIsNone
		
	# def test_remove_listener_when_stopping(self):
		# self.assertEqual(len(self.codewave.editor.changeListeners), 0)
		# test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		# self.codewave.onActivationKey()
		# self.assertEqual(len(self.codewave.editor.changeListeners), 1)
		# self.codewave.closingPromp.stop()
		# self.assertEqual(len(self.codewave.editor.changeListeners), 0)
		
	# def test_create_2_selections(self):
		# test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		# self.codewave.onActivationKey()
		# test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~\nlorem ipsum\n~~/|~~')
		
	# def test_revert_when_empty(self):
		# test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		# self.codewave.onActivationKey()
		# test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~\nlorem ipsum\n~~/|~~')
		# self.codewave.onActivationKey()
		# test_helper.assertEditorResult(self,self.codewave.editor, '|[lorem ipsum]')
		
	# def test_ref_should_stay_the_same(self):
		# test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		# self.codewave.onActivationKey()
		# closingPromp = self.codewave.closingPromp
		# self.assertEqual(closingPromp.nbChanges, 0)
		# test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~\nlorem ipsum\n~~/|~~')
		# test_helper.setEditorContent(self.codewave.editor, '~~e|~~\nlorem ipsum\n~~/e|~~')
		# self.codewave.editor.onAnyChange()
		# self.assertEqual(self.codewave.closingPromp, closingPromp)
		
	# def test_react_to_change(self):
		# test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		# self.codewave.onActivationKey()
		# closingPromp = self.codewave.closingPromp
		# self.assertEqual(closingPromp.nbChanges, 0)
		# test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~\nlorem ipsum\n~~/|~~')
		# test_helper.setEditorContent(self.codewave.editor, '~~e|~~\nlorem ipsum\n~~/e|~~')
		# self.codewave.editor.onAnyChange()
		# self.assertEqual(closingPromp.nbChanges, 1)
		
	# def test_keep_going_after_one_letter(self):
		# test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		# self.codewave.onActivationKey()
		# closingPromp = self.codewave.closingPromp
		# test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~\nlorem ipsum\n~~/|~~')
		# test_helper.setEditorContent(self.codewave.editor, '~~e|~~\nlorem ipsum\n~~/e|~~')
		# self.codewave.editor.onAnyChange()
		# self.assertIsNotNone
		
	# def test_detect_typed_text(self):
		# test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		# self.codewave.onActivationKey()
		# closingPromp = self.codewave.closingPromp
		# test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~\nlorem ipsum\n~~/|~~')
		# test_helper.setEditorContent(self.codewave.editor, '~~test|~~\nlorem ipsum\n~~/test|~~')
		# self.codewave.editor.onAnyChange()
		# self.assertEqual(closingPromp.typed(), 'test')
		
	# def test_stop_after_space(self):
		# test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		# self.codewave.onActivationKey()
		# closingPromp = self.codewave.closingPromp
		# test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~\nlorem ipsum\n~~/|~~')
		# test_helper.setEditorContent(self.codewave.editor, '~~test |~~\nlorem ipsum\n~~/test |~~')
		# self.codewave.editor.onAnyChange()
		# self.assertEqual(closingPromp.shouldStop(), True)
		# self.assertEqual(closingPromp.started, False)
		
	# def test_remove_space_after_stop(self):
		# test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		# self.codewave.onActivationKey()
		# closingPromp = self.codewave.closingPromp
		# test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~\nlorem ipsum\n~~/|~~')
		# test_helper.setEditorContent(self.codewave.editor, '~~test |~~\nlorem ipsum\n~~/test |~~')
		# self.codewave.editor.onAnyChange()
		# self.assertEqual(closingPromp.started, False)
		# test_helper.assertEditorResult(self,self.codewave.editor, '~~test |~~\nlorem ipsum\n~~/test~~')


		
if __name__ == '__main__':
		unittest.main()