from gymnasium import make
from stable_baselines3 import DQN, PPO
from gym_vectorvelocity import VectorVelocityEnv

env = make('VectorVelocity-v0', mode="human")

#---------------------------------------------------------------------------------------------------------------------
#model_to_visualize = PPO.load("D:/Uni/Reinforcement_Learning_Vector_Velocity/models/ppo/ppo_vector_velocity")
#model_to_visualize.set_env(env)
#---------------------------------------------------------------------------------------------------------------------
model_to_visualize = DQN.load("D:/Uni/Reinforcement_Learning_Vector_Velocity/models/dqn/dqn_vector_velocity", env=env)
#---------------------------------------------------------------------------------------------------------------------

# Play the saved model for 2000 timesteps
obs = env.reset()[0]
for _ in range(2000):
    action, _states = model_to_visualize.predict(obs, deterministic=True)
    obs, rewards, dones, _, info= env.step(action)
    env.render()