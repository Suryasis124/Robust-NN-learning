# Robust NN learning
This repository contains the Python code for the simulation experiments and the real data applications discussed in the paper "Provably robust learning of regression neural networks using $\beta$-divergence". All the .ipynb files are well commented and self-explanatory.

The files Function-1-parallel.ipynb, ..., Function-5-parallel.ipynb were used to generate the results in Tables 3-7 of the paper. The files ASN-CV.ipynb, BHP-CV.ipynb, CCS-CV.ipynb, respectively, were used to generate the 10-Fold CV TMSE results of the ASN, BHP, and CCS data, as given in Table 8. We used Python 3.10.12 version on the Ubuntu OS.

For each .ipynb file, the user needs to run all the cells sequentially to get the results.

We have implemented the DPD-loss function as a Python object/class and named it either "CustomLoss" or "DPDLoss" in different files. The argument "alpha" of this Python object corresponds to the tuning parameter $\beta$ of the $\beta$-divergence (DPD measure).
