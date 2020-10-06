from utils.Seckanje import checkIfReady

def startTRender(obj, threading):
	obj.t_render = threading.Thread(target=obj.runRender)
	obj.t_render.start()


def getTRender(obj):
	return obj.t_render.is_alive()


def runRender(obj, messagebox, os):
	if(checkIfReady(obj,True,messagebox)):
		obj.runCut(False)
		obj.footballEditor.mergeAll()
		obj.footballEditor.vremenaUSekundama = []
		obj.footballEditor.highlightsCounter = 0
		messagebox.showinfo('Renderovanje', 'Renderovanje zavrseno.')
		os.startfile(obj.footballEditor.imeFoldera)
