from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
from keras import optimizers
import copy
import random
import numpy as np
import math
import os.path

class cube:
	def __init__(self, state):
		self.state = state

	# face: F = 0, R = 1, B = 2, L = 3, U = 4, D = 5; prime: True, False
	def move(self, face, prime):
		rep = copy.deepcopy(self.state)

		# convoluted methodology by which we rotate a face of the cube
		if face == 0:
			if prime == True:
				# rotated face
				self.state[0][0] = rep[0][1]
				self.state[0][1] = rep[0][2]
				self.state[0][2] = rep[0][3]
				self.state[0][3] = rep[0][0]
				# right face (rel rot)
				self.state[1][0] = rep[5][3]
				self.state[1][3] = rep[5][2]
				# bottom face (rel rot)
				self.state[5][3] = rep[3][2]
				self.state[5][2] = rep[3][1]
				# left face (rel rot)
				self.state[3][2] = rep[4][3]
				self.state[3][1] = rep[4][2]
				# upper face (rel rot)
				self.state[4][3] = rep[1][0]
				self.state[4][2] = rep[1][3]

				return 0
			else:
				# rotated face
				self.state[0][0] = rep[0][3]
				self.state[0][1] = rep[0][0]
				self.state[0][2] = rep[0][1]
				self.state[0][3] = rep[0][2]
				# right face (rel rot)
				self.state[1][0] = rep[4][3]
				self.state[1][3] = rep[4][2]
				# upper face (rel rot)
				self.state[4][3] = rep[3][2]
				self.state[4][2] = rep[3][1]
				# left face (rel rot)
				self.state[3][2] = rep[5][3]
				self.state[3][1] = rep[5][2]
				# bottom face (rel rot)
				self.state[5][3] = rep[1][0]
				self.state[5][2] = rep[1][3]

				return 1
		elif face == 1:
			if prime == True:
				# rotated face
				self.state[1][0] = rep[1][1]
				self.state[1][1] = rep[1][2]
				self.state[1][2] = rep[1][3]
				self.state[1][3] = rep[1][0]
				# right face (rel rot)
				self.state[2][0] = rep[5][0]
				self.state[2][3] = rep[5][3]
				# bottom face (rel rot)
				self.state[5][0] = rep[0][2]
				self.state[5][3] = rep[0][1]
				# left face (rel rot)
				self.state[0][2] = rep[4][2]
				self.state[0][1] = rep[4][1]
				# upper face (rel rot)
				self.state[4][2] = rep[2][0]
				self.state[4][1] = rep[2][3]

				return 2
			else:
				# rotated face
				self.state[1][0] = rep[1][3]
				self.state[1][1] = rep[1][0]
				self.state[1][2] = rep[1][1]
				self.state[1][3] = rep[1][2]
				# right face (rel rot)
				self.state[2][0] = rep[4][2]
				self.state[2][3] = rep[4][1]
				# upper face (rel rot)
				self.state[4][2] = rep[0][2]
				self.state[4][1] = rep[0][1]
				# left face (rel rot)
				self.state[0][2] = rep[5][0]
				self.state[0][1] = rep[5][3]
				# bottom face (rel rot)
				self.state[5][0] = rep[2][0]
				self.state[5][3] = rep[2][3]

				return 3
		elif face == 2:
			if prime == True:
				# rotated face
				self.state[2][0] = rep[2][1]
				self.state[2][1] = rep[2][2]
				self.state[2][2] = rep[2][3]
				self.state[2][3] = rep[2][0]
				# right face (rel rot)
				self.state[3][0] = rep[5][1]
				self.state[3][3] = rep[5][0]
				# bottom face (rel rot)
				self.state[5][1] = rep[1][2]
				self.state[5][0] = rep[1][1]
				# left face (rel rot)
				self.state[1][2] = rep[4][1]
				self.state[1][1] = rep[4][0]
				# upper face (rel rot)
				self.state[4][1] = rep[3][0]
				self.state[4][0] = rep[3][3]

				return 4
			else:
				# rotated face
				self.state[2][0] = rep[2][3]
				self.state[2][1] = rep[2][0]
				self.state[2][2] = rep[2][1]
				self.state[2][3] = rep[2][2]
				# right face (rel rot)
				self.state[3][0] = rep[4][1]
				self.state[3][3] = rep[4][0]
				# upper face (rel rot)
				self.state[4][1] = rep[1][2]
				self.state[4][0] = rep[1][1]
				# left face (rel rot)
				self.state[1][2] = rep[5][1]
				self.state[1][1] = rep[5][0]
				# bottom face (rel rot)
				self.state[5][1] = rep[3][0]
				self.state[5][0] = rep[3][3]

				return 5
		elif face == 3:
			if prime == True:
				# rotated face
				self.state[3][0] = rep[3][1]
				self.state[3][1] = rep[3][2]
				self.state[3][2] = rep[3][3]
				self.state[3][3] = rep[3][0]
				# right face (rel rot)
				self.state[0][0] = rep[5][2]
				self.state[0][3] = rep[5][1]
				# bottom face (rel rot)
				self.state[5][2] = rep[2][2]
				self.state[5][1] = rep[2][1]
				# left face (rel rot)
				self.state[2][2] = rep[4][0]
				self.state[2][1] = rep[4][3]
				# upper face (rel rot)
				self.state[4][0] = rep[0][0]
				self.state[4][3] = rep[0][3]

				return 6
			else:
				# rotated face
				self.state[3][0] = rep[3][3]
				self.state[3][1] = rep[3][0]
				self.state[3][2] = rep[3][1]
				self.state[3][3] = rep[3][2]
				# right face (rel rot)
				self.state[0][0] = rep[4][0]
				self.state[0][3] = rep[4][3]
				# upper face (rel rot)
				self.state[4][0] = rep[2][2]
				self.state[4][3] = rep[2][1]
				# left face (rel rot)
				self.state[2][2] = rep[5][2]
				self.state[2][1] = rep[5][1]
				# bottom face (rel rot)
				self.state[5][2] = rep[0][0]
				self.state[5][1] = rep[0][3]

				return 7
		elif face == 4:
			if prime == True:
				# rotated face
				self.state[4][0] = rep[4][1]
				self.state[4][1] = rep[4][2]
				self.state[4][2] = rep[4][3]
				self.state[4][3] = rep[4][0]
				# right face (rel rot)
				self.state[1][1] = rep[0][1]
				self.state[1][0] = rep[0][0]
				# bottom face (rel rot)
				self.state[0][1] = rep[3][1]
				self.state[0][0] = rep[3][0]
				# left face (rel rot)
				self.state[3][1] = rep[2][1]
				self.state[3][0] = rep[2][0]
				# upper face (rel rot)
				self.state[2][1] = rep[1][1]
				self.state[2][0] = rep[1][0]

				return 8
			else:
				# rotated face
				self.state[4][0] = rep[4][3]
				self.state[4][1] = rep[4][0]
				self.state[4][2] = rep[4][1]
				self.state[4][3] = rep[4][2]
				# right face (rel rot)
				self.state[1][1] = rep[2][1]
				self.state[1][0] = rep[2][0]
				# upper face (rel rot)
				self.state[2][1] = rep[3][1]
				self.state[2][0] = rep[3][0]
				# left face (rel rot)
				self.state[3][1] = rep[0][1]
				self.state[3][0] = rep[0][0]
				# bottom face (rel rot)
				self.state[0][1] = rep[1][1]
				self.state[0][0] = rep[1][0]

				return 9
		elif face == 5:
			if prime == True:
				# rotated face
				self.state[5][0] = rep[5][1]
				self.state[5][1] = rep[5][2]
				self.state[5][2] = rep[5][3]
				self.state[5][3] = rep[5][0]
				# right face (rel rot)
				self.state[3][3] = rep[0][3]
				self.state[3][2] = rep[0][2]
				# bottom face (rel rot)
				self.state[0][3] = rep[1][3]
				self.state[0][2] = rep[1][2]
				# left face (rel rot)
				self.state[1][3] = rep[2][3]
				self.state[1][2] = rep[2][2]
				# upper face (rel rot)
				self.state[2][3] = rep[3][3]
				self.state[2][2] = rep[3][2]

				return 10
			else:
				# rotated face
				self.state[5][0] = rep[5][3]
				self.state[5][1] = rep[5][0]
				self.state[5][2] = rep[5][1]
				self.state[5][3] = rep[5][2]
				# right face (rel rot)
				self.state[3][3] = rep[2][3]
				self.state[3][2] = rep[2][2]
				# upper face (rel rot)
				self.state[2][3] = rep[1][3]
				self.state[2][2] = rep[1][2]
				# left face (rel rot)
				self.state[1][3] = rep[0][3]
				self.state[1][2] = rep[0][2]
				# bottom face (rel rot)
				self.state[0][3] = rep[3][3]
				self.state[0][2] = rep[3][2]

				return 11

	# for 'num' times, make random moves in order to scramble the cube
	def scramble(self, num):
		for n in range(0, num):
			sm = self.move(random.randint(0, 5), random.choice([True, False]))

		return sm

	# TODO - add one-hot encoding 'get' method in for network inputs
	def one_hot(self):
		oh_state = []
		for side in self.state:
			for sticker in side:
				oh = np.zeros(24)
				oh[(self.state.index(side)*4 - 1) + side.index(sticker)] = 1
				oh_state.extend(oh.copy())
		return oh_state

	def colorize(self):
		c_state = []
		for side in self.state:
			c_side = []
			for sticker in side:
				if sticker < 4:
					c_side.append('o')
				elif sticker < 8:
					c_side.append('g')
				elif sticker < 12:
					c_side.append('r')
				elif sticker < 16:
					c_side.append('b')
				elif sticker < 20:
					c_side.append('w')
				else:
					c_side.append('y')
			c_state.append(c_side.copy())
		return c_state

	def is_solved(self):
		col = self.colorize()
		# check for all stickers of a color being on the same side
		for side in col:
			if not (side[0] == side[1] == side[2] == side[3]):
				return False
		return True

