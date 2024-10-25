from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='Flow Chart')

# Set direction to Left-to-Right
dot.attr(rankdir='LR')  # Set direction to Left-to-Right

# Set DPI and size for web viewing
dot.attr(dpi='150')  # Lower DPI for web viewing
dot.attr(size='10.5,4!')  # Width of ~850px at 150 DPI, height of ~400px, ! forces size

# Optional: Add some margin and style improvements
dot.attr(margin='0.5')
# dot.attr(splines='ortho')  # Makes edges cleaner with right angles
dot.attr(nodesep='0.5')    # Space between nodes
dot.attr(ranksep='0.5')    # Space between ranks

# Add nodes
dot.node('state', 'State')
dot.node('reward/next state', 'Reward/ Next State')
dot.node('done', 'Done')
dot.node('agent action', 'Agent Action')

# Add edges
dot.edge('agent action', 'reward/next state')
dot.edge('state','reward/next state')
dot.edge('state','agent action')
dot.edge('reward/next state', 'state','if alive')
dot.edge('reward/next state', 'done', 'if dead')

# Render with specific DPI
dot.render('images/flowchart', format='png', cleanup=True, 
          renderer='cairo')  # Remove formatter parameter
