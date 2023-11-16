from create_graph import create_graph_code
from recursion_code import doTasks
import graphviz as gv

'''
RELEVANT EXAMPLE OF RECURSION
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

# create a graphviz object
# dot = gv.Graph(comment='Task List', engine='circo')
dot = gv.Graph(comment='Task List')

# set the default node style
dot.node('root', f'{timeToWork}-minutes', color='blue', fillcolor='lightblue', style='filled')

combinations = doTasks(tasks, dot, timeToWork=6)

# render the graph
dot.render('task_list.gv', view=True)

# To get the desired output format
def formatOutput(combinations):
    output = {}
    for i, combo in enumerate(combinations, 1):
        output[i] = combo
    return output

formatted_output = formatOutput(combinations)
# {1: ['Task 1', 'Task 2'], 2: ['Task 4', 'Task 5'], 3: ['Task 2', 'Task 5', 'Task 6']}

print("\nResult:")
for option, listoftasks in formatted_output.items():
    print(f"\tOption {option}: ", end="")
    for index, item in enumerate(listoftasks):
            if index < len(listoftasks) - 1:
                print(f"{item}, ", end="")
            else:
                print(f"{item}")

# Use the formatted output to generate the Graphviz code
# create_graph_code(formatted_output)



# ALTERNATIVE SOLUTION

# Co-pilot solution is superb with its use of lambda as a sorting key however, it only offers 1 selection of tasks.  I wanted to see if I could get all the tasks that could be completed within the given time.
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