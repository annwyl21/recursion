'''
Casidoo - Given a list of tasks, where each task has a duration, and a limited amount of available time to work, write a function to return the tasks that can be completed within the given time, without re-ordering the original list of tasks.
'''

# define the tasks
tasks = [
  { 'name': 'Load Washing Machine', 'duration': 4 },
  { 'name': 'Clean Sink', 'duration': 2 },
  { 'name': 'Mop Floors', 'duration': 7 },
  { 'name': 'Hang Laundry', 'duration': 5 },
  { 'name': 'Wipe Surfaces', 'duration': 1 },
  { 'name': 'Make Cup of Tea', 'duration': 3 }
]

timeToWork = 6

# ALTERNATIVE SOLUTION

# Co-pilot solution is superb with its use of lambda as a sorting key however, it only offers 1 selection of tasks, and it isn't guarenteed to be the most tasks I can complete.  I wanted to see if I could get all the task combinations that could be completed within the given time.
# Sort tasks by duration, shortest to longest, then iterate through the list of tasks.  If the timeToWork is greater than or equal to the duration of the task, add the task to the completedTasks list and subtract the duration of the task from the timeToWork.  Return the completedTasks list.
def doTasksCP(tasks, timeToWork):
	tasks.sort(key=lambda x: x['duration'])
	completedTasks = []
	for task in tasks:
		if timeToWork - task['duration'] >= 0:
			completedTasks.append(task['name'])
			timeToWork -= task['duration']
	return completedTasks

print("Alternative Solution: ", doTasksCP(tasks, timeToWork=6))
# ['Task 2', 'Task 5', 'Task 6']