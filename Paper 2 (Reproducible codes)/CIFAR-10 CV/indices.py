# This file shows how the indices of different folds of our cross-validation study has been generated
# Assume Y is a NumPy array of length 60000
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold

kf = KFold(n_splits=6, shuffle=True, random_state=42)
splits = list(kf.split(Y))

train_df = pd.DataFrame(np.column_stack([train for train, _ in splits]))
test_df = pd.DataFrame(np.column_stack([test for _, test in splits]))

train_df.to_csv("train_indices.csv", index=False, header=False)
test_df.to_csv("test_indices.csv", index=False, header=False)