import os
import math
import meshio
import shutil
import json
import struct, csv
import numpy as np


def searchNext(all_lines, visited, point, prev):
    for i in range(len(all_lines)):
        if(not visited[i]):
            line = all_lines[i]
                   
            if(point == line[0] and prev != line[1]):
                visited[i] = True
                return line[1]
            elif(point == line[1] and prev != line[0]):
                visited[i] = True
                return line[0]

DATA_DIR = os.path.join(os.getcwd(), "data") 
CYCL_DIR = os.path.join(DATA_DIR, "mnist_cycles")

if(not os.path.exists(CYCL_DIR)):
    os.mkdir(CYCL_DIR)
    for i in range(10):
        os.mkdir(os.path.join(CYCL_DIR, str(i)))


# for each subfolder
for fold_name in os.listdir("./data/mnist/"):
    print(fold_name)
    if(fold_name != ".DS_Store"):

        # for each file in the subfolder
        
        for filename in os.listdir("./data/mnist/"+fold_name+"/"):
            if("_cycles" in filename):
                
                # print(filename)
                # open the file produced by paraview and ttk
                
                ordered_cycles = {}
                try:
                    im = meshio.read("./data/mnist/"+fold_name+"/"+filename)

                    # for each cycle id, save the list of edges
                    array_of_cycles = {}
                    for i in range(len(im.cell_data['CycleId'][0])):
                        index = str(im.cell_data['CycleId'][0][i]);

                        if(index not in array_of_cycles):
                            array_of_cycles[index] = []


                        line = im.cells_dict['line'][i]
                        array_of_cycles[index].append([line[0].tolist(), line[1].tolist()])
                    
                    # for each cycle reorder the vertices so to have them ready to be plotted with THREE.js
                    for k in array_of_cycles:
                        val = array_of_cycles[k]
                        visited = np.zeros(len(val))
                        new_array = []

                        first_point= val[0][0]
                        prevP = val[0][0]
                        nextP = val[0][1]

                        visited[0] = True

                        new_array.append(im.points[first_point].tolist())
                        while(nextP != first_point):
                            new_array.append(im.points[nextP].tolist())
                            newP = searchNext(val, visited, nextP, prevP)
                            prevP = nextP
                            nextP = newP

                        new_array.append(im.points[first_point].tolist())
                        ordered_cycles[k] = new_array
                    
                except:
                    print("No cycles for "+filename)

                # create the output json file
                id = filename.split("_")[0]
            
                with open("./data/mnist_cycles/"+fold_name+"/"+id+"_cycle.json", 'w') as fp:
                    json.dump(ordered_cycles, fp)