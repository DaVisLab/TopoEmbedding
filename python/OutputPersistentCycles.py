import os
import math
import meshio
import shutil
import json
import struct, csv
import numpy as np
from sklearn.neighbors import KernelDensity
import matplotlib.pyplot as plt
#The script reads the distance.json in ROOT_DIR and extracts all the cycles and pairs from the minst, minst_pi, and minst_png according
# to the keys of the distance matrix 
PI = 3.141596
MAX_NUM_VERTICES = 1000
GRID_BOTTOM = 0
GRID_TOP = 25
ROOT_DIR = 'C:/Users/baoxu/OneDrive/Documents/GitHub/TopoEmbedding'
TEST_DIR = 'C:/Users/baoxu/source/repos/ReadPersistentPairs/cycles'
DATA_DIR = os.path.join(ROOT_DIR, "data")        # path of the data folder
VTK_DIR = os.path.join(DATA_DIR, "mnist")  
PSIMAGE_DIR = os.path.join(ROOT_DIR,"images")
DISTANCE_DIR = os.path.join(ROOT_DIR,"distance")
MINST_VTK_DIR =  os.path.join(DATA_DIR,"mnist")
MINST_PIMAGE =  os.path.join(DATA_DIR,"mnist_pi")
MINST_PNG =  os.path.join(DATA_DIR,"mnist_png")
CYCLE_DIR = os.path.join(DATA_DIR,"cycles")
PAIR_DIR = os.path.join(DATA_DIR, "pairs")
distance_file = os.path.join(DISTANCE_DIR,"distance.json")


def normalizeVertices(vertices):
    max = np.amax(vertices)
    min = np.amin(vertices)
    scale = 1.0/(max - min)
    theta = 90.0/180 * PI;
    for i in range(len(vertices)):
        vertices[i] = (vertices[i] - min) * scale
        xx = vertices[i][0]
        yy = vertices[i][1]
        vertices[i][0] = xx * math.cos(theta) + yy * math.sin(theta)
        vertices[i][1] = xx * -math.sin(theta) + yy * math.cos(theta)
# interprete vtk files for js 
def read_vtk_file(pd_file, cycle_file, cycle_info_file, pair_csv_file):
   
    pairs = meshio.read(pd_file)
    cycles = meshio.read(cycle_file)

    position_pairs1 = 0
    for i in range(0,len(pairs.cell_data['Type'][0])):
        if pairs.cell_data['Type'][0][i] == 0:
           position_pairs1 = i

    temp = position_pairs1
   
    with open(cycle_info_file,'wb') as file:
       file.write(struct.pack('<f', 1.0))
       file.write(struct.pack('<f', temp))

    indices = cycles.cells_dict['line'];
    k = 0
    pair_csv_path = os.path.join(PAIR_DIR, pair_csv_file);
    with open(pair_csv_path, 'w', newline='') as file:
         writer = csv.writer(file)
         writer.writerow(["ID", "Birth", "Death"])                                 
         for line in pairs.cells[0].data:       #write persistent pairs in csv file
            v0 = line[0]
            v1 = line[1]
            f0 = pairs.point_data["Filtration"][v0]
            f1 = pairs.point_data["Filtration"][v1]
            writer.writerow([k, f0, f1])
            k = k + 1
    j = 0
    k = 0
    temp = 0
    n_cycle = 0
    p_cycleId = cycles.cell_data['CycleId'][0][0]
    a = np.zeros(shape=(500,2))
    for cycleId in cycles.cell_data['CycleId'][0]:   #write cycleId and corresponding number of lines of every cycle
         k = k + 1
         if cycleId!= p_cycleId or k==len(cycles.cell_data['CycleId'][0]) :
            a[n_cycle] = [n_cycle,j]
            temp = temp + j;
            j = 0
            n_cycle = n_cycle + 1
            p_cycleId = cycleId
         if k==len(cycles.cell_data['CycleId'][0]) :
            a[n_cycle] = [n_cycle,j+1]
            temp = temp + j
            n_cycle = n_cycle + 1
            p_cycleId = cycleId
         j = j + 1
   
    with open(cycle_info_file,'ab') as file:
        file.write(struct.pack('<f', n_cycle))
        for i in range(0, n_cycle):
            file.write(struct.pack('<f', a[i][0]))
            file.write(struct.pack('<f', a[i][1]))

    num_lines = len(cycles.cell_data['CycleId'][0])
    num_vertices = len(cycles.points)
    vertices = np.zeros(shape = (num_vertices,3))
    lines = np.zeros(shape = (num_lines, 2))

    with open(cycle_info_file,'ab') as file:
        file.write(struct.pack('<f', num_vertices))

    for i in range(num_vertices):
        vertices[i] = cycles.points[i]
    for i in range(num_lines):
        lines[i] = cycles.cells_dict['line'][i]

    normalizeVertices(vertices)


    with open (cycle_info_file, 'ab') as file:
      for i in range(len(vertices)):
         file.write(struct.pack('<f', vertices[i][0]))
         file.write(struct.pack('<f', vertices[i][1]))

      for i in range(len(indices)):
         file.write(struct.pack('<f', indices[i][0]))
         file.write(struct.pack('<f', indices[i][1]))    
