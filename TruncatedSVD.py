import numpy as np
# from MulticoreTSNE import MulticoreTSNE as TSNE
from sklearn.manifold import TSNE
from sklearn.decomposition import TruncatedSVD
from matplotlib import pyplot as plt
import sys


if __name__ == '__main__':
    x = np.load('{}_feas.npy'.format(sys.argv[1]))
    y = np.load('{}_labels.npy'.format(sys.argv[1]))
    y = np.squeeze(y)
    for dim in [2, 3, 4, 16, 32, 64, 128, 256]:
        X_embedded = TruncatedSVD(n_components=i).fit_transform(x)

        print(X_embedded.shape)

        np.save('{}_TSVD_{}'.format(sys.argv[1], dim), X_embedded)

    # cm = plt.cm.get_cmap('RdYlBu')
    # sc = plt.scatter(X_embedded[:,0], X_embedded[:,1], c=y, vmin=16, vmax=77, s=5, cmap=cm)
    # plt.colorbar(sc)

    # plt.savefig('./figure/'+sys.argv[3]+'.png', dpi=120)
