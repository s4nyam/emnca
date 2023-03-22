
import random
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)


# board_array = np.zeros((100,100), 'int')


# for i in range (5000):
#     randominteger1 = random.randint(1,99)
#     randominteger2 = random.randint(1,99)
#     board_array[randominteger1,randominteger2] = 1

# print(board_array)    
def blockshaped(arr, nrows, ncols):
    
    h, w = arr.shape
    assert h % nrows == 0, f"{h} rows is not evenly divisible by {nrows}"
    assert w % ncols == 0, f"{w} cols is not evenly divisible by {ncols}"
    return (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(-1, nrows, ncols))


def FrequencyHistogram(array):
    # Let us split NxN array to smaller 2x2 blcks
    super_list =  []
    probabilities = []
    threshold1 = 0.03
    threshold2 = 0.06
    array = blockshaped(array,2,2)
    for each_sub_array in array:
        super_list.append(list(each_sub_array.flatten()))
    for i in range(len(super_list)):
        count = 0
        for j in range(len(super_list)):
            if(super_list[i]==super_list[j]):
                count = count+1
        probabilities.append(count/len(super_list))
    for i in range(len(probabilities)):
        if(probabilities[i] < threshold1):
            probabilities[i] = 8
        elif(probabilities[i] >= threshold1 and probabilities[i] < threshold2):
            probabilities[i] = 2
        else:
            probabilities[i] = 0
            
    modified_board = np.array(probabilities)
    shape = int(np.sqrt(len(probabilities)))
    # print(shape)
    modified_board = modified_board.reshape(shape,shape)
    return modified_board

# print(FrequencyHistogram(board_array))
