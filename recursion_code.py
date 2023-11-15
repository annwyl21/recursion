import graphviz

def doTasks(tasks, timeToWork, index=0, currentSum=0, currentCombination=[], depth=0):
	dot = graphviz.Graph(comment='Task List', engine='circo')
	dot.attr('node', style='filled')
	dot.node('root', f'{timeToWork}-minutes', color='blue', fillcolor='lightblue')

	task_nodes = {}

	for i, task in enumerate(tasks):
		node_id = f"{task['name']}_{depth}"
		task_nodes[(task['name'], depth)] = node_id
		dot.node(node_id, task['name'])
		
	# Indentation based on recursion depth
	indent = "  " * depth  
	# print(f"{indent}doTasks(index={index}, currentSum={currentSum}, currentCombination={currentCombination})")
	if currentSum > timeToWork:
		print(f"{indent}{currentSum} minutes TOO LONG, {currentCombination}\n")
		prev_item = currentCombination[index - 1]
		dot.edge (task_nodes[(prev_item, depth)], task_nodes[(item, depth)], color='grey')
		dot.node(task_nodes[(item, depth)], item, color='grey', fillcolor='lightgrey')
	else:
		if currentCombination:
			print(f"{indent}calculating... {currentCombination})")
		else:
			print(f"resetting...")

	# Initialize a list to store combinations
	combinations = []

	# If the current sum equals the target time, add the current combination to the list of combinations.
	if currentSum == timeToWork:
		print(f"FOUND combination ({timeToWork} minutes): ", end="")
		for index, item in enumerate(currentCombination):
			if index < len(currentCombination) - 1:
				print(f"{item}, ", end="")
			else:
				print(f"{item}\n")
				prev_item = currentCombination[index - 1]
				dot.edge (task_nodes[(prev_item, depth)], task_nodes[(item, depth)], color='green')
				dot.node(task_nodes[(item, depth)], item, color='blue', fillcolor='lightblue')
		# print(f"{indent}Found combination: {currentCombination}")
		combinations.append(currentCombination)
		return combinations

	# If the sum exceeds the target time or no more tasks are left, return an empty list (base case).
	if currentSum > timeToWork or index >= len(tasks):
		return combinations

	# Include the current task
	combinations += doTasks(tasks, timeToWork, index + 1, currentSum + tasks[index]['duration'], currentCombination + [tasks[index]['name']], depth + 1)

	# Exclude the current task
	combinations += doTasks(tasks, timeToWork, index + 1, currentSum, currentCombination, depth + 1)
	
	dot.render('task_list.gv', view=True)

	return combinations

'''
Recursion in `doTasks`

1. **Base Cases**:
	- The first `if` statement checks if the `currentSum` of task durations equals `timeToWork`. If it does, the current combination of tasks is a valid solution, so it's added to the `combinations` list. Then, the function returns this list.
	- The second `if` statement is another base case that handles two scenarios: 
		- If `currentSum` exceeds `timeToWork`, it means the current combination of tasks is not valid (as it takes more time than allowed), so an empty list is returned.
		- If `index` is equal to or greater than the length of the `tasks` list, it means all tasks have been considered, and no further combinations are possible. In this case, too, an empty list is returned.

	These base cases are essential for stopping the recursion. Without them, the function would keep calling itself indefinitely.

2. **Recursive Calls**:
	- The function makes two recursive calls for each task: one includes the current task (`index`) in the combination, and the other excludes it.
	- **Including the current task**: 
		- It increments `index` by 1 to move to the next task.
		- It adds the `duration` of the current task to `currentSum`.
		- It adds the `name` of the current task to `currentCombination`.
		- The function then calls itself with these updated values.
	- **Excluding the current task**: 
		- It increments `index` by 1 but does not change `currentSum` or `currentCombination`.
		- This represents the scenario where the current task is not part of the combination.
		- Again, the function calls itself with these values.
	- Both these calls explore different paths: one where the task is included in the final combination and one where it's not.

3. **Combining Results**:
	- The results (lists of combinations) from both recursive calls are added together using the `+=` operator. This is how the function aggregates all valid combinations that add up to `timeToWork`.

4. **Return**:
	- Finally, the function returns the `combinations` list, which contains all the valid combinations found through the recursive exploration.

In summary, the recursive part of the `doTasks` function systematically explores all possible ways to combine tasks, so that their total duration matches `timeToWork`. It does this by considering each task both in and out of the combination and then aggregates all valid combinations found during this process.
'''