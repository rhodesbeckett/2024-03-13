from tkinter import W


class TKWidgets(object):
	def __init__(self, frame):
		self.frame = frame
		self.__parents = {0: {"obj": self.frame, "row": 0, "column": 0, "positions": []}}
		self.font = ("Courier", 15)

	def get_parent(self, parent):
		return self.__parents[parent]["obj"]

	def get_children(self, parent):
		return self.get_parent(parent).winfo_children()

	def get_text(self, parent, index):
		return self.get_children(parent)[index].get()

	def set_text(self, parent, index, text):
		self.get_children(parent)[index]["text"] = text

	def get_object(self, parent, index):
		return self.get_children(parent)[index]

	def get_last_index(self, parent):
		return len(self.get_children(parent)) - 1

	def get_last_children(self, parent):
		return self.get_children(parent)[-1]

	def hide_children(self, parent, index):
		if (index != None):
			self.get_children(parent)[index].grid_remove()
		else:
			self.__parents[parent]["obj"].grid_remove()

	def show_children(self, parent, index):
		if (index != None):
			self.get_children(parent)[index].grid()
		else:
			print(parent)
			self.__parents[parent]["obj"].grid()

	def set(self, key="", value="", parent=None, index=None):
		if (parent == None and index == None):
			self.last[key] = value
		# self.getLastElement()
		else:

			self.get_children(parent)[index][key] = value

	def insert(self, widget, parent, data, newParent=False):
		if (parent in self.__parents):

			if (data != {}):
				row, column = self.__get_column_and_row(parent, data)
				self.__add_position(parent, (row, column))

				widget(self.get_parent(parent)).grid(
					row=row,
					column=column,
					sticky=data["sticky"],
					padx=data["padx"], pady=data["pady"],
					columnspan=data["columnspan"], rowspan=data["rowspan"])
				self.last = self.get_last_children(parent)
				if (newParent == True):
					self.__add_parent(parent)
				else:
					try:
						if (data["text"] == " "):
							self.set("font", self.font, parent, self.get_last_index(parent))
						elif (data["text"] == None):
							return None
						elif (data["text"] != ""):
							self.set_text(parent, self.get_last_index(parent), data["text"])
							self.set("font", self.font, parent, self.get_last_index(parent))


					except:
						print("greska")

	def __row(self, parent):
		row = self.__parents[parent]["row"]
		return row

	def __column(self, parent):
		column = self.__parents[parent]["column"]
		self.__parents[parent]["column"] += 1
		return column

	def setData(self, text="", padx=1, pady=1, sticky=W, rowspan=1, columnspan=1, row=None, column=None,ipadx=0,ipady=0):
		recnik = {"text": text, "padx": padx,
				  "pady": pady, "sticky": sticky,
				  "rowspan": rowspan, "columnspan": columnspan,
				  "row": row, "column": column,
				  "ipadx":0,"ipady":0,
				  }
		return recnik

	def __add_parent(self, parent):
		roditelj = self.get_last_children(parent)
		index = len(self.__parents)
		self.__parents.setdefault(index, {"obj": roditelj, "row": 0, "column": 0, "positions": []})

	def add_new_row(self, parent):
		self.__parents[parent]["row"] += 1
		self.__parents[parent]["column"] = 0

	def set_specific_grid(self, parent, index, row, column):
		self.get_children(parent)[index].grid(row=row, column=column)

	def set_font(self, font):
		self.font = font

	def __get_column_and_row(self, parent, data):

		if (data["column"] == None and data["row"] == None):
			row = self.__row(parent)
			column = self.__column(parent)

			moze = False
			while (moze == False):
				moze = self.__is_pos_available((row, column), parent)
				if (moze == True):
					break
				else:
					column = self.__column(parent)
			return row, column

		else:
			row = data["row"]
			column = data["column"]
			moze = False
			while (moze == False):
				moze = self.__is_pos_available((row, column), parent)
				if (moze == True):
					break
				else:
					column += 1
			return row, column

	def __is_pos_available(self, pos, parent):
		if (pos not in self.__parents[parent]["positions"]):
			return True
		else:
			return False

	def __add_position(self, i, pos):
		self.__parents[i]["positions"].append(pos)
