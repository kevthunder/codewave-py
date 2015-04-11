
import codewave_core.command as command
import codewave_core.core_cmds

class EditCmdProp():
	def __init__(self, name,options):
		self.name,options = name,options
		defaults = {
			'var' : None,
			'opt' : None,
			'funct' : None,
			'dataName' : None,
			'showEmpty' : False,
			'carret' : False,
		}
		for key in ['var','opt','funct']:
			if key in options:
				defaults['dataName'] = options[key]
		for key, val in defaults.items():
			if key in options:
				setattr(self,key,options[key])
			else:
				setattr(self,key,val)
				
	def setCmd(self,cmds):
		cmds[self.name] = codewave_core.core_cmds.setVarCmd(self.name)
	
	def writeFor(self,parser,obj):
		if parser.vars[self.name] is not None:
			obj[self.dataName] = parser.vars[self.name]
	def valFromCmd(self,cmd):
		if cmd is not None:
			if self.opt is not None:
				return cmd.getOption(self.opt)
			if self.funct is not None:
				return cmd[self.funct]()
			if self.var is not None:
				return cmd[self.var]
	def showForCmd(self,cmd):
		val = self.valFromCmd(cmd)
		return self.showEmpty or val is not None
	def display(self,cmd):
		if self.showForCmd(cmd):
			return "~~!"+self.name+"~~" +
				(self.valFromCmd(cmd) or "")+("|" if self.carret else "") +
				"~~!/"+self.name+"~~"
		
		
class self.edit_cmd_prop.source extends self.Codewave.EditCmdProp 
	def setCmd(self,cmds):
		cmds[self.name] = codewave_core.core_cmds.setVarCmd(self.name,{'preventParseAll' : True})
	def showForCmd(self,cmd):
		val = self.valFromCmd(cmd)
		return (self.showEmpty and !(cmd is not None and cmd.aliasOf?)) or val is not None
		
		
class string(EditCmdProp):
	def display(self,cmd):
		if self.valFromCmd(cmd)?:
			return "~~!"+self.name+" '"+(self.valFromCmd(cmd) or "")+("|" if self.carret else "")+"'~~"
		
		
class revBool(EditCmdProp):
	def setCmd(self,cmds):
		cmds[self.name] = codewave_core.core_cmds.setBoolVarCmd(self.name)
	def writeFor(self,parser,obj):
		if parser.vars[self.name] is not None:
			obj[self.dataName] = not parser.vars[self.name]
	def display(self,cmd):
		val = self.valFromCmd(cmd)
		if val is not None and not val:
			return "~~!"+self.name+"~~"

		
class bool(EditCmdProp):
	def setCmd(self,cmds):
		cmds[self.name] = codewave_core.core_cmds.setBoolVarCmd(self.name)
	def display(self,cmd):
		if self.valFromCmd(cmd)
			return "~~!"+self.name+"~~" 