from cgitb import small
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
    count=0
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

                sum_neigh = int(topLeft + topCenter + topRight + midLeft \
                        + midRight + bottomLeft + bottomCenter + bottomRight)

                neighbors = sum_neigh
                for k in range(len(B)):
                    if(current_state == 0 and neighbors == B[k]):
                        next_state = 1
                        cells_arr[i][j] = 1
                    
                for l in range(len(S)):
                    if(current_state == 1 and neighbors == S[l]):
                        next_state = 1
                        cells_arr[i][j] = 1
                if(neighbors not in B+S):
                    cells_arr[i][j] = 0    
        current_state_mat = [[cells_arr[i][j] for i in range(w)] for j in range(h)]
        arr = current_state_mat
        # Store and Append Board Array
        # board_arr.append(arr) - 
        # INTRODUCING TIME DELTA
        count=count+1
        time_delta = np.random.randint(1,10)
        if(count%time_delta==0):
            board_arr.append(arr)


    
    
    # Joint Compression is difficult to apply because it is time taking for 2D CA, 
    # thats why just applying for some grids in time delta steps


    # MU = C(1)+C(2)+...+C(n-1) / C(1||2||3||...||n-1)

    for small_board  in range(len(board_arr)):
        with open("small_board"+str(small_board)+".txt", "w") as output1:
            output1.write(str(board_arr[small_board]))

    import deflate
    individual_board_deflates = []
    for eachfile_board in range(len(board_arr)):
        filedata_board = open("small_board"+str(eachfile_board)+".txt", "rb").readline()
        compressed_value_board = deflate.gzip_compress(filedata_board, 6)
        df_value_board = compressed_value_board.__sizeof__()
        individual_board_deflates.append(df_value_board)

    with open("full_board_arrays.txt", "w") as output2:
        output2.write(str(board_arr))
    filedata = open('full_board_arrays.txt', "rb").readline()
    compressed = deflate.gzip_compress(filedata, 12)
    deflate_value_full = compressed.__sizeof__()
    import os
    os.system("rm *.txt")
    mu = sum(individual_board_deflates)/deflate_value_full
    return mu*1000000000000000



# B = [3]
# S = [2,3]
# print(cellularautomata(B,S))