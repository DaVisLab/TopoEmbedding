import meshio
import struct, csv
import numpy as np


def normalizeVertices(vertices):
    max = np.amax(vertices)
    scale = 1.0/max
    for i in range(len(vertices)):
        vertices[i] = vertices[i] * scale
        
def computeNormal(vertices,triangles, normals):
     for i in range(len(triangles)):
        id0 = int(triangles[i][0])
        id1 = int(triangles[i][1])
        id2 = int(triangles[i][2])
        v0 = vertices[id1] - vertices[id0]
        v1 = vertices[id2] - vertices[id1]
        v2 = vertices[id0] - vertices[id2]
        normals[id0] = np.cross(v0, v2)
        normals[id1] = np.cross(v1, v0)
        normals[id2] = np.cross(v2, v1)
     return

def writeMeshDataToFile(vertices, indices, normals):
    with open ('C:/Users/baoxu/Downloads/indices.dat', 'wb') as file:
      for i in range(len(indices)):
          file.write(struct.pack('<i', int(indices[i][0])))
          file.write(struct.pack('<i', int(indices[i][1])))
          file.write(struct.pack('<i', int(indices[i][2])))
    with open ('C:/Users/baoxu/Downloads/vertices.dat', 'wb') as file:
      for i in range(len(vertices)):
         file.write(struct.pack('<f', vertices[i][0]))
         file.write(struct.pack('<f', vertices[i][1]))
         file.write(struct.pack('<f', vertices[i][2]))
    with open ('C:/Users/baoxu/Downloads/normals.dat', 'wb') as file:
      for i in range(len(normals)):
         file.write(struct.pack('<f', normals[i][0]))
         file.write(struct.pack('<f', normals[i][1]))
         file.write(struct.pack('<f', normals[i][2]))

pairs = meshio.read("C:/Users/baoxu/Downloads/0_pd.vtk");
cycles = meshio.read("C:/Users/baoxu/Downloads/0_cycles.vtk")

position_pairs2 = 0
position_pairs1 = 0
for i in range(0,len(pairs.cell_data['Type'][0])):
    if pairs.cell_data['Type'][0][i] == 1:
       position_pairs2 = i
    if pairs.cell_data['Type'][0][i] == 0:
        position_pair1 = i

temp = position_pair1
with open('C:/Users/baoxu/OneDrive/Documents/cycleID.txt','w') as file:
    file.write('1')
    file.write(' ')
    file.write('%d' %temp)
    file.write('\r\n')
    file.write('2')
    file.write(' ')
    file.write('%d' %position_pairs2)
    file.write('\r\n')
indices = cycles.cells_dict['triangle'];

k = 0   
with open('C:/Users/baoxu/OneDrive/Documents/pair.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Birth", "Death"])                              
    for line in pairs.cells[0].data:       #write persistent pairs in csv file
        v0 = line[0]
        v1 = line[1]
        f0 = pairs.point_data["Filtration"][v0]
        f1 = pairs.point_data["Filtration"][v1]
 #  fout.write(struct.pack('<f', f0))#
 #  fout.write(struct.pack('<f', f1))# 
        writer.writerow([k, f0, f1])
j = 0
k = 0
temp = 0
n_cycle = 0
p_cycleId = cycles.cell_data['CycleId'][0][0]
a = np.zeros(shape=(500,2))
for cycleId in cycles.cell_data['CycleId'][0]:   #write cycleId and corresponding number of triangles of every cycle
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
with open('C:/Users/baoxu/OneDrive/Documents/cycleID.txt','a') as file:
    file.write('%d' %n_cycle)
    file.write('\r\n')
    for i in range(0, n_cycle):
        file.write('%d'%a[i][0])
        file.write(' ')
        file.write('%d'%a[i][1])
        file.write('\r\n')

num_triangles = len(cycles.cell_data['CycleId'][0])
num_vertices = len(cycles.points)
vertices = np.zeros(shape = (num_vertices,3))
triangles = np.zeros(shape = (num_triangles, 3))
normals = np.zeros(shape = (num_vertices, 3))


for i in range(num_vertices):
    vertices[i] = cycles.points[i]
for i in range(num_triangles):
    triangles[i] = cycles.cells_dict['triangle'][i]

normalizeVertices(vertices)
computeNormal(vertices,triangles,normals)
writeMeshDataToFile(vertices,triangles,normals)














