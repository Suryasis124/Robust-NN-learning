This folder contains Python codes for reproducing all simulation experiments and real data applications discussed in the paper: 
 - Provably robust learning of regression neural networks using $\beta$-divergence.

The DPD-loss function is implemented as a Python object/class and named as either "CustomLoss" or "DPDLoss" in different files, which can be used as a loss function input to the .fit method, applied to a Keras model object in a TensorFlow environment. 
The argument "beta" of this Python object corresponds to the tuning parameter $\beta$ of the $\beta$-divergence (DPD measure). 

----
## Function lists:
- Function-i-parallel.ipynb: Produces simulation results of Tables (2+i) of the paper, for i=1, 2, 3, 4, 5, 6, 7.
- ASN-CV.ipynb, BHP-CV.ipynb, CCS-CV.ipynb: Produce the 10-Fold CV TMSE results of the ASN, BHP, and CCS data, respectively, as given in Table 8 of the paper.
- ASN.csv, BHP.csv, CCS.csv: Contain the ASN, BHP, and CCS datasets, respectively, after required scaling.
- ASN-diagnostics.ipynb, BHP-diagnostics.ipynb, CCS-diagnostics.ipynb: Produce the scatterplots and histograms of the residuals for ASN, BHP, and CCS datasets, respectively.
- IF-NN-sigmoid.ipynb: Produces the influence function plots for the NN architecture with sigmoid activation function.
- IF-NN-relu.ipynb: Produces the influence function plots for the NN architecture with ReLU activation function.


---
All codes are prepared and tested using Python 3.10.12 version on the Ubuntu OS.
