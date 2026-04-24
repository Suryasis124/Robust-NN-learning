This folder contains Python codes for reproducing all simulation experiments and real data applications discussed in the paper: 
 - rSDNet: Unified Robust Neural Learning against Label Noise and Adversarial Attacks.

The SD-loss function is implemented as a Python object/class and named as either "SDIV" in the files, which can be used as a loss function input to the .fit method, applied to a Keras model object in a TensorFlow environment. 
The arguments "lam" and "beta" of this Python object correspond to the tuning parameters $\lambda$ and $\beta$ of the S-divergence. 
