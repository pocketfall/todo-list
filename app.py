import customtkinter as ctk
from config import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, WHITE, FONT, TRANSPARENT
from components import SimpleEntry, TaskContainer, Task, SuccessWindow
from utility import TaskWriter

class App(ctk.CTk):
	def __init__(self) -> None:
		# window configuration
		super().__init__()
		self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
		self.resizable(False, False)
		self.title("To do list")
		ctk.set_appearance_mode("dark")

		# grid configuration
		self.columnconfigure(0, weight= 1, uniform= "a")
		self.rowconfigure(0, weight= 1, uniform= "a")
		self.rowconfigure(1, weight= 7, uniform= "a")

		# variables
		self.task_string = ctk.StringVar()
		self.list_name = ctk.StringVar()
		self.font = FONT
		self.task_list = []
		self.task_container = None

		# widgets
		self.create_widgets()

		# app loop
		self.mainloop()
	
	def create_widgets(self) -> None:
		# simple entry to enter tasks
		SimpleEntry(parent= self, entry_variable= self.task_string, frame_color= TRANSPARENT,
			  font= self.font, button_func= self.enter_task).grid(row= 0, 
														 column= 0, 
														 sticky= "nsew",
														 padx= 5,
														 pady= 5)

		# button to save the list
		ctk.CTkButton(self, text= "Save list as file", font= self.font,
				command= self.save_list).place(relx= .5, rely= .11, anchor= "center")

		self.task_container = TaskContainer(parent= self, frame_color= WHITE, tasks= self.task_list)
		self.task_container.grid(row= 1, 
						   column= 0, 
						   sticky= "nsew",
						   padx= 10,
						   pady= 10)
	
	def save_list(self) -> None:
		if self.task_list:
			task_writer = TaskWriter(self.task_list)
			task_writer.save_file()
			self.show_successful_save()

		else:
			self.ask_for_tasks()
	
	def show_successful_save(self) -> None:
		SuccessWindow()

	def ask_for_tasks(self) -> None:
		print("no tasks in list")
	
	def enter_task(self) -> None:
		new_task = self.create_task()
		if new_task:
			self.task_list.append(new_task)
			self.task_container.display_tasks(self.task_list)
			
	
	def create_task(self) -> Task:
		try:
			task_number = len(self.task_list)
			return Task(parent= self.task_container, 
			   frame_color= TRANSPARENT, 
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
