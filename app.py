import customtkinter as ctk
from config import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, WHITE, FONT
from components import SimpleEntry, TaskContainer, Task

class App(ctk.CTk):
	def __init__(self):
		# window configuration
		super().__init__()
		self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
		self.resizable(False, False)
		self.title("To do list")
		ctk.set_appearance_mode("dark")

		# variables
		self.task_string = ctk.StringVar()
		self.font = FONT
		self.task_list = []

		# widgets
		self.create_widgets()

		# app loop
		self.mainloop()
	
	def create_widgets(self):
		SimpleEntry(parent= self, entry_variable= self.task_string, frame_color= BLACK,
			  font= self.font, button_func= self.enter_task).pack(fill= "x", expand= True, padx= 10, pady= 5)
		TaskContainer(parent= self, frame_color= WHITE).pack(fill= "both", expand= True, padx= 5, pady= 5)
	
	def enter_task(self):
		new_task = self.create_task()
		if new_task:
			self.task_list.append(new_task)
	
	def create_task(self):
		try:
			return Task(parent= self, frame_color= "red", label_text= self.task_string.get(), font= self.font, kill_command= self.delete_task)
		except Exception as e:
			print(e)
			return None

	def delete_task(self):
		pass

if __name__ == "__main__":
	App()
