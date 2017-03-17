import numpy as np
import random
from queue import *
import datetime
from collections import namedtuple

faces = np.array([1,4,5,6,7,9])
def zero_test(cube3D,faces):
    goal=np.zeros((12,3,3))
    checker = 1
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if cube3D[faces[i], j, k] != goal[faces[i], j, k]:
                    checker = 0
                    return checker

    return checker

def goal_test(cube3D,faces,goal):
    checker = 1
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if cube3D[faces[i], j, k] != goal[faces[i], j, k]:
                    checker = 0
                    return checker

    return checker

def create_sudoku_cube(numbers,faces):
    cube3D = np.zeros((12, 3, 3))
    index = 0;
    for i in range(6):
        for j in range(3):
            for k in range(3):
                cube3D[faces[i], j, k] = numbers[index]
                index+=1
    return cube3D

def solved_cube(faces):
    cube3D = np.zeros((12, 3, 3))
    record = np.ones(6)
    counter=1
    # print(record)
    for i in range(6):
        for j in range(3):
            for k in range(3):
                cube3D[faces[i], j, k] = counter
                counter+=1
        counter=1
    return cube3D

def successor_function(cube3D,faces,type):
    if type == "F":

        cube3D[5, :, :] = np.rot90(cube3D[5,:,:],3)



        bucket = np.array(cube3D[6, :, 0])
        bucket = bucket[::-1]
        cube3D[6, :, 0] = cube3D[1, 2, :]

        bucket2 = np.array(cube3D[9, 0, :])

        cube3D[9, 0, :] = bucket



        bucket = np.array(cube3D[4, :, 2])
        bucket = bucket[::-1]
        cube3D[4, :, 2] = bucket2



        cube3D[1, 2, :] = bucket

        return cube3D

    if type == "L":

        cube3D[4, :, :] = np.rot90(cube3D[4,:,:],3)


        bucket = np.array(cube3D[5, :, 0])
        cube3D[5, :, 0] = cube3D[1, :, 0]

        bucket2 = np.array(cube3D[9, :, 0])
        bucket2 = bucket2[::-1]

        cube3D[9, :, 0] = bucket

        bucket = np.array(cube3D[7, :, 2])
        bucket = bucket[::-1]
        cube3D[7, :, 2] = bucket2


        cube3D[1, :, 0] = bucket

        return cube3D

    if type == "R":

        cube3D[6, :, :] = np.rot90(cube3D[6, :, :], 3)

        bucket = np.array(cube3D[7, :, 0])
        bucket = bucket[::-1]
        cube3D[7, :, 0] = cube3D[1, :, 2][::-1]



        bucket2 = np.array(cube3D[9, :, 2])

        cube3D[9, :, 2] = bucket

        bucket = np.array(cube3D[5, :, 2])
        cube3D[5, :, 2] = bucket2


        cube3D[1, :, 2] = bucket

        return cube3D

    if type == "U":

        cube3D[1, :, :] = np.rot90(cube3D[1, :, :], 3)



        bucket = np.array(cube3D[4, 0, :])
        cube3D[4, 0, :] = cube3D[5, 0, :]


        bucket2 = np.array(cube3D[7, 0, :])

        cube3D[7, 0, :] = bucket



        bucket = np.array(cube3D[6, 0, :])
        cube3D[6, 0, :] = bucket2



        cube3D[5, 0, :] = bucket

        return cube3D

    if type == "D":

        cube3D[9, :, :] = np.rot90(cube3D[9, :, :], 3)

        bucket = np.array(cube3D[6, 2, :])
        cube3D[6, 2, :] = cube3D[5, 2, :]

        bucket2 = np.array(cube3D[7, 2, :])

        cube3D[7, 2, :] = bucket

        bucket = np.array(cube3D[4, 2, :])
        cube3D[4, 2, :] = bucket2

        cube3D[5, 2, :] = bucket

        return cube3D

    if type == "B":
        cube3D[7, :, :] = np.rot90(cube3D[7, :, :], 3)

        bucket = np.array(cube3D[4, :, 0])
        cube3D[4, :, 0] = cube3D[1, 0, :][::-1]
        bucket2 = np.array(cube3D[9, 2, :])
        bucket2 = bucket2[::-1]
        cube3D[9, 2, :] = bucket
        bucket = np.array(cube3D[6, :, 2])
        cube3D[6, :, 2] = bucket2
        cube3D[1, 0, :] = bucket
        return cube3D

    if type == "F-":

        cube3D[5, :, :] = np.rot90(cube3D[5,:,:],1)

        bucket = np.array(cube3D[4, :, 2])
        cube3D[4, :, 2] = cube3D[1, 2, :][::-1]

        bucket2 = np.array(cube3D[9, 0, :])
        bucket2 = bucket2[::-1]

        cube3D[9, 0, :] = bucket

        bucket = np.array(cube3D[6, :, 0])
        cube3D[6, :, 0] = bucket2

        cube3D[1, 2, :] = bucket

        return cube3D

    if type == "L-":

        cube3D[4, :, :] = np.rot90(cube3D[4,:,:],1)


        bucket = np.array(cube3D[7, :, 2])
        bucket = bucket[::-1]
        cube3D[7, :, 2] = cube3D[1, :, 0][::-1]

        bucket2 = np.array(cube3D[9, :, 0])

        cube3D[9, :, 0] = bucket

        bucket = np.array(cube3D[5, :, 0])
        cube3D[5, :, 0] = bucket2

        cube3D[1, :, 0] = bucket

        return cube3D

    if type == "R-":

        cube3D[6, :, :] = np.rot90(cube3D[6, :, :], 1)


        bucket = np.array(cube3D[5, :, 2])
        cube3D[5, :, 2] = cube3D[1, :, 2]

        bucket2 = np.array(cube3D[9, :, 2])
        bucket2 = bucket2[::-1]

        cube3D[9, :, 2] = bucket

        bucket = np.array(cube3D[7, :, 0])
        bucket = bucket[::-1]
        cube3D[7, :, 0] = bucket2

        cube3D[1, :, 2] = bucket

        return cube3D

    if type == "U-":

        cube3D[1, :, :] = np.rot90(cube3D[1, :, :], 1)


        bucket = np.array(cube3D[6, 0, :])
        cube3D[6, 0, :] = cube3D[5, 0, :]

        bucket2 = np.array(cube3D[7, 0, :])

        cube3D[7, 0, :] = bucket

        bucket = np.array(cube3D[4, 0, :])
        cube3D[4, 0, :] = bucket2

        cube3D[5, 0, :] = bucket
        return cube3D

    if type == "D-":

        cube3D[9, :, :] = np.rot90(cube3D[9, :, :], 1)

        bucket = np.array(cube3D[4, 2, :])
        cube3D[4, 2, :] = cube3D[5, 2, :]

        bucket2 = np.array(cube3D[7, 2, :])

        cube3D[7, 2, :] = bucket

        bucket = np.array(cube3D[6, 2, :])
        cube3D[6, 2, :] = bucket2

        cube3D[5, 2, :] = bucket

        return cube3D

    if type == "B-":

        cube3D[7, :, :] = np.rot90(cube3D[7, :, :], 1)


        bucket = np.array(cube3D[6, :, 2])
        bucket = bucket[::-1]
        cube3D[6, :, 2] = cube3D[1, 0, :]

        bucket2 = np.array(cube3D[9, 2, :])
        cube3D[9, 2, :] = bucket
        bucket = np.array(cube3D[4, :, 0])
        bucket = bucket[::-1]
        cube3D[4, :, 0] = bucket2
        cube3D[1, 0, :] = bucket
        return cube3D

