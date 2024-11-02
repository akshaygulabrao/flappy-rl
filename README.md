# Flappy Bird Reinforcement Learning using Tabular Q-Learning

## Introduction
Reinforcement Learning (RL) refers to a general class of algorithms built to explore an environment through trial and error. The algorithm's (agent's) goal is to maximize a reward signal while interacting with its environment sequentially over multiple timesteps. Reinforcement learning formulates the sequential decision making process with a Markov Decision Process (MDP). 

MDPs provide a formal framework to describe agent interaction. This interaction is defined with four components: state, actions, rewards, and transition probabilities. The state space $S$ is the set of all possible situations that an agent can observe. The action space $A$ is the set of all possible actions that an agent can do. The reward function $R$ is a function $R(S,A) \rightarrow \mathbb{R}$ which maps a state $S$ and an action $A$ to a scalar reward $R$. The transition probability $P(S'|S,A)$ is a function of state $S$ and action $A$ that returns the probability of the next state $S'$.


<img src="images/chart.png" width="500" alt="Agent-Environment Interaction">
<p style="text-align: center;">The agent observes the current state of the world and chooses an action. The world then updates the state and returns a reward to the agent indicating whether the action was desirable.</p>

In this paper, I implement Q-Learning in an autonomous learning agent which solves the MDP for the Flappy Bird game. Flappy Bird is a good testbench for Reinforcement Learning algorithms because of its simple game mechanics and finite action space. First, I introduce Markov Decision Processes, the Bellman Equation, and Q-Learning, and then demonstrate how to apply it to flappy bird.

## Background

### Markov Decision Processes
An agent's interaction with the environment can be represented as an MDP trajectory. The agent is initially provided the state $S_0$ and must choose an action $A_0$, from which the world will update $S_1$ and $R_1$ for the agent to learn from. The MDP trajectory is a sequence $M$ where

$$M = S_0,A_0,R_1,S_1,A_1,R_2,S_2,A_2, \ldots$$

where:
- $t \in \mathbb{N}$ is the timestep
- $d$ is the dimension of the world state
- $S_t \in \mathbb{R}^d$ is the state at time $t$
- $A_t \in \mathbb{N}$ is the action at time $t$
- $R_t \in \mathbb{R}$ is the reward at time $t$ for state $(S_{t-1},A_{t-1})$

In my implementation of Flappy Bird, the state space is $S \in \mathbb{R}^d$, where $d$ represents coordinates of the last pipe, the next 2 pipes, the player's position, velocity, and rotation.

Every MDP must satisfy the Markov Property, the next state is only dependent on the state prior to it, not any other states. This means that it is possible to compute the optimal action at any given time using only a single state. If the Markov property was not satisfied, then the transition probabilities would need to be computed with $P(S' | S_t,A_t,S_{t-1}, A_{t-1},...)$ instead of $P(S' | S_t,A_t)$. This would make learning the optimal policy orders of magnitude more expensive.

The goal of each learning algorithm is to solve the MDP by finding an optimal policy. A policy is a decision-making function $\pi$ that maps each state to an action. The optimal policy maximizes the expected reward of all future states. A discount rate $\gamma$ is applied to all future states because future states are less certain than immediate states. The expected reward $G$ at time $t$ is then:

$$G_t \doteq R_t + \sum^\infty_{k=1} \gamma^{k}R_{t+k} = \sum^\infty_{k=0}\gamma^kR_{t+k}$$

The agent can model its expected return by using the quality function $q_\pi(s,a)$, which measures the quality of an action $A_t$ in state $S_t$. The expected reward of each action is then

$$q_\pi(s,a) \doteq \mathbb{E}_\pi[G_t|S_t = s,A_t = a] = \mathbb{E}_\pi[\sum^\infty_{k=0}\gamma^kR_{t+k} | S_t = s,A_t = a]$$

### Bellman Equation
The Bellman Equation approximates the true value of each state and action, which is the sum of the reward and all future rewards in the current state. The state-action value function $q_\pi$ is computed recursively using the Bellman equation to learn the true state-action function $q^*(s,a)$.

$$
\begin{align*}
q_\pi(s,a) &= \mathbb{E}_\pi[G_t|S_t = s,A_t = a] && \text{(definition)}\\
&= \mathbb{E}_\pi[R_t + \gamma G_{t+1} | S_t = s, A_t = a] && \text{(expand $G_t$)}\\
&= \sum_{s'}\sum_{r}p(s',r|s,a)[r + \gamma\mathbb{E}_\pi[G_{t+1}|S_{t+1} = s', A_{t+1} = a']] && \text{(expectation)}\\
&= \sum_{s',r}p(s',r|s,a)[r + \gamma q_\pi(s',a')] && \text{(recursive definition)}
\end{align*}
$$

The Bellman Equation requires knowledge of environment dynamics $P(S',R | S,A)$ and the discounted expected return $G_t$, neither of which is available to the agent. Instead the agent must be able to estimate the values through interacting with the environment.

### Q-Learning
In Q-Learning, instead of learning an optimal policy, the agent instead learns the quality function, and then takes the best action in each state. The agent updates $q_\pi(s,a)$ in real time based on the reward received $R_{t+1}$, the new state $S_{t+1}$, and the value of the state $S_{t+1}$,  assuming that the optimal action is taken $\max_aQ_\pi(S_{t+1}, a)$. Q-learning is an off-policy learning algorithm, meaning it can learn the value of the optimal policy regardless of the agent's thinking behind actions since the next state is only dependent on the previous state and the action. If the agent takes action $A_t$ in state $S_t$ then

$$Q_\pi(S_t,A_t) \leftarrow Q_\pi(S_t,A_t) + \alpha[R_{t+1} + \gamma\max_aQ_\pi(S_{t+1},a) - Q_\pi(S_t,A_t)]$$

where
- $\alpha$ is the step-size used to update each state
- $\gamma$ is the discount rate of future states

## References
Sutton, R. S., & Barto, A. G. (2018). Reinforcement Learning: An Introduction (2nd ed.). MIT Press.