from components import Task
from config import SAVE_FOLDER
from glob import glob

class TaskWriter:
	"""
	class made to manage the creation of a file to contain the todo list
	the user has created, it should reflect what the user does to the list
	"""
	def __init__(self, task_list: list[Task]) -> None:
		# variables
		self.task_list = task_list
		self.folder_contents = glob(f"./{SAVE_FOLDER}/list*")
		self.file_name = None

	def save_file(self) -> None:
		self.name_file()
		self.write_task_file(self.file_name)
	
	def write_task_file(self, list_name) -> None:
		with open(f"{SAVE_FOLDER}/{list_name}", "w") as f:
			for task in self.task_list:
				task_dict = self.unpack_task_data(task)
				task_data_formatted = self.format_task_data(task_dict)
				f.write(task_data_formatted)
				
	
	def format_task_data(self, task_data: dict) -> str:
		task_data_formatted = f"{task_data['list_idx']},{task_data['is_checked']},{task_data['task']}\n"
		return task_data_formatted

	def unpack_task_data(self, task: Task) -> dict:
		task_name = str(task.task_text)
		task_is_checked = task.is_checked
		task_number = task.task_number
		return {"list_idx": task_number, "is_checked": task_is_checked, "task": task_name}

	def name_file(self) -> None:
		print(self.folder_contents)
		folder_contents_sorted = sorted([list_num.split("/")[-1] for list_num in self.folder_contents])
		print(folder_contents_sorted)
		if "list0.txt" in folder_contents_sorted:
			# name the file list<list_count>
			list_count = len(self.folder_contents)
			self.file_name = f"list{list_count}.txt"
		else:
			self.file_name = "list0.txt"
