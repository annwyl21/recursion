import graphviz

dot = graphviz.Graph(comment='Task List', engine='circo')

dot.attr('node', style='filled')

dot.node('1', '6-minutes', color='blue', fillcolor='lightblue', fontsize='28')

dot.node('2', 'Load Washing Machine')
dot.node('3', 'Clean Sink')
dot.node('4', 'Mop Floors')
dot.node('5', 'Hang Laundry')
dot.node('6', 'Wipe Surfaces')
dot.node('7', 'Make Cup of Tea')

dot.node('9', 'Clean Sink', color='blue', fillcolor='lightblue')
dot.edge('2', '9', color='green')
dot.node('2', _attributes={'color': 'blue', 'fillcolor': 'lightblue'})
dot.edge('1', '2', color='green')

dot.node('10', 'Mop Floors', color='grey', fillcolor='lightgrey')
dot.edge('2', '10', color='grey')

dot.node('11', 'Hang Laundry', color='grey', fillcolor='lightgrey')
dot.edge('2', '11', color='grey')

dot.node('12', 'Wipe Surfaces', color='grey', fillcolor='lightgrey')
dot.edge('2', '12', color='grey')

dot.node('13', 'Make Cup of Tea', color='grey', fillcolor='lightgrey')
dot.edge('2', '13', color='grey')


dot.node('14', 'Mop Floors', color='grey', fillcolor='lightgrey')
dot.edge('3', '14', color='grey')

dot.node('15', 'Hang Laundry', color='grey', fillcolor='lightgrey')
dot.edge('3', '15', color='grey')

dot.node('16', 'Wipe Surfaces', color='blue', fillcolor='lightblue')
dot.edge('3', '16', color='green')
dot.node('3', _attributes={'color': 'blue', 'fillcolor': 'lightblue'})
dot.edge('1', '3', color='green')

dot.node('17', 'Make Cup of Tea', color='blue', fillcolor='lightblue')
dot.edge('16', '17', color='green')


dot.node('4', _attributes={'color': 'grey', 'fillcolor': 'lightgrey'})
dot.edge('1', '4', color='grey')


dot.node('18', 'Wipe Surfaces', color='blue', fillcolor='lightblue')
dot.edge('5', '18', color='green')
dot.node('5', _attributes={'color': 'blue', 'fillcolor': 'lightblue'})
dot.edge('1', '5', color='green')

dot.node('19', 'Make Cup of Tea', color='grey', fillcolor='lightgrey')
dot.edge('5', '19', color='grey')


dot.node('20', 'Make Cup of Tea', color='grey', fillcolor='lightgrey')
dot.edge('6', '20', color='grey')
dot.node('6', _attributes={'color': 'grey', 'fillcolor': 'lightgrey'})
dot.edge('1', '6', color='grey')


dot.node('7', _attributes={'color': 'grey', 'fillcolor': 'lightgrey'})
dot.edge('1', '7', color='grey')


dot.render('task_list.gv', view=True)