class nn:
	def __init__(self):
		self.create_model()

	def create_model(self):
		if os.path.isfile('rubiks_rl.h5'):
			print('Model found! Loading...')
			self.model = load_model('rubiks_rl.h5')
		else:
			self.model = Sequential()
			self.model.add(Dense(units=2000, activation='tanh', input_dim=576, kernel_initializer='random_uniform', bias_initializer='zeros'))
			self.model.add(Dense(units=3500, activation='tanh', kernel_initializer='random_uniform', bias_initializer='zeros'))
			self.model.add(Dense(units=4700, activation='tanh', kernel_initializer='random_uniform', bias_initializer='zeros'))
			self.model.add(Dense(units=3000, activation='tanh', kernel_initializer='random_uniform', bias_initializer='zeros'))
			self.model.add(Dense(units=1200, activation='tanh', kernel_initializer='random_uniform', bias_initializer='zeros'))
			self.model.add(Dense(units=300, activation='tanh', kernel_initializer='random_uniform', bias_initializer='zeros'))
			self.model.add(Dense(units=12, activation='sigmoid', kernel_initializer='random_uniform', bias_initializer='zeros'))
			self.model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

	def __call__(self):
		return self.model

	def preprocess(self, game, discount):
		processed_out = []

		for l in range(0, len(game)):
			processed_out.append(np.asarray(game[l])*(discount**(len(game) - l - 1))) # reward dep

		return processed_out

	def train(self, games, e_greedy, epochs, discount):
		instance = cube([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[16,17,18,19],[20,21,22,23]])

		long_states = []
		long_actions = []

		for i in range(games):
			states = []
			actions = []

			counter = 0

			instance.scramble(30)

			while not instance.is_solved():
				states.append(instance.one_hot())

				if random.uniform(0, 1) <= e_greedy:
					sampled = instance.scramble(1)
					act = np.zeros(12)
					act[sampled] = 1
				else:
					pre = self.model.predict(np.asarray([instance.one_hot()]))[0]
					best = np.argmax(pre)
					act = np.zeros(12)
					instance.move(math.floor(best / 2), bool(best % 2))
					act[best] = 1

				actions.append(act)

				counter += 1

				if counter % 10000 == 0:
					print(counter)
					print(len(states))

				if len(states) == 50000:
					states = states[25000:]
					actions = actions[25000:]

			long_states.extend(copy.deepcopy(states))
			long_actions.extend(copy.deepcopy(self.preprocess(actions, discount)))

		'''zipped = list(zip(long_states, long_actions))
		zipped = random.shuffle(zipped)
		long_states, long_actions = zip(*zipped)'''

		self.model.fit(np.asarray(long_states), np.asarray(long_actions), batch_size=len(long_states), epochs=10)

		self.model.save('rubiks_rl.h5')

if __name__ == '__main__':
	network = nn()
	while True:
		network.train(1, 1, 10, .97)
