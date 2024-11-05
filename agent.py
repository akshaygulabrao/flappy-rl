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
class Agent:
    def __init__(self):
        pass
    
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
        print(f"last_pipe_x: {last_pipe_x}, next_pipe_x: {next_pipe_x},\
               player_y: {player_y}, last_pipe_y_bottom: {last_pipe_y_bottom}")

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
        if state == 1:
            return 1
        else:
            return 0
        
    def learn(self, state, action, reward, next_state, terminated):
        pass