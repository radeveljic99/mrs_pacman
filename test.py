import gym

env = gym.make('LunarLander-v2')

env.reset()

for step in range(200):
    env.render()
    env.step(env.action_space.sample())

env.close()    