samples_x = np.empty([0,2])   
samples_y = np.empty([0,2])

def get_cycle_vertices(cycle_file):
    global samples_x, samples_y
    cycles = meshio.read(cycle_file)
    num_vertices = len(cycles.points)
    cur_len = len(samples_x)
    for i in range(num_vertices):       
        samples_x = np.insert(samples_x,cur_len + i, GRID_TOP - cycles.points[i][0])
        samples_y = np.insert(samples_y,cur_len + i, cycles.points[i][1])

"""Build 2D KDE"""
def ked2D(x, y, bandwidth, xbins = 100j, ybins = 100j, **kwargs):
   xx, yy = np.mgrid[GRID_BOTTOM:GRID_TOP:xbins, GRID_BOTTOM:GRID_TOP:ybins]
   xy_sample = np.vstack([yy.ravel(), xx.ravel()]).T
   
   xy_train  = np.vstack([y, x]).T
   kde_skl = KernelDensity(kernel='gaussian',bandwidth=bandwidth, **kwargs)
   kde_skl.fit(xy_train)

   # score_samples() returns the log-likelihood of the samples
   z = np.exp(kde_skl.score_samples(xy_sample))
   return xx, yy, np.reshape(z, xx.shape)

for file in os.listdir(TEST_DIR): 
    cycle_file = os.path.join(TEST_DIR, file)
    get_cycle_vertices(cycle_file)


xx,yy,zz = ked2D(samples_y, samples_x, 2.0)

plt.pcolormesh(xx, yy, zz,shading='auto')
plt.scatter(samples_y, samples_x, s=2, facecolor='white')
plt.show()
plt.savefig('test.png')

''' for file in os.listdir(VTK_DIR):
   vtk_sub_folder = os.path.join(VTK_DIR,file)
   cycle_sub_folder = os.path.join(CYCLE_DIR,file)
   pair_sub_folder = os.path.join(PAIR_DIR, file)
   for file in os.listdir(vtk_sub_folder):
       if file.endswith("_cycles.vtk"):
            number = file.split('_')[0]
            cycle_file_name = number + "_cycles.dat"
            cycle_file = os.path.join(cycle_sub_folder, cycle_file_name)
            minst_vtk_file = os.path.join(vtk_sub_folder,file)
            pair_vtk_name = number + "_pd.vtk"
            pair_vtk_file =  os.path.join(vtk_sub_folder, pair_vtk_name)            
            pair_csv_name = number + "_pd.csv"
            pair_csv_file = os.path.join(pair_sub_folder, pair_csv_name)
            read_vtk_file(pair_vtk_file,minst_vtk_file,cycle_file,pair_csv_file)  '''

# extract cycle data according to distance.json         
'''
with open(distance_file) as json_file:
    data = json.load(json_file)
    for p in data:
        name = sorted(p.keys())[0]
        temp =  name.split('/')
        digit = temp[0]
        number = temp[1].split('_')[0]
        minst_vtk_subfolder = os.path.join(MINST_VTK_DIR,digit)
        vtk_file_name = number + "_cycles.vtk"
        minst_vtk_file =  os.path.join(minst_vtk_subfolder, vtk_file_name)
        cycle_file_name = number + "_cycles.dat"
        cycle_subfolder = os.path.join(CYCLE_DIR,digit)
        cycle_file = os.path.join(cycle_subfolder, cycle_file_name)
        pair_vtk_name = number + "_pd.vtk"
        pair_vtk_file =  os.path.join(minst_vtk_subfolder, pair_vtk_name)
        pair_subfolder = os.path.join(PAIR_DIR, digit)
        pair_csv_name = number + "_pd.csv"
        pair_csv_file = os.path.join(pair_subfolder, pair_csv_name)
        read_vtk_file(pair_vtk_file,minst_vtk_file,cycle_file,pair_csv_file)
'''
