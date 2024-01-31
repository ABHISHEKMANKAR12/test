from .task import task
def create_task(title,description,category=None):
    new_task=task(title,description,category)
    return new_task