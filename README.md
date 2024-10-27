# Flappy Bird Reinforcement Learning
 The idea behind this project is to create a bot that can play flappy bird.[^1] The bot interacts with the world similarly to how a human would play a video game. There are timesteps that happen at very quick intervals. At each interval, the bot gets too choose which move to make given the state of the world. It's actions impact the state of the world. 

![Image](images/chart.png)

In this flappy bird game, the state updates are going to happen approximately every 1/30th of a second (aka the framerate) and the agent is responsible for making decisions at each one of thise timeframes. The state is  measured characteristics like altitude, velocity, distance to next pipe, gap between pipes. The agent is then responsible for answering "Given the state, it is better to jump or not to jump?". The math way of saying this used in popular RL literature like [Sutton and Barto](http://incompleteideas.net/book/RLbook2020.pdf) is 

$$
S = \in \mathbb{R}^{n}\\
A = \in  \{0,1\}\\s
(S,A) \rightarrow (S', R)
$$

Now the agent is responsible for deciding on a state based on the action. In other words the agent is a function $Q$ such that

$$
Q(S) = A
$$



[^1]: A continuation of a project that I started a few years ago. Let's see if I can find the src. It turns out I had a deleting phase of my life where I deleted all of my repositories because I thought I would never come back to this project. Time to start over. The good news is that I lost the code, but not the knowledge.