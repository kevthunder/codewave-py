import re
import codewave_core.util as util

def assertEditorResult(test_case,editor,res):
	realText,sels = extractSelections(res)
	test_case.assertEqual(editor.text,realText)
	if len(sels):
		if editor.allowMultiSelection():
			test_case.assertEqual(list(map(lambda s: s.raw(), editor.getMultiSel())), list(map(lambda s: s.raw(), sels)))
		else:
			test_case.assertEqual(editor.getCursorPos().raw(),sels[0].raw())
	
def setEditorContent(editor,val):
	realText,sels = extractSelections(val)
	if len(sels):
		if editor.allowMultiSelection():
			editor.setMultiSel(sels)
		else:
			editor.setCursorPos(sels[0].start,sels[0].end)
	editor.text = realText

def extractSelections(text):
	sels = []
	finalText = text
	while True:
		match = re.search(r'\|\[(.*)\]',finalText)
		if match is not None:
			sels.append(util.Pos(match.start(),match.start()+len(match.group(1))))
			finalText = re.sub(r'\|\[(.*)\]',r'\1',finalText,1)
		elif '|' in finalText:
			sels.append(util.Pos(finalText.index('|')))
			finalText = finalText.replace('|','',1)
		else:
			break
	return [finalText,sels]
