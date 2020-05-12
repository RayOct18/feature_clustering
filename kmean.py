from sklearn.cluster import KMeans
import numpy as np
import sys
import pandas as pd

for dim in [2, 3, 4, 16, 32, 64, 128, 256]:
    df, X = [], []
    X = np.load('{}_TSVD_{}.npy'.format(sys.argv[1], dim))
    y = np.load('{}_labels.npy'.format(sys.argv[1]))
    y = np.squeeze(y)
    name = np.load('{}_names.npy'.format(sys.argv[1]))
    for groups in [4, 6, 8, 10, 12]:
        kmean = KMeans(n_clusters=groups, n_jobs=8, max_iter=10000).fit(X)
        label = kmean.labels_
        data = np.array([name, label, y]).T
        df = pd.DataFrame(data,columns=['name', 'label', 'age'])
        df.to_csv('{}_kmean_d{}_n{}.csv'.format(sys.argv[1], dim,groups), index=False)
