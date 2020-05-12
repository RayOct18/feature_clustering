import pandas as pd
import matplotlib.pyplot as plt
import sys
import re

file = sys.argv[1]
n = file.split('_')[-1]
n = re.sub('[^0-9]', '', n)
df = pd.read_csv(file)
label = set(df['label'])

for i in range(len(label)):
    df_temp = df[df['label'] == i]
    quantiles = df_temp['age'].quantile([0.25, 0.5, 0.75])
    print(quantiles)
