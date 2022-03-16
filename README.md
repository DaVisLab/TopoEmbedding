# TopoEmbedding
Existing software libraries for Topological Data Analysis (TDA) offer limited support for interactive visualization. Most libraries only allow to visualize topological descriptors (e.g., persistence diagrams), and lose the connection with the original domain of data. This makes it challenging  for users to interpret the results of a TDA pipeline in an exploratory context. TopoEmbedding is a web-based tool that simplifies the interactive visualization and analysis of persistence-based descriptors. TopoEmbedding allows non-experts in TDA to explore similarities and differences found by TDA descriptors with simple yet effective visualization techniques.  
The link of the tool is https://davislab.github.io/TopoEmbedding/
## Pipeline
The repository mainly consist of three folders: **data**, **js**, and **python**.

- **data** folder contains 1000 handwritten digits (100 images per digit), which are the subset of the original famous MINST dataset to perform the analysis and visualization.

- **js** folder includes the javascripts file that implements the main functionality of the TopoEmbedding interface.

- **python** folder includes the python scripts that do the computation for the persistence analysis pipeline.

To run the scripts, typing following commands to install the dependencies:

```
pip install -U meshio giotto-tda matplotlib scipy persim sklearn

```
