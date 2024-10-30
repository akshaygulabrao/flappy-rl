# Flappy Bird Reinforcement Learning

Reinforcment learning(RL) is a subset of machine learning where a decision-making algorithm (agent) lives in a simulation and learns how to maximize a scalar reward signal. The scalar reward is continuously fed to the agent as it makes decisions through the simulation. The agent is able to replay the simulation multiple times and can collect data to improves its decision making iteratively over multiple runs.

 In this project, I create an reinforcement learning agent that can play flappy bird[^1]. Flappy bird is an extremely simple game where the objective is to control when a bird "flaps" its wings and flies in the air. The bird must flap it's wings often enough that it doesn't fall down, but not so often that it goes off screen and hits the ceiling. 
 
 The bot interacts with the world similarly to how a human would play a video game. There are timesteps that happen at very quick intervals. At each interval, the bot gets too choose which move to make given the state of the world. It's actions impact the state of the world, and the rewards that it receives. 

<img src="images/chart.png" width="500">

In this flappy bird game, the state updates are going to happen approximately every 1/30th of a second (aka the framerate) and the agent is responsible for making decisions at each one of thise timeframes. The state is  measured characteristics like altitude, velocity, distance to next pipe, gap between pipes. The agent is then responsible for answering "Given the state, it is better to jump or not to jump?". The math way of saying this used in popular RL literature like [Sutton and Barto](http://incompleteideas.net/book/RLbook2020.pdf) is 

$$
S = \in \mathbb{R}^{n}\\
A = \in  \{0,1\}\\
(S,A) \rightarrow (S', R)
$$

Now the agent is responsible for deciding on a state based on the action. In other words the agent is a function $Q$ such that

$$
Q(S) = A
$$



[^1]: A continuation of a project that I started a few years ago. Let's see if I can find the src. It turns out I had a deleting phase of my life where I deleted all of my repositories because I thought I would never come back to this project. Time to start over. The good news is that I lost the code, but not the knowledge.