import gym
import ballbeam_gym
import numpy as np
import matplotlib.pyplot as plt

kwargs = {'timestep': 0.05, 
          'setpoint': 0.0,
          'beam_length': 1.0,
          'max_angle': 0.5,
          'init_velocity': 0.5,
          'max_timesteps': 100,
          'action_mode': 'continuous'}

env = gym.make('BallBeamSetpoint-v0', **kwargs)

Kp = 2.0
Ki = 0.0000001
Kd = 0.8
s = 0.0 
#holds sum of errors

xpoints = np.array([x for x in range(100)])
ypoints = np.empty(100)
#holds ball position which is to be plotted vs time step
ypoints1 = np.empty(100)
#holds beam angle which is to be plotted vs time step

for i_episode in range(3):
    observation = env.reset()
    for t in range(100):
        s = s + (env.bb.x - env.setpoint)
        env.render()
        ypoints[t] = observation[1]   #storing ball position in ypoints array
        ypoints1[t] = observation[0]  #storing beam angle in ypoints array
        theta = Kp*(env.bb.x - env.setpoint) + Ki*(s) + Kd*(env.bb.v) #our action
        observation, reward, done, info = env.step(theta) 
        #step function takes action as argument to give feedback
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
    print(xpoints)
    print(ypoints)
    plt.figure()
    plt.plot(xpoints, ypoints)
    plt.figure()
    plt.plot(xpoints, ypoints1)


env.close()