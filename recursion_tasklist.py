# Casidoo - Given a list of tasks, where each task has a duration, and a limited amount of available time to work, write a function to return the tasks that can be completed within the given time, without re-ordering the original list of tasks.

# RELEVANT EXAMPLE OF RECURSION

tasks = [
  { 'name': 'Load Washing Machine', 'duration': 4 },
  { 'name': 'Clean Sink', 'duration': 2 },
  { 'name': 'Mop Floors', 'duration': 7 },
  { 'name': 'Hang Laundry', 'duration': 5 },
  { 'name': 'Wipe Surfaces', 'duration': 1 },
  { 'name': 'Make Cup of Tea', 'duration': 3 },
  { 'name': 'Make Cup of Coffee', 'duration': 3 }
]

timeToWork = 6

def doTasks(tasks, timeToWork, index=0, currentSum=0, currentCombination=[], depth=0):
    # Indentation based on recursion depth
    indent = "  " * depth  
    # print(f"{indent}doTasks(index={index}, currentSum={currentSum}, currentCombination={currentCombination})")
    if currentSum > timeToWork:
         print(f"{indent}{currentCombination}, {currentSum} minutes (too long)")
    else:
         print(f"{indent}{currentCombination})")

    # Initialize a list to store combinations
    combinations = []

    # If the current sum equals the target time, add the current combination to the list of combinations.
    if currentSum == timeToWork:
        # print(f"{indent}Found combination: {currentCombination}")
        print(f"\n{indent}Found combination: {currentCombination}, {timeToWork} minutes\n")
        combinations.append(currentCombination)
        return combinations

    # If the sum exceeds the target time or no more tasks are left, return an empty list (base case).
    if currentSum > timeToWork or index >= len(tasks):
        return combinations

    # Include the current task
    combinations += doTasks(tasks, timeToWork, index + 1, currentSum + tasks[index]['duration'], currentCombination + [tasks[index]['name']], depth + 1)

    # Exclude the current task
    combinations += doTasks(tasks, timeToWork, index + 1, currentSum, currentCombination, depth + 1)

    return combinations

# To get the desired output format
def formatOutput(combinations):
    output = {}
    for i, combo in enumerate(combinations, 1):
        output[i] = combo
    return output

combinations = doTasks(tasks, timeToWork=6)
formatted_output = formatOutput(combinations)
print(formatted_output)
# {1: ['Task 1', 'Task 2'], 2: ['Task 4', 'Task 5'], 3: ['Task 2', 'Task 5', 'Task 6']}

# Use the formatted output to generate the Graphviz code
# Initialize parts of the Graphviz code
nodes = []
edges = []

# Process the dictionary to create nodes and edges
for key, tasklist in formatted_output.items():
    option = 'Option ' + str(key)
    nodes.append(f'\"{option}\" [color=yellow, style=filled, shape=rectangle]')
    for value in tasklist:
        edges.append(f'\"{option}\" -- \"{value}\"')

# Combine everything into the final Graphviz code
graphviz_code = "graph G {\n\t" + "\n\t".join(nodes + edges) + "\n}"

# Create a file with the Graphviz code
with open('outfile.gv', 'w') as f:
    f.write(graphviz_code)

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

# Co-pilot solution is superb with its use of lambda as a sorting key however, it only offers 1 selection of tasks.  I wanted to see if I could get all the tasks that could be completed within the given time.
def doTasksCP(tasks, timeToWork):
	tasks.sort(key=lambda x: x['duration'])
	completedTasks = []
	for task in tasks:
		if timeToWork - task['duration'] >= 0:
			completedTasks.append(task['name'])
			timeToWork -= task['duration']
	return completedTasks

print(doTasksCP(tasks, timeToWork=6))
# ['Task 2', 'Task 5', 'Task 6']