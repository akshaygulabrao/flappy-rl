from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='Flow Chart')

# Set DPI and size
dot.attr(dpi='300')
# Optional: Set size in inches (width,height)
dot.attr(size='8.5,11')  # Letter size paper

# Add nodes
dot.node('state', 'State')
dot.node('reward/next state', 'Reward/ Next State')
dot.node('next state', 'Next State')
dot.node('done', 'Done')

# Add edges
dot.edge('agent action', 'reward/next state')
dot.edge('state','reward/next state')
dot.edge('state','agent action')
dot.edge('reward/next state', 'next state')
dot.edge('next state', 'state','if alive')
dot.edge('next state', 'done', 'if dead')

# Render with specific DPI
dot.render('flowchart', format='png', cleanup=True, 
          renderer='cairo')  # Remove formatter parameter
