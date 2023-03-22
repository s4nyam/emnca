import numpy as np
w = 100
h = 100
# initial mask
CA_STEPS = 50
mat = 'border'
board_arr = []
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



def cellularautomata(B,S):
    for i in range(CA_STEPS):
        # Evolve CA
        initial_mat = start_state(w, h, state=mat)
        neighbors=0
        next_state=0
        my_cells=[initial_mat[i, j] for i in range(w) for j in range(h)]
        cells_arr = np.asarray(my_cells).reshape(w, h)
        for i in range(w):
            for j in range(h):
                current_state = cells_arr[i,j]
                i_minus = i - 1
                if i_minus < 0:
                    i_minus = w - 1

                i_plus = i + 1
                if i_plus > w - 1:
                    i_plus = 0

                j_minus = j - 1
                if j_minus < 0:
                    j_minus = h - 1

                j_plus = j + 1
                if j_plus > h - 1:
                    j_plus = 0

                topLeft = cells_arr[i_minus][j_minus]
                topCenter = cells_arr[i][j_minus]
                topRight = cells_arr[i_plus][j_minus]
                midLeft = cells_arr[i_minus][j]
                midRight = cells_arr[i_plus][j]
                bottomLeft = cells_arr[i_minus][j_plus]
                bottomCenter = cells_arr[i][j_plus]
                bottomRight = cells_arr[i_plus][j_plus]

                sum = int(topLeft + topCenter + topRight + midLeft \
                        + midRight + bottomLeft + bottomCenter + bottomRight)

                neighbors = sum
                for k in range(len(B)):
                    if(current_state == 0 and neighbors == B[k]):
                        next_state = 1
                        cells_arr[i][j] = 1
                    
                for l in range(len(S)):
                    if(current_state == 1 and neighbors == S[l]):
                        next_state = 1
                        cells_arr[i][j] = 2
                if(neighbors not in B+S):
                    cells_arr[i][j] = 0    
        current_state_mat = [[cells_arr[i][j] for i in range(w)] for j in range(h)]
        arr = current_state_mat
        # Store and Append Board Array
        board_arr.append(arr)


    # Calculate Deflate over that board array
    import os
    try:
        os.remove("board_arrays.txt")
        # print("Removed Successfully")
    except:
        pass
    with open("board_arrays.txt", "w") as output:
        output.write(str(board_arr))
    import deflate
    filedata = open('board_arrays.txt', "rb").readline()
    compressed = deflate.gzip_compress(filedata, 6)
    deflate_value = compressed.__sizeof__()
    return deflate_value



# B = [1,3,5,7]
# S = [1,3,5,7]
# print(cellularautomata(B,S))