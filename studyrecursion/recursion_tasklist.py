from studygv.create_graph import create_graph_code
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
dot = gv.Graph(comment='Task List', engine='circo')
# dot = gv.Graph(comment='Task List')

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
