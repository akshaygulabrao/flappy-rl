from flappy_bird_gymnasium.envs.constants import (
    BACKGROUND_WIDTH,
    BACKGROUND_HEIGHT,
    BASE_WIDTH,
    FILL_BACKGROUND_COLOR,
    LIDAR_MAX_DISTANCE,
    PIPE_HEIGHT,
    PIPE_VEL_X,
    PIPE_WIDTH,
    PLAYER_ACC_Y,
    PLAYER_FLAP_ACC,
    PLAYER_HEIGHT,
    PLAYER_MAX_VEL_Y,
    PLAYER_PRIVATE_ZONE,
    PLAYER_ROT_THR,
    PLAYER_VEL_ROT,
    PLAYER_WIDTH,
)
import numpy as np
class Agent:
    def __init__(self):
        self.epsilon = 0.1
        self.qtable = np.zeros((2,2),dtype=np.float32)
    
    def discretize_state(self, state):
        last_pipe_x = state[0]
        last_pipe_y_top = state[1]
        last_pipe_y_bottom = state[2]
        next_pipe_x = state[3]
        next_pipe_y_top = state[4]
        next_pipe_y_bottom = state[5]
        next_next_pipe_x = state[6]
        next_next_pipe_y_top = state[7]
        next_next_pipe_y_bottom = state[8]
        player_y = state[9]
        player_vel = state[10]
        player_angle = state[11]

        if last_pipe_x > 0.05:
            if(player_y > last_pipe_y_bottom - (PLAYER_HEIGHT  / BACKGROUND_WIDTH)):
                return 1
            else:
                return 0
        else:
            if(player_y > next_pipe_y_bottom - (PLAYER_HEIGHT  / BACKGROUND_WIDTH)):
                return 1
            else:
                return 0
    
    def act(self, state):
        if np.random.uniform(0, 1) < self.epsilon:
            return np.random.randint(0, 2)
        else:
            return np.argmax(self.qtable[state])
            
    def learn(self, state, action, reward, next_state, terminated):
        if not terminated:
            self.qtable[state][action] = self.qtable[state][action] + 0.1 * (reward + 0.9 * self.qtable[next_state][np.argmax(self.qtable[next_state])] - self.qtable[state][action])
        else:
            self.qtable[state][action] = self.qtable[state][action] + 0.1 * (reward - self.qtable[state][action])
