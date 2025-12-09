from components import Task

class TaskWriter:
	"""
	class made to manage the creation of a file to contain the todo list
	the user has created, it should reflect what the user does to the list
	"""
	def __init__(self, task_list: list[Task]):
		self.task_list = task_list
	
	def write_task_file(self, list_name):
		with open(f"task_lists/{list_name}", "w") as f:
			pass
