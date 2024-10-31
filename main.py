import flappy_bird_gymnasium
import gymnasium
env = gymnasium.make("FlappyBird-v0", render_mode="human",use_lidar=False)

obs, _ = env.reset()
while True:
    # Next action:
    # (feed the observation to your agent here)
    print(obs)
    action = env.action_space.sample()

    # Processing:
    obs, reward, terminated, _, info = env.step(action)
    
    # Checking if the player is still alive
    if terminated:
        break

env.close()

This paper presents an application reinforcement learning agent to play flappy bird and reward the agent for surviving as long as it can. Flappy bird is a simple game where an agent must learn the game's simple flight dynamics in order to avoid a stream of obstacles. The agent receives an environment state at each moment and must choose an action. In this case, the action space is discrete: jump or don't jump. The agent makes sequential decisions in order to maximize its accumulated reward signal throughout the entire simulation while updating its evaluation of the state.

Sequential decision making is formulated as a finite Markov Decision Process (MDPs) [^2]. In an MDP, the agent and environment interact at every timestep. In finite MDPs, theactions, states, and timesteps are all finite. At each timestep $t \in \mathbb{N}$, the agent receives the state $ S_t \in S$ where S is the set of all possible states, and must choose an action $A_t \in A$, where $A$ is the set of all possible actions. Then a simulation can be modeled as a trajectory like: 
$$S_0,A_0,R_1,S_1,A_1,R_2,S_2,A_2,R_3,...$$


<img src="images/chart.png" width="500">




[^1]: [Sutton and Barto](http://incompleteideas.net/book/RLbook2020.pdf)
[^2]: [Sutton and Barto](http://incompleteideas.net/book/RLbook2020.pdf) Chapter 3

At every timestep $t \in \mathbb{N}$