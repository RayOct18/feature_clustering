import pandas as pd
import matplotlib.pyplot as plt
import sys
import re

file = sys.argv[1]
n = file.split('_')[-1]
n = re.sub('[^0-9]', '', n)
df = pd.read_csv('gmm_new/'+file)
boxplot = df.boxplot(column=['age'], by='label')

plt.savefig(sys.argv[1].split('.')[0]+'_box.png', dpi=120)

