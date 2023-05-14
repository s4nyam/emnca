
import random
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)


# board_array = np.zeros((20,20), 'int')


# for i in range (200):
#     randominteger1 = random.randint(1,19)
#     randominteger2 = random.randint(1,19)
#     board_array[randominteger1,randominteger2] = 1

# # print(board_array)    


def blockshaped(arr, nrows, ncols):
    
    h, w = arr.shape
    assert h % nrows == 0, f"{h} rows is not evenly divisible by {nrows}"
    assert w % ncols == 0, f"{w} cols is not evenly divisible by {ncols}"
    return (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(-1, nrows, ncols))

# Return the Hamming distance between string1 and string2.
# string1 and string2 should be the same length.
def hamming_distance(string1, string2): 
    # Start with a distance of zero, and count up
    distance = 0
    # Loop over the indices of the string
    L = len(string1)
    for i in range(L):
        # Add 1 to the distance if these two characters are not equal
        if string1[i] != string2[i]:
            distance += 1
    # Return the final count of differences
    return distance
def Clustering(array):
    # Let us split NxN array to smaller 2x2 blcks
    super_list =  []
    super_list_2020 = []
    hamming_distance_between_superlists = []
    final_board = []
    array = blockshaped(array,2,2)
    for each_sub_array in array:
        super_list.append(list(each_sub_array.flatten()))
    # print(len(super_list))
    for i in range(len(super_list)):
        for j in range(len(super_list)):
            hamming_distance_between_superlists.append(hamming_distance(str(super_list[i]),str(super_list[j])))
    
    modified_board = np.array(hamming_distance_between_superlists)
    shape = int(np.sqrt(len(modified_board)))
    temp_board = modified_board.reshape(shape,shape)
    blockshaped_20_20 = blockshaped(temp_board,5,5)
    for each_sub_array in blockshaped_20_20:
        super_list_2020.append(list(each_sub_array.flatten()))
    # print(super_list_2020[0])
    
    # for eacharray in super_list_2020:
    #     final_board.append(sum(eacharray)/20)

    for eacharray in super_list_2020:
        summa = sum(eacharray)/20
        if(summa >1):
            final_board.append(1)
        else:
            final_board.append(0)
    
    
    final_mod_boaard = np.array(final_board)
    shape = int(np.sqrt(len(final_mod_boaard)))
    # print(shape)
    modified_board2 = final_mod_boaard.reshape(shape,shape)
    return modified_board2

# print(Clustering(board_array))
