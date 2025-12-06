import customtkinter as ctk
from config import WINDOW_WIDTH

class SimpleEntry(ctk.CTkFrame):
	"""
	Class that creates a frame containing a CTkLabel, CTkEntry and CTkButton in a row
	"""
	def __init__(self, parent, entry_variable, frame_color, font, button_func):
		super().__init__(master= parent, fg_color= frame_color)
		ctk.CTkLabel(self, text= "Enter a task: ", font= font).pack(side= "left", fill= "both", padx= 10)
		ctk.CTkEntry(self, textvariable= entry_variable, font= font, width= WINDOW_WIDTH // 2).pack(side= "left", fill= "x", expand= True, padx= 10)
		ctk.CTkButton(self, command= button_func, text= "Enter", font= font).pack(side= "left")

class TaskContainer(ctk.CTkScrollableFrame):
	"""
	Class that houses task objects within it while allowing scrolling
	"""
	def __init__(self, parent, frame_color):
		super().__init__(master= parent, fg_color= frame_color)

class Task(ctk.CTkFrame):
	"""
	Class that houses, in this order, a checkbox, label, and button.
	the checkbox is for marking if a task is complete or not, the label is the task
	and the final button is for deleting the task
	"""
	def __init__(self, parent, frame_color, label_text, font, kill_command):
		super().__init__(master= parent, fg_color= frame_color)
		ctk.CTkCheckBox(self).pack(expand= True, fill= "both")
		ctk.CTkLabel(self, text= label_text, font= font).pack(expand= True, fill= "both")
		ctk.CTkButton(self, command= kill_command, text= "X", font= font).pack(expand= True, fill= "both")

