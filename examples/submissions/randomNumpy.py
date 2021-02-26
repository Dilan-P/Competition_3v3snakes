import numpy as np
import random

def selectActionRandom(action_space):
  # Create empty matrix of size (num_player_actions, action_options)
  player_action = np.zeros(shape=(1, action_space[0].n))

  # Select a random option from the action space
  selected_action = random.randint(0, action_space[0].n - 1)

  # Add the selected action to the player_action
  player_action[0, selected_action] = 1

  return player_action

def my_controller(observation_list, action_space_list, is_act_continuous):
    num_agents = len(observation_list)

    joint_action = np.array([selectActionRandom(action_space_list[i]) for i in range(num_agents)])

    joint_action = joint_action.tolist()

    return joint_action