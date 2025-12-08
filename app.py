import customtkinter as ctk
from config import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, WHITE, FONT
from components import SimpleEntry, TaskContainer, Task

class App(ctk.CTk):
	def __init__(self) -> None:
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
		self.task_container = None

		# widgets
		self.create_widgets()

		# app loop
		self.mainloop()
	
	def create_widgets(self) -> None:
		SimpleEntry(parent= self, entry_variable= self.task_string, frame_color= BLACK,
			  font= self.font, button_func= self.enter_task).pack(fill= "x", expand= True, padx= 10, pady= 5)
		self.task_container = TaskContainer(parent= self, frame_color= WHITE, tasks= self.task_list)
		self.task_container.pack(fill= "both", expand= True, padx= 5, pady= 5)
	
	def enter_task(self) -> None:
		new_task = self.create_task()
		if new_task:
			self.task_list.append(new_task)
			self.task_container.display_tasks(self.task_list)
			
	
	def create_task(self) -> Task:
		try:
			task_number = len(self.task_list)
			return Task(parent= self.task_container, 
			   frame_color= "red", 
			   label_text= self.task_string.get(), 
			   font= self.font, 
			   kill_command= self.delete_task,
			   task_number= task_number)
		except Exception as e:
			print(e)
			return None

	def delete_task(self, list_idx: int) -> None:
		self.task_list.remove(self.task_list[list_idx - 1])
		self.task_container.winfo_children()[list_idx - 1].destroy()

if __name__ == "__main__":
	App()
