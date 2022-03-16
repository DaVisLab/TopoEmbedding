# TopoEmbedding
Existing software libraries for Topological Data Analysis (TDA) offer limited support for interactive visualization. Most libraries only allow to visualize topological descriptors (e.g., persistence diagrams), and lose the connection with the original domain of data. This makes it challenging for users to interpret the results of a TDA pipeline in an exploratory context. TopoEmbedding is a web-based tool that simplifies the interactive visualization and analysis of persistence-based descriptors. TopoEmbedding allows non-experts in TDA to explore similarities and differences found by TDA descriptors with simple yet effective visualization techniques.  
The link to the tool is https://davislab.github.io/TopoEmbedding/

The repository mainly consist of three folders: **data**, **js**, and **python**.

- **data** folder stores all the precomputed data for the visualization. Under the **data** folder:
   - *minst_png* contains the original MNIST images as input for persistent homology analysis. Currently we have 1000 handwritten digits (100 images per digits) stored under 10 subdirectory representing 10 digits.
   - *minst* contains the direct output of the Topological ToolKit (TTK): the persistent diagram and cycles for each image in *minst_png*.
   - *mnist_cycles* contains the *.json* files for storing the cycles, which are used to render the cycles in the 
   - *mnist_pd* contains the *.csv* files for storing the pairs in the persistent diagrams.
   - *mnist_pi* contains the *.csv* files for storing the matrix values of persistent images.
   - *mnist_mapping* contains the *.json* file for storing the weights of each pair to the pixels of the persistent images.
   - *mnist_embedding* contains *.json* file for storing the scatter plot for each embedding method.

- **js** folder includes the javascripts file that implements the main functionality of the TopoEmbedding interface. Main files include:
   - *force.js* renders the scatter plot using the *.json* file in the *mnist_embedding*.
   - *inputimage.js* renders the persistent cycles (in the *minst_cycles* folder) over the orginal input images (in the *minst_png* folder) using *Three.js*.
   - *persistence-image.js* renders the persistent images (in the *mnist_pi* folder) in a 10 by 10 square panel using *svg*.
   - *showMinkowski.js* renders the chart showing the pixel-wise difference of two persistent images.

- **python** folder includes the python scripts that do the computation for the persistence analysis pipeline.
  - The *compute_data.py* run the *ttk_generate_pairs_mnist.py*  (trace generated using paraview version 5.6.0) to compute cycles and persistent diagrams for the png images under the './data/mnist_png/' directory. *mnist*, *mnist_cycles*,*mnist_pd*, *mnist_pi*, *mnist_mapping* and *mnist_embedding* directories are then automatically generated after the computation. For the code below in *compute_data.py*:
    ```
    ...
      os.system("~/ttk-clemson/ParaView-v5.6.0/build/bin/pvpython ./python/ttk_generate_pairs_mnist.py image.vti "+full_path+" "+folder+" "+number);
    ...
    ```
    Make sure the first argument *~/ttk-clemson/ParaView-v5.6.0/build/bin/pvpython* is replaced with the correct Paraview directory.
  - *compute_cycles.py* converts output (*vtk* files) of *compute_data.py* into *json* files for storing cycles and *csv* files for storing persistent pairs under the *mnist_cycles* and *mnist_pd* files. The *compute_cycles.py* should be run after the *compute_cycles.py*. 
  - *compute_pi_embedding.py* first computes the persistent images from the persistent diagrams, then computes pair-wise distance for all the persistent images, and finally computes a lower dimension embedding with one of the three dimensionality reduction techniques: Isomap, Multi-dimensional Scaling (MDS), and t-distributed Stochastic Neighbor Embedding (t-SNE).

## Installing the dependencies

The persistent homology is computed using the newly developed TTK plugin at the website [PersistentCyles](https://github.com/IuricichF/PersistenceCycles) (refer to the website for additional instructions about installing TTK). Make sure the plugin is correctly installed before running *compute_data.py*

Additional python libraries need to be installed for running *compute_cycles* and *compute_pi_embedding* by typing the following commands to install the dependencies:

```
pip install -U meshio giotto-tda matplotlib scipy persim sklearn pyevtk

```




