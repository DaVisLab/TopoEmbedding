
# Run the script from the project root path.
import os
import csv
import json
import umap
import meshio
import numpy as np
import gtda.plotting
import gtda.diagrams
import matplotlib.pyplot as plt
import scipy.spatial.distance as ssdist
from persim import images_kernels
from persim import PersistenceImager
from sklearn import manifold

# Directory information
DATA_DIR = os.path.join(os.getcwd(), "data")            # path of the data folder
VTK_DIR = os.path.join(DATA_DIR, "mnist")               # path of the vtk files
PD_DIR = os.path.join(DATA_DIR, "mnist_pd")             # path of the persistence diagram pairs
PI_DIR = os.path.join(DATA_DIR, "mnist_pi")             # path of the persistence image matrices
MAP_DIR = os.path.join(DATA_DIR, "mnist_mapping")       # path of the mappings
EBD_DIR = os.path.join(DATA_DIR, "mnist_embeddings")    # path of the embeddings

def getPersistenceDiagram(vtkFilePath, toFile=False):
    """
    Get the persistence diagram ([birth, death, type]) from a given vtk file.

    Parameters
    ----------
    vtkFilePath: string
        The path of the vtk file.
    toFile: bool
        If True, write the persistence pairs to a csv file.

    Returns
    ----------
    pdiagrm: list
        The list containing all persistence pairs.

    """
    pdiagram = []
    try:
        ppairs = meshio.read(vtkFilePath)
        
        k = 0
        for line in ppairs.cells[0].data: 
            v0 = line[0]
            v1 = line[1]
            f0 = ppairs.point_data["Filtration"][v0]    # birth
            f1 = ppairs.point_data["Filtration"][v1]    # death
            t = ppairs.cell_data["Type"][0][k]          # homology dimension
            k += 1
            pdiagram.append([f0, f1, t])

        # Write the pairs to a csv file
        if toFile:
            subFolder = os.path.basename(os.path.dirname(vtkFilePath))
            outFile = os.path.splitext(os.path.basename(vtkFilePath))[0]+'.csv'  # replace the file extension
            with open(os.path.join(PD_DIR, subFolder, outFile), 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Birth", "Death", "TYPE"]) 
                writer.writerows(pdiagram)
    except:
        print("Empty persistence diagram for "+vtkFilePath)

    return (pdiagram)

def transform(pers_pair, skew=True, resolution=None, weight=None, weight_params=None, kernel=None, kernel_params=None, _bpnts=None, _ppnts=None):
    """ Transform a persistence pair into a persistence image.
    Adapted from https://github.com/scikit-tda/persim/blob/822c9ca85cb08b382fbc128ffd158a37f921e5b9/persim/images.py#L74 

    Parameters
    ----------
    pers_dgm : (1,2) numpy.ndarray
        A persistence pair.
    skew : boolean 
        Flag indicating if diagram(s) need to first be converted to birth-persistence coordinates (default: True).
    resolution : pair of ints
        The number of pixels along the birth and persistence axes in the persistence image.
    weight : callable
        Function which weights the birth-persistence plane.
    weight_params : dict
        Arguments needed to specify the weight function.
    kernel : callable
        Cumulative distribution function defining the kernel.
    kernel_params : dict
        Arguments needed to specify the kernel function.
    _bpnts : (N,) numpy.ndarray
        The birth coordinates of the persistence image pixel locations.
    _ppnts : (M,) numpy.ndarray
        The persistence coordinates of the persistence image pixel locations.

    Returns
    -------
    numpy.ndarray
        (M,N) numpy.ndarray encoding the persistence image corresponding to pers_pair.
    """
    pers_pair = np.copy(pers_pair)
    pers_img = np.zeros(resolution)

    # if necessary convert from birth-death coordinates to birth-persistence coordinates
    if skew:
        pers_pair[1] = pers_pair[1] - pers_pair[0]

    # compute weight for the persistence pair
    wts = weight(pers_pair[0], pers_pair[1], **weight_params)

    # omitting special case from source code
    # handle the special case of a standard, isotropic Gaussian kernel
    if kernel == images_kernels.gaussian:
        general_flag = False
        sigma = kernel_params['sigma']

        # sigma is specified by a single variance
        if isinstance(sigma, (int, float)):
            sigma = np.array([[sigma, 0.0], [0.0, sigma]], dtype=np.float64)

        if (sigma[0][0] == sigma[1][1] and sigma[0][1] == 0.0):
            sigma = np.sqrt(sigma[0][0])
            ncdf_b = images_kernels.norm_cdf((_bpnts - pers_pair[0]) / sigma)
            ncdf_p = images_kernels.norm_cdf((_ppnts - pers_pair[1]) / sigma)
            curr_img = ncdf_p[None, :] * ncdf_b[:, None]
            pers_img += wts*(curr_img[1:, 1:] - curr_img[:-1, 1:] - curr_img[1:, :-1] + curr_img[:-1, :-1])
        else:
            general_flag = True

    # handle the general case
    if general_flag:
        bb, pp = np.meshgrid(_bpnts, _ppnts, indexing='ij')
        bb = bb.flatten(order='C')
        pp = pp.flatten(order='C')
        curr_img = np.reshape(kernel(bb, pp, mu=pers_pair, **kernel_params),
                                (resolution[0]+1, resolution[1]+1), order='C')
        pers_img += wts*(curr_img[1:, 1:] - curr_img[:-1, 1:] - curr_img[1:, :-1] + curr_img[:-1, :-1])
    

    return pers_img


def getPersistenceImage(pdiagramPath, type=None, saveMatrix=False, saveImage=False):
    """
    Get the persitence image from the given persistence diagram csv file with 
    a specific homology dimension.

    Parameters
    ----------
    pdiagramPath: string
        The persistence diagram containing triplets of birth, death and homology dimension.
    type: int
        The homogoly dimension used to produce the persistence image.
    prefix: string
        The prefix added to the filenames, only works if `saveMatrix` or `saveImage` is True.
    saveMatrix: bool
        If True, write the matrix of persistence image to a file.
    saveImage: bool
        If True, write the plot of the persistence image to a file.

    Returns
    ----------
    pimage: array_like
        The persistence image with the given persistence diagram and homology dimension.
    """
    # select the dimension and remove it from the triplet
    pdiagram = np.genfromtxt(pdiagramPath, delimiter=',')

    # when the persistence diagram has only one tuple the diagram was read from file with the wrong shape
    diag = []
    if(len(pdiagram.shape)==1):
        diag.append(pdiagram)
        pdiagram = np.array(diag)

    if type is None:
        pdiagram = pdiagram[:,:-1]
    else:
        pdiagram = pdiagram[pdiagram[:,2] == type, :-1]
    

    p_size = 0.1
    # Generate the persistence image
    pimgr = PersistenceImager(pixel_size=p_size, birth_range=(0.0,1.0), kernel_params={'sigma':0.01})
    # pimgr.fit(pdiagram, skew=True)
    pimage = pimgr.transform(pdiagram, skew=True)

    num_pixels = 1.0 / p_size
    head = ", ".join(list(map(str, list(range(int(num_pixels))))))

    # check each pixel in persistence image
    height = pimgr.resolution[0]
    width = pimgr.resolution[1]
    mapping = {p : {"idx": [], "weights": []} for p in range(height*width)}
    for k in range(pdiagram.shape[0]):
        image = transform(pdiagram[k], skew=True, resolution=pimgr.resolution, weight=pimgr.weight, weight_params=pimgr.weight_params, kernel=pimgr.kernel, kernel_params=pimgr.kernel_params, _bpnts=pimgr._bpnts, _ppnts=pimgr._ppnts)
        avg = np.mean(image)
        for i in range(height):
            for j in range(width):
                if (image.T[i][j]) > avg:
                    mapping[j*width+i]["idx"].append(k); 
                    mapping[j*width+i]["weights"].append(round(image.T[i][j] / pimage[i][j], 6));

    if saveMatrix:
        subFolder = os.path.basename(os.path.dirname(pdiagramPath))
        csvFile = os.path.basename(pdiagramPath)
        csvFile = csvFile[:-5] + 'i' + csvFile[-4:]
        mappingFile = csvFile[:-6] + "mapping.json"
        np.savetxt(os.path.join(PI_DIR, subFolder, csvFile), pimage, fmt="%.6f", delimiter=',', header=head, comments="")
        with open(os.path.join(MAP_DIR, subFolder, mappingFile), 'w') as file:
            json.dump(mapping, file, indent=2)
    
    if saveImage:
        subFolder = os.path.basename(os.path.dirname(pdiagramPath))
        imgFile = os.path.basename(pdiagramPath)
        imgFile = imgFile[:-5] + "i.png"
        fig = plt.figure()
        ax = plt.subplot(1,1,1)
        pimgr.plot_image(pimage, ax)
        # plt.show()
        fig.savefig(os.path.join(PI_DIR, subFolder, imgFile))
        
    return (pimage)


def getPairwiseDist(images):
    """
    Get the pairwise distance for the collection of persistence images.

    Parameters
    ----------
    images: array_like
        A collection of persistence images.

    Returns
    ----------
    distance: array_like
        The pairwise distances for the persistence images.
    """

    pers_images = np.asarray(images)
    if pers_images.ndim != 3:
        print("The dimension of the input array should be 3!\n")
        return -1

    pers_images = pers_images.reshape(len(pers_images), -1)
    dists = ssdist.pdist(pers_images, "minkowski", p=2.0)

    return ssdist.squareform(dists)


def getEmbeddings(distances, showFig=False):
    """
    Get the embeddings from the distance matrix using different methods.

    Parameters
    ----------
    distances: array_like
        The distance matrix for persistence images.
    showFig: bool
        If True, show the grouped scatter plot for the embeddings.

    Returns
    ----------
    embeddings: dictionary
        The dictionary containing embeddings computed with different methods.
    """

    # methods used for computing embeddings
    methods = {}
    methods["Isomap"] = manifold.Isomap(n_neighbors=5, n_components=2, metric="precomputed")
    methods["MDS"] = manifold.MDS(n_components=2, dissimilarity="precomputed", random_state=0)
    methods["t-SNE"] = manifold.TSNE(n_components=2, metric="precomputed", square_distances=True, init="random", random_state=0)
    # methods["UMAP"] = umap.UMAP(n_neighbors=5, metric="precomputed", init="random", n_components=2, random_state=0)

    # save embedding information
    embeddings = {}
    for i, (label, method) in enumerate(methods.items()):
        embeddings[label] = {}
        Y = method.fit_transform(distances)
        embeddings[label]["x"] = [round(x, 8) for x in Y[:, 0].tolist()]
        embeddings[label]["y"] = [round(x, 8) for x in Y[:, 1].tolist()]

    # TODO: plot the grouped scatter plot
    if showFig:
        # color settings
        groups = [[0, 6, 8, 9], [1, 7, 4], [2, 3, 5]]
        colors = ("red", "green", "blue")

        digits = []
        grouped_embeddings = ([], [], [])

        for dist in distances:
            digits.append(int(next(iter(dist))[0]))

        for i in range(3):
            for j in groups[i]:
                grouped_embeddings[i].append(Y[digits==j])

        fig = plt.figure(figsize=(8,8))
        ax = fig.add_subplot(2, 2, i+1)
        ax.set_title(label)
        plt.show()
    
    return embeddings

# Main function
if __name__ == "__main__":

    SAVE_ALL_PERS_DIAGRAMS = True
    SAVE_ALL_PERS_IMAGES = True
    SAVE_ALL_EMBEDDINGS = True
    

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


    # Save all persistence diagrams to csv files
    
    print("Computing persistence diagrams")
    if SAVE_ALL_PERS_DIAGRAMS:
        for i in range(10):
            dataDir = os.path.join(VTK_DIR, str(i))
            if os.path.exists(dataDir):
                files = [f for f in os.listdir(dataDir) if "csv" in f]
                for file in files:
                    os.remove(os.path.join(dataDir, file))

        for i in range(10):
            dataDir = os.path.join(VTK_DIR, str(i))
            if os.path.exists(dataDir):
                for file in os.listdir(dataDir):
                    if file.endswith("_pd.vtk"):
                        pdiagram = getPersistenceDiagram(os.path.join(dataDir, file), True)

    # one-line code for testing
    # pimg = getPersistenceImage(os.path.join(PD_DIR, "7", "0_pd.csv"), None, True)

    # reset all persistence images to csv files
    print("Computing persistence images")
    if SAVE_ALL_PERS_IMAGES:
        for i in range(10):
            pimgDir = os.path.join(PI_DIR, str(i))
            if os.path.exists(pimgDir):
                files = [f for f in os.listdir(pimgDir) if "csv" in f]
                for file in files:
                    os.remove(os.path.join(pimgDir, file))

        for i in range(10):
            pdiagDir = os.path.join(PD_DIR, str(i))
            if os.path.exists(pdiagDir):
                files = os.listdir(pdiagDir)
                for file in os.listdir(pdiagDir):
                    pimage = getPersistenceImage(os.path.join(pdiagDir, file), 1, True)
                


    # 100 persistence images coming from different digits
    print("Computing embeddings")
    if SAVE_ALL_EMBEDDINGS:
        persistence_images = []
        file_list = []
        for i in range(10):
            pimgDir = os.path.join(PI_DIR, str(i))
            if os.path.exists(pimgDir):
                files = [f for f in os.listdir(pimgDir) if "pi.csv" in f]
                files.sort()
                for file in files:
                    pimage = np.genfromtxt(os.path.join(pimgDir, file), delimiter=',', skip_header=1)
                    persistence_images.append(pimage)
                    file_list.append(str(i)+ '/' + file)
        # Compute the pairwise distances
        print("Computing pairwise distances between "+str(len(persistence_images))+" persistence images")
        distances = getPairwiseDist(persistence_images)
        embeddings = getEmbeddings(distances)
        # write results to json files
        for _, (method, result) in enumerate(embeddings.items()):
            tmp_dict = {}
            tmp_dict["name"] = file_list
            tmp_dict["x"] = result["x"]
            tmp_dict["y"] = result["y"]
            output_file = "embeddings_" + method + ".json"
            file = open(os.path.join(EBD_DIR, output_file), 'w')
            json.dump(tmp_dict, file, indent=2)

