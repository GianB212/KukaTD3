import gym
import numpy as np
from td3_torch import Agent
import matplotlib.pyplot as plt

def plot_learning_curve(scores, x, figure_file):
    running_avg = np.zeros(len(scores))
    for i in range(len(running_avg)):
        running_avg[i] = np.mean(scores[max(0, i-100):(i+1)])
    plt.plot(x, running_avg)
    plt.title('Running average of previous 100 scores')
    plt.savefig(figure_file)

if __name__ == '__main__':
    env = gym.make('BipedalWalker-v2')
    agent = Agent(alpha=0.001, beta=0.001, input_dims=env.observation_space.shape, tau=0.005, env=env, batch_size=100, layer1_size=400, layer2_size=300, n_actions=env.action_space.shape[0])
    n_games = 1500
    filename = 'Walker2d_' + str(n_games) + '.png'
    figure_file = 'plots/' + filename

    best_score = env.reward_range[0]
    score_history = []

    agent.load_models()

    for i in range(n_games):
        observation = env.reset()
        done = False
        score = 0
        while not done:
            action = agent.choose_action(observation)
            observation_, reward, done, info = env.step(action)
            agent.remember(observation, action, reward, observation_, done)
            agent.learn()
            score += reward
            observation = observation_
            env.render()
        score_history.append(score)
        avg_score = np.mean(score_history[-100:])

        if avg_score > best_score:
            best_score = avg_score
            agent.save_models()

        print('episode ', i, 'score %.2f' %score, ' average score %.3f' %avg_score)
    x = [i+1 for i in range(n_games)]
    plot_learning_curve(score_history, x, figure_file)

