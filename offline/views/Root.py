from easy_tk import EasyTkObject
from tkinter.ttk import Notebook
from tkinter import Frame,HORIZONTAL
from views.FrameMatchInfo import FrameMatchInfo
from views.FrameEditor import FrameEditor
from views.FrameTest import FrameTest
from views.FrameCut import FrameCut
from views.FrameRender import FrameRender
from views.FrameHome import FrameHome
from models import factory_model

class Root(EasyTkObject):
    
    def __init__(self):
        super(Root, self).__init__()
        self.create_root()
        self.geometry = "895x351"
        self.tabs = {}
        self.model = factory_model()
        notebook = self.set_notebook()
        self.set_all_frames(notebook)
        self.change_geometry()


    def set_notebook(self):
        self.import_modules([Notebook,])
        self.add_just_one('views/json/notebook.json','NotebookTest')
        child = self.get('NotebookTest',False)
        master = self.easy.create_master(child.obj,'NotebookTest')
        return {'TkChild':child,'TkMaster':master,"name":'NotebookTest'}

    def change_geometry(self):
        self.root.geometry("446x423")
        self.root.update()

    def set_all_frames(self,notebook):
        self.easy.widgets_on_screen()
        for frame in (FrameHome,FrameMatchInfo,FrameEditor,FrameTest,FrameCut,FrameRender,):
            frame = frame()
            frame.set_controller(self)
            frame.set_model(self.model)
            frame.adding_complete_widgets(self.get_easy_root(),notebook)
            frame.create_widgets()
            notebook['TkChild'].get().add(frame.get(frame.name),text=frame.tab_text)
            self.tabs[type(frame).__name__] = frame
        self.get('NotebookTest').bind('<<NotebookTabChanged>>',self.tab_changed)
        

    def get_easy_root(self):
        child = self.get("root", False)
        master = self.easy.create_master(child.get(),'root')
        return {"TkChild": child, "TkMaster": master, "name": "root"}
    
    def tab_changed(self,event):
        selection = event.widget.select()
        tab = event.widget.tab(selection, "text")
        if tab == "Testing":
            self.tabs['FrameTest'].download_testing()
            self.root.geometry("1040x396")
        elif tab in ("Cat","Render"):
            self.tabs["FrameCut"].get_can_cut()
        else:
            self.change_geometry()

    def switch_to_editor(self,ID,halftime):
        self.get("NotebookTest").select(1)
        self.tabs['FrameEditor'].download_highlights(ID)

        self.tabs['FrameMatchInfo'].download_match_comp(ID,halftime)
        self.tabs['FrameMatchInfo'].change_fields()
        
        self.tabs['FrameEditor'].change_fields()
        self.tabs['FrameEditor'].filter_halftime()