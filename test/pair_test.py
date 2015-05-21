import unittest
import textwrap
import re
import test.test_helper as test_helper

import codewave_core.util as util
import codewave_core.codewave as codewave
import codewave_core.text_parser as text_parser

class PairTestCase(unittest.TestCase):
	def setUp(self):
		self.pair = None
		
	# def test_find_next_opening(self):
		# self.pair = util.Pair('1','2')
		# text = "abc 1 2 1 2"
		# res = self.pair.matchAny(text)
		
		# self.assertIsNotNone(res)
		# self.assertEqual(res.start(), 4)
		# self.assertEqual(res.name(), 'opener')
		
	# def test_find_after_offset(self):
		# self.pair = util.Pair('1','2')
		# text = "abc 1 2 1 2"
		# res = self.pair.matchAny(text,5)
		
		# self.assertIsNotNone(res)
		# self.assertEqual(res.start(), 6)
		# self.assertEqual(res.name(), 'closer')
		
	# def test_find_next_regexp_opening(self):
		# self.pair = util.Pair(re.compile(r'\d'),re.compile(r'\$'))
		# text = "abc 1 $ 1 $"
		# res = self.pair.matchAny(text)
		
		# self.assertIsNotNone(res)
		# self.assertEqual(res.start(), 4)
		# self.assertEqual(res.name(), 'opener')
		
	# def test_find_last_closing(self):
		# self.pair = util.Pair('1','2')
		# text = "abc 1 2 1 2"
		# res = self.pair.matchAnyLast(text)
		
		# self.assertIsNotNone(res)
		# self.assertEqual(res.start(), 10)
		# self.assertEqual(res.name(), 'closer')
		
	# def test_find_last_regexp_closing(self):
		# self.pair = util.Pair(re.compile(r'\d'),re.compile(r'\$'))
		# text = "abc 1 $ 1 $"
		# res = self.pair.matchAnyLast(text)
		
		# self.assertIsNotNone(res)
		# self.assertEqual(res.start(), 10)
		# self.assertEqual(res.name(), 'closer') 
		
	# def test_match_text_openner_and_closer(self):
		# self.pair = util.Pair('((','))')
		# text = "abc (( def )) end"
		# res = self.pair.wrapperPos(util.Pos(8),text)
		
		# self.assertIsNotNone(res)
		# self.assertEqual(res.raw(), [4,13])
	
	# def test_return_None_on_no_match(self):
		# self.pair = util.Pair('((','))')
		# text = "abc (( def ) end"
		# res = self.pair.wrapperPos(util.Pos(8),text)
		
		# self.assertIsNone(res)
		
	# def test_match_regexp_openner_and_closer(self):
		# self.pair = util.Pair(re.compile('#+-+'),re.compile('-+#+'))
		# text = "abc ##-- def --## end"
		# res = self.pair.wrapperPos(util.Pos(10),text)
		
		# self.assertIsNotNone(res)
		# self.assertEqual(res.raw(), [4,17])
			
	# def test_match_identical_openner_and_closer(self):
		# self.pair = util.Pair('##','##')
		# text = "abc ## def ## end"
		# res = self.pair.wrapperPos(util.Pos(8),text)
		
		# self.assertIsNotNone(res)
		# self.assertEqual(res.raw(), [4,13])
		
	# def test_match_identical_regexp_openner_and_closer(self):
		# self.pair = util.Pair(re.compile('##'),re.compile('##'))
		# text = "abc ## def ## end"
		# res = self.pair.wrapperPos(util.Pos(8),text)
		
		# self.assertIsNotNone(res)
		# self.assertEqual(res.raw(), [4,13])
		
	# def test_match_with_optionnal_close(self):
		# self.pair = util.Pair('((','))',{optionnal_end:True})
		# text = "abc (( def end"
		# res = self.pair.wrapperPos(util.Pos(8),text)
		
		# self.assertIsNotNone(res)
		# self.assertEqual(res.raw(), [4,14])
		
	# def test_allow_match_validation(self):
		# self.pair = util.Pair(re.compile('#+-+'),re.compile('-+#+'),{
			# 'validMatch': (lambda match : len(match)() < 6)
		# })
		# text = "abc ##-- def ---### --## end"
		# res = self.pair.wrapperPos(util.Pos(10),text)
		
		# self.assertIsNotNone(res)
		# self.assertEqual(res.raw(), [4,24])
		
		
		
if __name__ == '__main__':
		unittest.main()