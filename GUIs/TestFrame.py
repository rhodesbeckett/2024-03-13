from tkinter import *
from editor import FootballEditor
from editor.Checker import Checker as Checker
class TestFrame(Frame):
	def __init__(self, parent, controller,fe,checker):
		Frame.__init__(self, parent)
		self.footballEditor = fe
		self.checker = checker
		self.controller = controller
		self.grid(row=0, column=0, sticky=W)
		self.create_widgets()
	def create_widgets(self):
		self.nazadBtn = Button(self,text="Nazad a ovo je TestFrame",command=lambda var="FootballFrame": self.controller.prebaci_frejm(var))
		self.nazadBtn.grid()
	def proveraEntries(self,lista = [],stringVars = [],prvoPol = 0,drugoPol = 0):
		vremenaUSekundama = self.footballEditor.checker.proveraEntries(lista,stringVars,prvoPol,drugoPol)
		self.footballEditor.checker.vremenaUSekundama = vremenaUSekundama
		for i in vremenaUSekundama:
			print(i)