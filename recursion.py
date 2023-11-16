import graphviz as gv

def doTasks(tasks, dot, timeToWork, index=0, currentSum=0, currentCombination=[], depth=0, last_node='root'):
	"""
	Recursive function to find combinations of tasks that fit within a specified time limit

	:param tasks: List of tasks where each task is a dictionary with 'name' and 'duration'
	:param dot: Graphviz graph object for visualization
	:param timeToWork: Total time limit for task combinations
	:param index: Current index in the tasks list
	:param currentSum: Current sum of durations in the current combination
	:param currentCombination: Current combination of tasks being considered
	:param depth: Current depth of recursion
	:param last_node: ID of the last node added to the graph
	"""

	# Base case: Exceeding time limit or no more tasks to consider thus preventing an infinite loop
	'''Base Case: The function returns an empty list if the current sum of task durations (currentSum) exceeds timeToWork or if there are no more tasks to consider (index >= len(tasks)).
	When designing a recursive function, defining the base case(s) is one of the first and most important steps. The recursive step (where the function calls itself) should always work towards reaching this base case.'''
	if currentSum > timeToWork or index >= len(tasks):
		return []

	'''Including a Task: The function considers adding the current task to the combination (new_combination_include). If the total duration doesn’t exceed timeToWork, it adds a node and an edge to the graph representing this decision and makes a recursive call to consider the next task.'''
	# Logic for including the current task in the combination
	new_combination_include = currentCombination + [tasks[index]['name']]
	node_id_include = f"{depth+1}_{'-'.join(new_combination_include)}"

	# Check if including the task does not exceed the time limit
	if currentSum + tasks[index]['duration'] <= timeToWork:
		# Create a node and an edge for including the task
		node_name = f'{tasks[index]["name"]} ({tasks[index]["duration"]})'
		dot.node(node_id_include, node_name, color='darkgreen', fillcolor='lightgreen')
		dot.edge(last_node, node_id_include, color='green')
		
		# Recursive call - including the current task (do this chore now, add it and move on)
		combinations = doTasks(tasks, dot, timeToWork, index + 1, currentSum + tasks[index]['duration'], new_combination_include, depth + 1, node_id_include)
	else:
		combinations = []

	'''Excluding a Task: Independently, the function also considers the scenario where the current task is not included (new_combination_exclude). It adds a node and an edge for this decision and then makes a recursive call.'''
	# Logic for excluding the current task from the combination
	new_combination_exclude = list(currentCombination)
	node_id_exclude = f"{depth+1}_{'-'.join(new_combination_exclude)}"
	
	# Create a node and an edge for excluding the task
	
	if currentSum + tasks[index]['duration'] > timeToWork:
		node_name = f'END - {tasks[index]["name"]} ({tasks[index]["duration"]})'
		dot.node(node_id_exclude, node_name, color='pink', fillcolor='lightgrey', shape='box')	
	else:
		node_name = f'SKIP - {tasks[index]["name"]} ({tasks[index]["duration"]})'
		dot.node(node_id_exclude, node_name, style='filled, dashed', color='orange', fillcolor='yellow')
	dot.edge(last_node, node_id_exclude, color='grey')

	# Recursive call - excluding the current task (bank the chore for later, skip it and move on)
	combinations += doTasks(tasks, dot, timeToWork, index + 1, currentSum, new_combination_exclude, depth + 1, node_id_exclude)

	'''Visualization: Each recursive call adds nodes and edges to the Graphviz graph, visualizing the decision tree of including or excluding tasks.'''

	return combinations

# Example usage

tasks = [
  { 'name': 'Load Washing Machine', 'duration': 4 },
  { 'name': 'Clean Sink', 'duration': 2 },
  { 'name': 'Mop Floors', 'duration': 7 },
  { 'name': 'Hang Laundry', 'duration': 5 },
  { 'name': 'Wipe Surfaces', 'duration': 1 },
  { 'name': 'Make Cup of Tea', 'duration': 3 }
]
timeToWork = 6

# Initialize the graph
dot = gv.Graph(comment='Task List')
# dot.attr(rankdir='TB')
dot.attr(label='Should I do this chore now or bank it for later ?')
dot.attr(fontsize='20')
dot.attr('node', style='filled')
dot.node('root', f'Time Available ({timeToWork}-minutes)', color='orange', fillcolor='yellow')

# Run the recursive function
doTasks(tasks, dot, timeToWork)

# Render and view the graph
#dot.render('task_list.gv', view=True)

dot.render('ToDoList', format='png', view=True)