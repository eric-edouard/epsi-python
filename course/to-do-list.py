

class ToDoList():
    def __init__(self):
        self.todos = []

    def add_todo(self, task):
        self.todos.append({'is_done': False, 'task': task})

    def remove_todo(self, index):
        del self.todos[index]

    def toggle_todo(self, index):
        self.todos[index]['is_done'] = not self.todos[index]['is_done']

    def print(self):
        for i in range(len(self.todos)):
            todo = self.todos[i]
            print(
                f"{i}  -  [{'X' if todo['is_done'] else ' '}] {todo['task']}")


todo_list = ToDoList()

user_input = ""

while (not "exit" in user_input):
    user_input = input("Action ? \n")
    if ("add" in user_input):
        task = input("Task ? ")
        todo_list.add_todo(task)
        todo_list.print()

    if ("remove" in user_input):
        index = input("Index ? ")
        todo_list.remove_todo(int(index))
        todo_list.print()

    if ("toggle" in user_input):
        index = input("Index ? ")
        todo_list.toggle_todo(int(index))
        todo_list.print()


    if ("print" in user_input):
        todo_list.print()
