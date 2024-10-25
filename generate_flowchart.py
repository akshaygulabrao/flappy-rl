from graphviz import Digraph

dot = Digraph(comment='Flow Chart')
dot.attr(rankdir='TB')  # Top to Bottom direction

# Add nodes
dot.node('A', 'Start')
dot.node('B', 'Process 1')
dot.node('C', 'Decision')
dot.node('D', 'Process 2')
dot.node('E', 'End')

# Add edges
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D', 'Yes')
dot.edge('C', 'E', 'No')
dot.edge('D', 'E')

# Save the diagram
dot.render('flowchart', format='png', cleanup=True)
