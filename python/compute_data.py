import meshio
import numpy as np
from matplotlib import image
from pyevtk.hl import imageToVTK
from scipy import ndimage
import os

root = './data/mnist_png/testing'
destination = './data/mnist'

full_path = os.path.abspath("./")


DATA_DIR = os.path.join(os.getcwd(), "data")            # path of the data folder
IMG_DIR = os.path.join(DATA_DIR, "mnist_png")        # path of the vtk images
VTK_DIR = os.path.join(DATA_DIR, "mnist")                 # path of the vtk cycles and pd
PD_DIR = os.path.join(DATA_DIR, "mnist_pd")                   # path of the persistence diagram pairs
PI_DIR = os.path.join(DATA_DIR, "mnist_pi")                   # path of the persistence image matrices
MAP_DIR = os.path.join(DATA_DIR, "mnist_mapping")             # path of the mappings
EBD_DIR = os.path.join(DATA_DIR, "mnist_embeddings")          # path of the embeddings
CYCL_DIR = os.path.join(DATA_DIR, "mnist_cycles")          # path of the embeddings


if(not os.path.exists(VTK_DIR)):
    os.mkdir(VTK_DIR)
    for i in range(10):
        os.mkdir(os.path.join(VTK_DIR, str(i)))

if(not os.path.exists(PD_DIR)):
    os.mkdir(PD_DIR)
    for i in range(10):
        os.mkdir(os.path.join(PD_DIR, str(i)))

if(not os.path.exists(PI_DIR)):
    os.mkdir(PI_DIR)
    for i in range(10):
        os.mkdir(os.path.join(PI_DIR, str(i)))

if(not os.path.exists(MAP_DIR)):
    os.mkdir(MAP_DIR)
    for i in range(10):
        os.mkdir(os.path.join(MAP_DIR, str(i)))

if(not os.path.exists(EBD_DIR)):
    os.mkdir(EBD_DIR)
    for i in range(10):
        os.mkdir(os.path.join(EBD_DIR, str(i)))

if(not os.path.exists(CYCL_DIR)):
    os.mkdir(CYCL_DIR)
    for i in range(10):
        os.mkdir(os.path.join(CYCL_DIR, str(i)))


for subdir in os.walk(root):
    if len(subdir[1]) == 0:
        print(subdir[0])
        for files in subdir[2]:

            if(files == ".DS_Store"):
                continue
            
            folder = subdir[0].split("/")[4]
            number = files.split(".")[0]

            if(os.path.exists('/Users/fiurici/GitHub/TopoEmbedding/data/mnist/'+folder+'/'+number+'_cycles.vtk')):
                continue

            im = image.imread(subdir[0]+"/"+files)
            im = np.array(im, dtype="double")
            
            inside = im > 0
            outside = im <= 0

            im1 = ndimage.morphology.distance_transform_edt(inside)
            im2 = ndimage.morphology.distance_transform_edt(outside)

            im = im2-im1

            im = (im - np.min(im))/np.ptp(im)

            im = im.reshape([im.shape[0],im.shape[1],1])
            imageToVTK('image', pointData = {"field": im})


            os.system("~/ttk-clemson/ParaView-v5.6.0/build/bin/pvpython ./python/ttk_generate_pairs_mnist.py image.vti "+full_path+" "+folder+" "+number)