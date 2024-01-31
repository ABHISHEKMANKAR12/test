from task_package.create_task import create_task
from task_package.edit_task import edit_task
from task_package.category_task import category_task

#create a task
task1=create_task("complete your assignment","finish task management system")

#display the task
print("task1:",task1)

#edit the task
edit_task(task1,new_title="updated assignment",new_description="review and submit to Rashmi mam")
print("updated task",task1)

#category the task
category_task(task1,"zappkode academy")

#display the category task
print("category task:",task1)