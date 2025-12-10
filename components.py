import customtkinter as ctk
from collections.abc import Callable
from config import WINDOW_WIDTH, FONT

class SimpleEntry(ctk.CTkFrame):
	"""
	Class that creates a frame containing a CTkLabel, CTkEntry and CTkButton in a row
	"""
	def __init__(self, parent, 
			  entry_variable: ctk.StringVar, 
			  frame_color: str, 
			  font: tuple, 
			  button_func: Callable[[], None]) -> None:
		super().__init__(master= parent, fg_color= frame_color)
		ctk.CTkLabel(self, text= "Enter a task: ", font= FONT).pack(side= "left", fill= "both", padx= 10)
		ctk.CTkEntry(self, textvariable= entry_variable, font= font, width= WINDOW_WIDTH // 2).pack(side= "left", fill= "x", expand= True, padx= 10)
		ctk.CTkButton(self, command= button_func, text= "Enter", font= font).pack(side= "left")

class SuccessWindow(ctk.CTkToplevel):
	"""
	window that shows a brief message saying a todo list was saved
	"""
	def __init__(self):
		super().__init__()
		self.geometry("400x200")
		self.title("Success")
		self.resizable(False, False)

		label_text = "List saved successfully!\nFind it in task_lists (the folder)"
		ctk.CTkLabel(self, text= label_text, font= FONT).pack(fill= "both", expand= True, padx= 10, pady= 10)

class Task(ctk.CTkFrame):
	"""
	Class that has a checkbox with text to display the task the user enterd
	and a button to delete the task
	"""
	def __init__(self, parent, 
			  frame_color: str, 
			  label_text: str, 
			  font: tuple, 
			  kill_command: Callable[[int], None], 
			  task_number: int) -> None:
		super().__init__(master= parent, fg_color= frame_color)

		# variables
		self.task_text = label_text
		self.is_checked = False
		self.task_number = task_number

		# widgets
		ctk.CTkCheckBox(self,
				  text= self.task_text,
				  font= FONT,
				  command= self.checked).pack(expand= True, fill= "both", side= "left")
		ctk.CTkButton(self, 
				command= lambda x= self.task_number: kill_command(x), 
				text= "X", 
				font= font,
				width= 50).place(relx= .9, rely= .5, anchor= "center")
	
	def checked(self):
		"""
		update the self.is_checked variable for storing the task data
		"""
		if not self.is_checked:
			self.is_checked = True
		else:
			self.is_checked = False

class TaskContainer(ctk.CTkScrollableFrame):
	"""
	Class that houses task objects within it while allowing scrolling
	"""
	def __init__(self, parent, 
			  frame_color: str,
			  tasks: list[Task]) -> None:
		super().__init__(master= parent, fg_color= frame_color)
	
	def display_tasks(self, task_list: list[Task]) -> None:
		for task in task_list:
			task.pack(pady= 10, padx= 10, expand= True, fill= "x")

