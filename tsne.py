import numpy as np
from tsnecuda import TSNE
from matplotlib import pyplot as plt
import sys


if __name__ == '__main__':
    x = np.load(sys.argv[1])
    y = np.load(sys.argv[2])
    y = np.squeeze(y)

    X_embedded = TSNE(n_components=2, perplexity=30.0).fit_transform(x)

    print(X_embedded.shape)

    cm = plt.cm.get_cmap('RdYlBu')
    sc = plt.scatter(X_embedded[:,0], X_embedded[:,1], c=y, vmin=16, vmax=77, s=5, cmap=cm)
    plt.colorbar(sc)

    plt.savefig('./figure/'+sys.argv[3]+'.png', dpi=120)