def breadth_first_search(initial_state,faces,goal):
    q = Queue()
    MyNode = namedtuple("MyNode", "Child Transition Parent")
    Transitions = np.array(["F","L","R","U","D","B","F-","L-","R-","U-","D-","B-"])
    traversed_nodes = list()
    initial = MyNode(initial_state,"N",np.zeros((12,3,3)))
    q.put(initial)
    while q.empty() == 0:
        node_to_traverse = q.get()
        traversed_nodes.append(str(node_to_traverse[0]))
        for i in range(12):
            test = np.array(node_to_traverse[0])
            rotated = successor_function(test, faces, Transitions[i])
            node = MyNode(rotated,Transitions[i],node_to_traverse)
            if str(rotated) not in traversed_nodes:
                q.put(node)
                if goal_test(rotated,faces,goal):
                    moves=list()
                    while node[1]!="N":
                        moves.append(node[1])
                        node = node[2]
                    return (rotated,moves)






##################################              Main Code               #####################################
print("\nProcessing\n")
##################################              Reading From File       #####################################
numbers = list()
filename = "InitialState.txt"
for line in open(filename):
    cleanedLine = line.strip()
    if cleanedLine:  # is not empty
        numbers.append(cleanedLine[0])
        numbers.append(cleanedLine[2])
        numbers.append(cleanedLine[4])

cube3D = np.array(create_sudoku_cube(numbers,faces))
numbers[:] = []
filename = "FinalState.txt"
for line in open(filename):
    cleanedLine = line.strip()
    if cleanedLine:  # is not empty
        numbers.append(cleanedLine[0])
        numbers.append(cleanedLine[2])
        numbers.append(cleanedLine[4])

goal = np.array(create_sudoku_cube(numbers,faces))

###############################################################################################################
##################################              To Solve The Cube       #####################################
print("\n\nThe Initial state of cube :-\n\n")
print(cube3D)
start_time = datetime.datetime.now().replace(microsecond=0)
print("\nProcessing\n")
(result,moves) = breadth_first_search(cube3D,faces,goal)
end_time = datetime.datetime.now().replace(microsecond=0)
print("\n\nThe Final state of cube :-\n\n")
print(result)
diff = end_time-start_time
print("Time Taken By BFS  :-  " + str(diff))
print("The Moves Required to solve it are : " + str(moves[::-1]))

################################################################################################################


