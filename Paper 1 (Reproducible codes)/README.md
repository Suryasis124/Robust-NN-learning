The files contain the Python code for the simulation experiments and the real data applications discussed in the paper "Provably robust learning of regression neural networks using $\beta$-divergence". The DPD-loss function was implemented as a Python object/class and named as either "CustomLoss" or "DPDLoss" in different files, which can be used as a loss function input to the .fit method, applied to a Keras model. The argument "alpha" of this Python object corresponds to the tuning parameter $\beta$ of the $\beta$-divergence (DPD measure). We used Python 3.10.12 version on the Ubuntu OS.

The files Function-1-parallel.ipynb, ..., Function-5-parallel.ipynb were used to generate the simulation experiment results in Tables 3-7 of the paper. The files ASN-CV.ipynb, BHP-CV.ipynb, CCS-CV.ipynb, respectively, were used to generate the 10-Fold CV TMSE results of the ASN, BHP, and CCS data, as given in Table 8.

We further provided a file -- User instruction to apply a robust training method.ipynb, which gives clear instructions about how to apply the existing as well as the proposed method to a new dataset. 

