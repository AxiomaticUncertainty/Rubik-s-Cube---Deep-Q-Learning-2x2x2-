from keras.models import Sequential
import copy

class cube:
	def __init__(self, state):
		self.state = state

	# face: F = 0, R = 1, B = 2, L = 3, U = 4, D = 5; prime: True, False
	def move(self, face, prime):
		rep = copy.deepcopy(self.state)

		if face == 0:
			if prime == True:
				# rotated face
				print(rep[0][0])
				self.state[0][0] = rep[0][1]
				self.state[0][1] = rep[0][2]
				self.state[0][2] = rep[0][3]
				print(rep[0][0])
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

class nn:
	def __init__(self):
		pass

	def get_model():
		pass

	__call__ = get_model()

if __name__ == '__main__':
	c = cube([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[16,17,18,19],[20,21,22,23]]) # default arrangement, with each sub-list (face) being in the same order as is used for cube.move
	print(c.state)
	c.move(0, True)
	print(c.state)
	c.move(0, False)
	print(c.state)
