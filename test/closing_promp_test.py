import unittest
import textwrap
import re

import codewave_core.util as util
import codewave_core.codewave as codewave
import test.test_editor as test_editor

import test.test_helper as test_helper

class PhpTestCase(unittest.TestCase):
	def setUp(self):
		codewave.init()
		self.codewave = codewave.Codewave(test_editor.TestEditor('Lorem Ipsum'))
		
	def test_add_listener(self):
		self.assertEqual(len(self.codewave.editor.changeListeners), 0)
		test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		self.codewave.onActivationKey()
		self.assertEqual(len(self.codewave.editor.changeListeners), 1)
		
	def test_create_ref_in_Codewave_obj(self):
		self.assertEqual(len(self.codewave.editor.changeListeners), 0)
		test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		self.codewave.onActivationKey()
		self.assertIsNotNone
		
	def test_remove_ref_when_stopping(self):
		self.assertEqual(len(self.codewave.editor.changeListeners), 0)
		test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		self.codewave.onActivationKey()
		self.assertIsNotNone
		self.codewave.closingPromp.stop()
		self.assertIsNone
		
	def test_remove_listener_when_stopping(self):
		self.assertEqual(len(self.codewave.editor.changeListeners), 0)
		test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		self.codewave.onActivationKey()
		self.assertEqual(len(self.codewave.editor.changeListeners), 1)
		self.codewave.closingPromp.stop()
		self.assertEqual(len(self.codewave.editor.changeListeners), 0)
		
	def test_create_2_selections(self):
		test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~\nlorem ipsum\n~~/|~~')

	def test_find_whithin_open_bounds(self):
		test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		self.codewave.onActivationKey()
		closingPromp = self.codewave.closingPromp
		test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~\nlorem ipsum\n~~/|~~')
		text, sels = test_helper.extractSelections('|~~|~~|\nlorem ipsum\n~~/~~')

		self.assertEqual(closingPromp.startPosAt(0).raw(), [sels[0].start,sels[2].end])
		self.assertEqual(closingPromp.startPosAt(0).innerContainsPos(sels[1]), True)
		self.assertEqual(closingPromp.typed(), '')
		self.assertEqual(closingPromp.codewave.brakets + (closingPromp.typed() or '') + closingPromp.codewave.brakets, '~~~~')
		self.assertEqual(closingPromp.startPosAt(0).text(), '~~~~')
		
		self.assertIsNotNone(closingPromp.whithinOpenBounds(sels[1]))
		self.assertEqual(closingPromp.whithinOpenBounds(sels[1]).raw(), [sels[0].start,sels[2].end])
		

	def test_find_whithin_close_bounds(self):
		test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		self.codewave.onActivationKey()
		closingPromp = self.codewave.closingPromp
		test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~\nlorem ipsum\n~~/|~~')
		text, sels = test_helper.extractSelections('~~~~\nlorem ipsum\n|~~/|~~|')
		
		self.assertEqual(closingPromp.endPosAt(0).raw(), [sels[0].start,sels[2].end])
		self.assertEqual(closingPromp.endPosAt(0).innerContainsPos(sels[1]), True)
		self.assertEqual(closingPromp.typed(), '')
		self.assertEqual(closingPromp.codewave.brakets + closingPromp.codewave.closeChar + closingPromp.typed() + closingPromp.codewave.brakets, '~~/~~')
		self.assertEqual(closingPromp.endPosAt(0).text(), '~~/~~')
		
		self.assertIsNotNone(closingPromp.whithinCloseBounds(sels[1]))
		self.assertEqual(closingPromp.whithinCloseBounds(sels[1]).raw(), [sels[0].start,sels[2].end])
		
	def test_revert_when_empty(self):
		test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~\nlorem ipsum\n~~/|~~')
		
		text, sels = test_helper.extractSelections('~~|~~\nlorem ipsum\n~~/~~')
		self.assertIsNotNone(self.codewave.commandOnPos(sels[0].start))
		
		self.codewave.onActivationKey()
		test_helper.assertEditorResult(self,self.codewave.editor, '|[lorem ipsum]')
		
	def test_ref_should_stay_the_same(self):
		test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		self.codewave.onActivationKey()
		closingPromp = self.codewave.closingPromp
		self.assertEqual(closingPromp.nbChanges, 0)
		test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~\nlorem ipsum\n~~/|~~')
		test_helper.setEditorContent(self.codewave.editor, '~~e|~~\nlorem ipsum\n~~/e|~~')
		self.codewave.editor.onAnyChange()
		self.assertEqual(self.codewave.closingPromp, closingPromp)
		
	def test_react_to_change(self):
		test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		self.codewave.onActivationKey()
		closingPromp = self.codewave.closingPromp
		self.assertEqual(closingPromp.nbChanges, 0)
		test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~\nlorem ipsum\n~~/|~~')
		test_helper.setEditorContent(self.codewave.editor, '~~e|~~\nlorem ipsum\n~~/e|~~')
		self.codewave.editor.onAnyChange()
		self.assertEqual(closingPromp.nbChanges, 1)
		
	def test_keep_going_after_one_letter(self):
		test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		self.codewave.onActivationKey()
		closingPromp = self.codewave.closingPromp
		test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~\nlorem ipsum\n~~/|~~')
		test_helper.setEditorContent(self.codewave.editor, '~~e|~~\nlorem ipsum\n~~/e|~~')
		self.codewave.editor.onAnyChange()
		self.assertIsNotNone
		
	def test_detect_typed_text(self):
		test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		self.codewave.onActivationKey()
		closingPromp = self.codewave.closingPromp
		test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~\nlorem ipsum\n~~/|~~')
		test_helper.setEditorContent(self.codewave.editor, '~~test|~~\nlorem ipsum\n~~/test|~~')
		self.codewave.editor.onAnyChange()
		self.assertEqual(closingPromp.typed(), 'test')
		
	def test_stop_after_space(self):
		test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		self.codewave.onActivationKey()
		closingPromp = self.codewave.closingPromp
		test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~\nlorem ipsum\n~~/|~~')
		test_helper.setEditorContent(self.codewave.editor, '~~test |~~\nlorem ipsum\n~~/test |~~')
		self.codewave.editor.onAnyChange()
		self.assertEqual(closingPromp.shouldStop(), True)
		self.assertEqual(closingPromp.started, False)
		
	def test_remove_space_after_stop(self):
		test_helper.setEditorContent(self.codewave.editor, '|[lorem ipsum]')
		self.codewave.onActivationKey()
		closingPromp = self.codewave.closingPromp
		test_helper.assertEditorResult(self,self.codewave.editor, '~~|~~\nlorem ipsum\n~~/|~~')
		test_helper.setEditorContent(self.codewave.editor, '~~test |~~\nlorem ipsum\n~~/test |~~')
		self.codewave.editor.onAnyChange()
		self.assertEqual(closingPromp.started, False)
		test_helper.assertEditorResult(self,self.codewave.editor, '~~test |~~\nlorem ipsum\n~~/test~~')


		
if __name__ == '__main__':
		unittest.main()