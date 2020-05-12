import numpy as np
from sklearn.mixture import GaussianMixture
import pandas as pd


for dim in [128, 256, 512]:
    df, X = [], []
    X = np.load('{}_TSVD_{}.npy'.format(sys.argv[1], dim))
    y = np.load('{}_labels.npy'.format(sys.argv[1]))
    y = np.squeeze(y)
    name = np.load('{}_names.npy'.format(sys.argv[1]))
    for groups in [4, 5, 6, 7, 8]:
        gmm = GaussianMixture(n_components=groups, max_iter=10000).fit(X)
        label = gmm.predict(X)
        data = np.array([name, label, y]).T
        df = pd.DataFrame(data,columns=['name', 'label', 'age'])
        df.to_csv('{}_gmm_d{}_n{}.csv'.format(sys.argv[1], dim, groups), index=False)
