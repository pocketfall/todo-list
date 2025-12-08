import customtkinter as ctk
from collections.abc import Callable
from config import WINDOW_WIDTH

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
		ctk.CTkLabel(self, text= "Enter a task: ", font= font).pack(side= "left", fill= "both", padx= 10)
		ctk.CTkEntry(self, textvariable= entry_variable, font= font, width= WINDOW_WIDTH // 2).pack(side= "left", fill= "x", expand= True, padx= 10)
		ctk.CTkButton(self, command= button_func, text= "Enter", font= font).pack(side= "left")

class Task(ctk.CTkFrame):
	"""
	Class that houses, in this order, a checkbox, label, and button.
	the checkbox is for marking if a task is complete or not, the label is the task
	and the final button is for deleting the task
	"""
	def __init__(self, parent, 
			  frame_color: str, 
			  label_text: str, 
			  font: tuple, 
			  kill_command: Callable[[int], None], 
			  task_number: int) -> None:
		super().__init__(master= parent, fg_color= frame_color)
		ctk.CTkCheckBox(self, width= 50).pack(expand= True, fill= "both", side= "left")
		ctk.CTkLabel(self, text= label_text, font= font).pack(expand= True, fill= "both", side= "left")
		ctk.CTkButton(self, 
				command= lambda x= task_number: kill_command(x), 
				text= "X", 
				font= font).pack(expand= True, fill= "both", side= "left")

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

