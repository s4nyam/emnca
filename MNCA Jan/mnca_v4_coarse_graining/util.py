import numpy as np
import random
# from EC import Born
# from EC import Survive


B = [5,6,5]
S = [4,4,8,1,5,6,8]


class Cells(object):
    def __init__(self, current_state, neighbors, next_state):
        self.current_state = current_state
        self.neighbors = neighbors
        self.next_state = next_state

    def maze(self):
        if self.current_state == 1 and (self.neighbors <= 4):
            self.next_state = 1
        elif self.current_state == 0 and (self.neighbors == 3):
            self.next_state = 1
        else:
            self.next_state = 0

    def walled(self):
        if self.current_state == 1 and (2 <= self.neighbors <= 5):
            self.next_state = 1
        elif self.current_state == 0 and (4 <= self.neighbors <= 7):
            self.next_state = 1
        else:
            self.next_state = 0

    def life(self):
        # game of life good stuff with cross or random (B3/S23)
        if self.current_state == 0 and self.neighbors == 3:
            self.next_state = 1
        elif self.current_state == 1 and (self.neighbors == 2 or self.neighbors == 3):
            self.next_state = 1
        else:
            self.next_state = 0

    def high_life(self):
        if self.current_state == 1 and (self.neighbors == 2 or self.neighbors == 3):
            self.next_state = 1
        elif self.current_state == 0 and (self.neighbors == 3 or self.neighbors == 6):
            self.next_state = 1
        else:
            self.next_state = 0

    def spots(self):
        if self.current_state == 1 and (self.neighbors == 2 or self.neighbors == 3):
            self.next_state = 1
        elif self.current_state == 0 and (self.neighbors == 1):
            self.next_state = 1
        else:
            self.next_state = 0

    def lsd(self):
        if self.current_state == 1 and (self.neighbors == 1 or self.neighbors == 2 or self.neighbors == 5):
            self.next_state = 1
        elif self.current_state == 0 and (self.neighbors == 3 or self.neighbors == 6):
            self.next_state = 1
        else:
            self.next_state = 0

    def move(self):
        if self.current_state == 1 and (5 >= self.neighbors >= 3):
            self.next_state = 1
        elif self.current_state == 0 and (self.neighbors == 3 or self.neighbors == 6 or self.neighbors == 8):
            self.next_state = 1
        else:
            self.next_state = 0

    def rand_choice(self):
        if self.current_state == 1 and (self.neighbors < 3 or self.neighbors > 2):
            self.next_state = 0
        elif self.current_state == 0 and (self.neighbors != 2):
            self.next_state = 0
        else:
            self.next_state = 1

    def replicator(self):
        if self.current_state == 1 and (self.neighbors == 1 or self.neighbors == 3 or self.neighbors == 5 or self.neighbors == 7):
            self.next_state = 1
        elif self.current_state == 0 and (self.neighbors == 1 or self.neighbors == 3 or self.neighbors == 5 or self.neighbors == 7):
            self.next_state = 1
        else:
            self.next_state = 0

    def update_states(self):
        self.current_state = self.next_state
        # return self
    

    def EC_rule(self):
        
        # print("B: ",B)
        # print("S: ",S)
        for i in range(len(B)):
            if(self.current_state == 0 and self.neighbors == B[i]):
                self.next_state = 1
            
        for i in range(len(S)):
            if(self.current_state == 1 and self.neighbors == S[i]):
                self.next_state = 1
        if(self.neighbors not in B+S):
            self.next_state = 0
        

ca = Cells


def start_state(w, h, state):

    if state == 'diag':
        A = np.zeros((w, h))
        A[:, 0] = 1
        A[0, :] = 1
        A[:, -1] = 1
        A[-1, :] = 1
        np.fill_diagonal(A, 1)
        return A
    if state == 'border':
        B = np.zeros((w, h), dtype=int)
        B[1:-1, 1:-1] = 1
        return B
    elif state == 'cross':
        A = np.eye(w, dtype=int)
        B = np.rot90(A).copy()
        C = np.array(A + B)
        return C
    elif state == 'rand':
        return np.random.randint(0, 2, (w, h))
    elif state == 'N':
        N = np.zeros((w, h))
        N[:, 0] = 1
        N[:, -1] = 1
        np.fill_diagonal(N, 1)
        return N
    elif state == 'Z':
        Z = np.zeros((w, h))
        Z[:, 0] = 1
        Z[:, -1] = 1
        np.fill_diagonal(Z, 1)
        Z = np.rot90(Z)
        return Z
    else:
        print('wrong dimensions')


def initialize(w, h, mat):
    initial_mat = start_state(w, h, state=mat)
    my_cells = [ca(current_state=initial_mat[i, j], neighbors=0, next_state=0)
                for i in range(w) for j in range(h)]
    cells_arr = np.asarray(my_cells).reshape(w, h)
    return cells_arr
