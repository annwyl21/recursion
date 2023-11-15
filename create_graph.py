def create_graph_code(formatted_output):
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
