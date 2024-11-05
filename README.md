# Reinforcement Learning with Flappy Bird
One of the long-standing challenges of computers is the ability to learn from experience. Reinforcement learning (RL) is a field of artificial intelligence that aims to teach computers how to learn by placing them in interactive environments. The computer program (agent) observes the state of an environment and then chooses an action. As a result, the state changes, and the environment informs the agent whether the behavior was optimal through a numerical reward signal. The agent interacts with the environment numerous times to correlate states, actions, and rewards with each other. Ultimately, the agent finds an optimal policy to maximize the cumulative reward over time.

Flappy Bird is a mobile game from 2013 where the user controls a bird to dodge a stream of static obstacles. The bird naturally falls, so the user must balance flight dynamics with obstacle avoidance to periodically "flap" its wings, providing the bird with a burst of acceleration.
![Flappy Bird](/images/flappy.png)

The agent can learn how to recognize the state of the bird and determine optimal flapping times using an RL algorithm known as Q-Learning. Introduced by Watkins in 1989, Q-Learning enables the agent to leverage previous experiences to choose the best action.

Here, I implement Q-Learning for Flappy Bird using the open-source library Gymnasium and the environment created by Luptakova et al.