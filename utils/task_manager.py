import threading

def run_task(task, args, callback):
    # task: function
    # args: tuple with arguments to function [task]
    # callback: function that is called after task is finished. Uses the return from task as argument
    # Takes a task, runs the task on a seperate thread, then returns the result of task to result function
    def wrapper():
        result = task(*args)
        callback(result)
        
    thread = threading.Thread(target=wrapper)
    thread.start()
    return thread