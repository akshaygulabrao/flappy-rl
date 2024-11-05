import flappy_bird_gymnasium
import gymnasium
import numpy as np
from tqdm import tqdm
from agent import Agent

env = gymnasium.make("FlappyBird-v0",render_mode="human",use_lidar=False,normalize_obs=True)
agent = Agent()

for i in range(100):
    current_obs, _ = env.reset()
    if (i+1) % 5 == 0:
        print(f"Episode {i+1}")

    while True:
        state = agent.discretize_state(current_obs)

        action = agent.act(state)

        next_obs, reward, terminated, truncated, info = env.step(action)
        next_state = agent.discretize_state(next_obs)
        agent.learn(state, action, reward, next_state, terminated)
        
        if terminated:
            break 
        current_obs = next_obs
env.close()
