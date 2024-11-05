import flappy_bird_gymnasium
import gymnasium
import numpy as np
from tqdm import tqdm
from agent import Agent

env = gymnasium.make("FlappyBird-v0",render_mode="human",use_lidar=False,normalize_obs=True)
agent = Agent()

for i in range(1):
    current_obs, _ = env.reset()
    while True:
        state = agent.discretize_state(current_obs)

        action = agent.act(state)
        
        current_obs, reward, terminated, truncated, info = env.step(action)
        
        if terminated:
            break 
env.close()
